#pragma once

#include "../state/state_vector.hpp"
#include "../types.hpp"

namespace qulacs {
namespace internal {
// forward declarations
class GateBase;

template <typename T>
concept GateImpl = std::derived_from<T, GateBase>;

class IGateImpl;
class GlobalPhaseImpl;
class XGateImpl;
class YGateImpl;
class ZGateImpl;
class HGateImpl;
class SGateImpl;
class SdagGateImpl;
class TGateImpl;
class TdagGateImpl;
class SqrtXGateImpl;
class SqrtXdagGateImpl;
class SqrtYGateImpl;
class SqrtYdagGateImpl;
class P0GateImpl;
class P1GateImpl;
class RXGateImpl;
class RYGateImpl;
class RZGateImpl;
class U1GateImpl;
class U2GateImpl;
class U3GateImpl;
class CXGateImpl;
class CZGateImpl;
class SwapGateImpl;
class FusedSwapGateImpl;
class PauliGateImpl;
class PauliRotationGateImpl;

template <GateImpl T>
class GatePtr;
}  // namespace internal
using Gate = internal::GatePtr<internal::GateBase>;

enum class GateType {
    I,
    GlobalPhase,
    X,
    Y,
    Z,
    H,
    S,
    Sdag,
    T,
    Tdag,
    SqrtX,
    SqrtXdag,
    SqrtY,
    SqrtYdag,
    P0,
    P1,
    RX,
    RY,
    RZ,
    U1,
    U2,
    U3,
    CX,
    CZ,
    Swap,
    FusedSwap,
    Pauli,
    PauliRotation
};

template <internal::GateImpl T>
constexpr GateType get_gate_type() {
    if constexpr (internal::IGateImpl) return GateType::I;
    if constexpr (internal::GlobalPhaseGateImpl) return GateType::GlobalPhase;
    if constexpr (internal::XGateImpl) return GateType::X;
    if constexpr (internal::YGateImpl) return GateType::Y;
    if constexpr (internal::ZGateImpl) return GateType::Z;
    if constexpr (internal::HGateImpl) return GateType::H;
    if constexpr (internal::SGateImpl) return GateType::S;
    if constexpr (internal::SdagGateImpl) return GateType::Sdag;
    if constexpr (internal::TGateImpl) return GateType::T;
    if constexpr (internal::TdagGateImpl) return GateType::Tdag;
    if constexpr (internal::SqrtXGateImpl) return GateType::SqrtX;
    if constexpr (internal::SqrtXdagGateImpl) return GateType::SqrtXdag;
    if constexpr (internal::SqrtYGateImpl) return GateType::SqrtY;
    if constexpr (internal::SqrtYdagGateImpl) return GateType::SqrtYdag;
    if constexpr (internal::P0GateImpl) return GateType::P0;
    if constexpr (internal::P1GateImpl) return GateType::P1;
    if constexpr (internal::RXGateImpl) return GateType::RX;
    if constexpr (internal::RYGateImpl) return GateType::RY;
    if constexpr (internal::RZGateImpl) return GateType::RZ;
    if constexpr (internal::U1GateImpl) return GateType::U1;
    if constexpr (internal::U2GateImpl) return GateType::U2;
    if constexpr (internal::U3GateImpl) return GateType::U3;
    if constexpr (internal::CXGateImpl) return GateType::CX;
    if constexpr (internal::CZGateImpl) return GateType::CZ;
    if constexpr (internal::SwapGateImpl) return GateType::Swap;
    if constexpr (internal::FusedSwapGateImpl) return GateType::FusedSwap;
    if constexpr (internal::PauliGateImpl) return GateType::Pauli;
    if constexpr (internal::PauliRotationGateImpl) return GateType::PauliRotation;
    static_assert("unknown GateImpl");
}

namespace internal {
class GateBase {
public:
    virtual ~GateBase() = default;

    [[nodiscard]] virtual std::vector<UINT> get_target_qubit_list() const = 0;
    [[nodiscard]] virtual std::vector<UINT> get_control_qubit_list() const = 0;

    [[nodiscard]] virtual Gate copy() const = 0;
    [[nodiscard]] virtual Gate get_inverse() const = 0;

    virtual void update_quantum_state(StateVector& state_vector) const = 0;
};

template <GateImpl T>
class GatePtr {
    friend class GateFactory;
    template <GateImpl U>
    friend class GatePtr;

private:
    std::shared_ptr<T> _gate_ptr;
    GateType _gate_type;

public:
    GatePtr() = default;
    GatePtr(const GatePtr& gate) = default;
    template <GateImpl U>
    GatePtr(const std::shared_ptr<U>& gate_ptr) {
        if constexpr (std::is_same_v<T, U>) {
            _gate_ptr = gate_ptr;
        } else if constexpr (std::is_same_v<T, internal::GateBase>) {
            _gate_ptr = std::static_pointer_cast<T>(gate_ptr);
        } else {
            if (_gate_type != get_gate_type<T>()) {
                throw std::runtime_error("invalid gate cast");
            }
            _gate_ptr = std::static_pointer_cast<T>(gate_ptr);
        }
    }
    template <GateImpl U>
    GatePtr(const GatePtr<U>& gate) : GatePtr(gate._gate_ptr) {}

    GateType gate_type() const { return _gate_type; }

    T* operator->() const {
        if (!_gate_ptr) {
            throw std::runtime_error("GatePtr::operator->(): Gate is Null");
        }
        return _gate_ptr.get();
    }
};
}  // namespace internal

}  // namespace qulacs
