#include "circuit.hpp"

#include <ranges>

#include "gate/gate_factory.hpp"
#include "gate/gate_npair_qubit.hpp"
#include "gate/gate_one_control_one_target.hpp"
#include "gate/gate_one_qubit.hpp"
#include "gate/gate_pauli.hpp"
#include "gate/gate_quantum_matrix.hpp"
#include "gate/gate_two_qubit.hpp"
#include "gate/gate_zero_qubit.hpp"

namespace qulacs {
UINT Circuit::calculate_depth() const {
    std::vector<UINT> filled_step(_n_qubits, 0ULL);
    for (const auto& gate : _gate_list) {
        std::vector<UINT> control_qubits = gate->get_control_qubit_list();
        std::vector<UINT> target_qubits = gate->get_control_qubit_list();
        UINT max_step_amount_target_qubits = 0;
        for (UINT control : control_qubits) {
            if (max_step_amount_target_qubits < filled_step[control]) {
                max_step_amount_target_qubits = filled_step[control];
            }
        }
        for (UINT target : control_qubits) {
            if (max_step_amount_target_qubits < filled_step[target]) {
                max_step_amount_target_qubits = filled_step[target];
            }
        }
        for (UINT control : control_qubits) {
            filled_step[control] = max_step_amount_target_qubits + 1;
        }
        for (UINT target : target_qubits) {
            filled_step[target] = max_step_amount_target_qubits + 1;
        }
    }
    return *std::ranges::max_element(filled_step);
}

void Circuit::add_gate(const Gate& gate) {
    check_gate_is_valid(gate);
    _gate_list.push_back(gate->copy());
}
void Circuit::add_gate(Gate&& gate) {
    check_gate_is_valid(gate);
    _gate_list.push_back(std::move(gate));
}
void Circuit::add_circuit(const Circuit& circuit) {
    for (const auto& gate : circuit._gate_list) {
        add_gate(gate);
    }
}
void Circuit::add_circuit(Circuit&& circuit) {
    for (auto&& gate : circuit._gate_list) {
        add_gate(std::move(gate));
    }
}

void Circuit::update_quantum_state(StateVector& state) const {
    for (const auto& gate : _gate_list) {
        gate->update_quantum_state(state);
    }
}

Circuit Circuit::copy() const {
    Circuit ccircuit(_n_qubits);
    for (const auto& gate : _gate_list) {
        ccircuit.add_gate(gate->copy());
    }
    return ccircuit;
}

Circuit Circuit::get_inverse() const {
    Circuit icircuit(_n_qubits);
    for (const auto& gate : _gate_list | std::views::reverse) {
        icircuit.add_gate(gate->get_inverse());
    }
    return icircuit;
}

void Circuit::optimize() {
    std::vector<Gate> optimized;
    UINT no_waiting_gate = std::numeric_limits<qulacs::UINT>::max();
    std::vector<UINT> waiting_gate(_n_qubits, no_waiting_gate);
    double global_phase = 0.;
    for (UINT i : std::views::iota(_gate_list.size())) {
        const Gate& gate = _gate_list[i];
        if (gate.gate_type() == GateType::I) continue;
        if (gate.gate_type() == GateType::GlobalPhase) {
            global_phase += GlobalPhaseGate(gate)->angle();
            continue;
        }
        auto control_target = {gate->get_control_qubit_list(), gate->get_target_qubit_list()};
        auto target_view = control_target | std::views::join;
        UINT waiting = [&] {
            UINT res = no_waiting_gate;
            for (UINT target : target_view) {
                if (waiting_gate[target] == res) continue;
                if (waiting_gate[target] == no_waiting_gate) continue;
                if (res != no_waiting_gate) return no_waiting_gate;
                res = waiting_gate[target];
            }
            return res;
        }();
        auto merge_gate = [](Gate g1, Gate g2) -> std::optional<std::pair<Gate, double>> {
            auto g1type = g1.gate_type(), g2type = g2.gate_type();
            if (g1type == GateType::X) {
                if (g2type == GateType::X) return std::make_pair(I(), 0.);
                if (g2type == GateType::Y) return std::make_pair(Z(XGate(g1)->target()), -PI() / 2);
                if (g2type == GateType::Z) return std::make_pair(Y(XGate(g1)->target()), PI() / 2);
            }
        };
    }
}

void Circuit::check_gate_is_valid(const Gate& gate) const {
    auto targets = gate->get_target_qubit_list();
    auto controls = gate->get_control_qubit_list();
    bool valid = true;
    if (!targets.empty()) valid &= *std::max_element(targets.begin(), targets.end()) < _n_qubits;
    if (!controls.empty()) valid &= *std::max_element(controls.begin(), controls.end()) < _n_qubits;
    if (!valid) {
        throw std::runtime_error("Gate to be added to the circuit has invalid qubit range");
    }
}
}  // namespace qulacs
