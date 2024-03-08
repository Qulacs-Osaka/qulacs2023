from enum import Enum
from typing import (Any, Callable, Iterable, Optional, Sequence, Typing, Union,
                    overload)

import qulacs2023

def CX(arg0: int, arg1: int, /) -> qulacs2023.qulacs_core.Gate: ...

class CXGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def control(self) -> int: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def CZ(arg0: int, arg1: int, /) -> qulacs2023.qulacs_core.Gate: ...

class CZGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def control(self) -> int: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

class Circuit:
    """
    None
    """

    def __init__(self, arg: int, /) -> None: ...
    def add_circuit(self, arg: qulacs2023.qulacs_core.Circuit, /) -> None: ...
    def add_gate(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def calculate_depth(self) -> int: ...
    def copy(self) -> qulacs2023.qulacs_core.Circuit: ...
    def gate_count(self) -> int: ...
    def gate_list(self) -> list[qulacs2023.qulacs_core.Gate]: ...
    def get(self, arg: int, /) -> qulacs2023.qulacs_core.Gate: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Circuit: ...
    def n_qubits(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def FusedSwap(arg0: int, arg1: int, arg2: int, /) -> qulacs2023.qulacs_core.Gate: ...

class FusedSwapGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def block_size(self) -> int: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def qubit_index1(self) -> int: ...
    def qubit_index2(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

class Gate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

class GateType(Enum):
    """
    <attribute '__doc__' of 'GateType' objects>
    """

    CX: Any

    CZ: Any

    FusedSwap: Any

    GlobalPhase: Any

    H: Any

    I: Any

    P0: Any

    P1: Any

    Pauli: Any

    PauliRotation: Any

    RX: Any

    RY: Any

    RZ: Any

    S: Any

    Sdag: Any

    SqrtX: Any

    SqrtXdag: Any

    SqrtY: Any

    SqrtYdag: Any

    Swap: Any

    T: Any

    Tdag: Any

    U1: Any

    U2: Any

    U3: Any

    X: Any

    Y: Any

    Z: Any

def GlobalPhase(arg: float, /) -> qulacs2023.qulacs_core.Gate: ...

class GlobalPhaseGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def phase(self) -> float: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def H(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class HGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def I() -> qulacs2023.qulacs_core.Gate: ...

class IGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

class InitializationSettings:
    """
    None
    """

    def __init__(self) -> None: ...
    def get_device_id(self) -> int: ...
    def get_disable_warnings(self) -> bool: ...
    def get_map_device_id_by(self) -> str: ...
    def get_num_threads(self) -> int: ...
    def get_print_configuration(self) -> bool: ...
    def get_tools_args(self) -> str: ...
    def get_tools_help(self) -> bool: ...
    def get_tools_libs(self) -> str: ...
    def get_tune_internals(self) -> bool: ...
    def has_device_id(self) -> bool: ...
    def has_disable_warnings(self) -> bool: ...
    def has_map_device_id_by(self) -> bool: ...
    def has_num_threads(self) -> bool: ...
    def has_print_configuration(self) -> bool: ...
    def has_tools_args(self) -> bool: ...
    def has_tools_help(self) -> bool: ...
    def has_tools_libs(self) -> bool: ...
    def has_tune_internals(self) -> bool: ...
    def set_device_id(
        self, arg: int, /
    ) -> qulacs2023.qulacs_core.InitializationSettings: ...
    def set_disable_warnings(
        self, arg: bool, /
    ) -> qulacs2023.qulacs_core.InitializationSettings: ...
    def set_map_device_id_by(
        self, arg: str, /
    ) -> qulacs2023.qulacs_core.InitializationSettings: ...
    def set_num_threads(
        self, arg: int, /
    ) -> qulacs2023.qulacs_core.InitializationSettings: ...
    def set_print_configuration(
        self, arg: bool, /
    ) -> qulacs2023.qulacs_core.InitializationSettings: ...
    def set_tools_args(
        self, arg: str, /
    ) -> qulacs2023.qulacs_core.InitializationSettings: ...
    def set_tools_help(
        self, arg: bool, /
    ) -> qulacs2023.qulacs_core.InitializationSettings: ...
    def set_tools_libs(
        self, arg: str, /
    ) -> qulacs2023.qulacs_core.InitializationSettings: ...
    def set_tune_internals(
        self, arg: bool, /
    ) -> qulacs2023.qulacs_core.InitializationSettings: ...

class Operator:
    """
    None
    """

    def __init__(self, arg: int, /) -> None: ...
    def add_operator(self, arg: qulacs2023.qulacs_core.PauliOperator, /) -> None: ...
    def add_random_operator(
        self, operator_count: int, seed: Optional[int] = None
    ) -> None: ...
    def apply_to_state(self, arg: qulacs2023.qulacs_core.StateVector, /) -> None: ...
    def get_dagger(self) -> qulacs2023.qulacs_core.Operator: ...
    def get_expectation_value(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> complex: ...
    def get_transition_amplitude(
        self,
        arg0: qulacs2023.qulacs_core.StateVector,
        arg1: qulacs2023.qulacs_core.StateVector,
        /,
    ) -> complex: ...
    def is_hermitian(self) -> bool: ...
    def n_qubits(self) -> int: ...
    def optimize(self) -> None: ...
    def terms(self) -> list[qulacs2023.qulacs_core.PauliOperator]: ...
    def to_string(self) -> str: ...

def P0(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class P0Gate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def P1(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class P1Gate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

class PauliOperator:
    """
    None
    """

    def __init__(
        self, bit_flip_mask: int, phase_flip_mask: int, coef: complex = 1.0
    ) -> None:
        """
        __init__(self, bit_flip_mask: int, phase_flip_mask: int, coef: complex = 1.0) -> None
        """
        ...

    @overload
    def __init__(self, coef: complex = 1.0) -> None:
        """
        __init__(self, coef: complex = 1.0) -> None
        """
        ...

    @overload
    def __init__(
        self,
        target_qubit_list: list[int],
        pauli_id_list: list[int],
        coef: complex = 1.0,
    ) -> None:
        """
        __init__(self, target_qubit_list: list[int], pauli_id_list: list[int], coef: complex = 1.0) -> None
        """
        ...

    @overload
    def __init__(self, pauli_string: str, coef: complex = 1.0) -> None:
        """
        __init__(self, pauli_string: str, coef: complex = 1.0) -> None
        """
        ...

    @overload
    def __init__(self, pauli_id_par_qubit: list[int], coef: complex = 1.0) -> None:
        """
        __init__(self, pauli_id_par_qubit: list[int], coef: complex = 1.0) -> None
        """
        ...

    def add_single_pauli(self, arg0: int, arg1: int, /) -> None: ...
    def apply_to_state(self, arg: qulacs2023.qulacs_core.StateVector, /) -> None: ...
    def change_coef(self, arg: complex, /) -> None: ...
    def get_XZ_mask_representation(self) -> tuple[int, int]: ...
    def get_coef(self) -> complex: ...
    def get_dagger(self) -> qulacs2023.qulacs_core.PauliOperator: ...
    def get_expectation_value(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> complex: ...
    def get_pauli_id_list(self) -> list[int]: ...
    def get_pauli_string(self) -> str: ...
    def get_qubit_count(self) -> int: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def get_transition_amplitude(
        self,
        arg0: qulacs2023.qulacs_core.StateVector,
        arg1: qulacs2023.qulacs_core.StateVector,
        /,
    ) -> complex: ...

def RX(arg0: int, arg1: float, /) -> qulacs2023.qulacs_core.Gate: ...

class RXGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def angle(self) -> float: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def RY(arg0: int, arg1: float, /) -> qulacs2023.qulacs_core.Gate: ...

class RYGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def angle(self) -> float: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def RZ(arg0: int, arg1: float, /) -> qulacs2023.qulacs_core.Gate: ...

class RZGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def angle(self) -> float: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def S(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class SGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def Sdag(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class SdagGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def SqrtX(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class SqrtXGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def SqrtXdag(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class SqrtXdagGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def SqrtY(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class SqrtYGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def SqrtYdag(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class SqrtYdagGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

class StateVector:
    """
    None
    """

    def Haar_random_state(
        n_qubits: int, seed: Optional[int] = None
    ) -> qulacs2023.qulacs_core.StateVector: ...
    def __init__(self, arg: qulacs2023.qulacs_core.StateVector) -> None:
        """
        __init__(self, arg: qulacs2023.qulacs_core.StateVector) -> None
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        __init__(self) -> None
        """
        ...

    @overload
    def __init__(self, arg: int, /) -> None:
        """
        __init__(self, arg: int, /) -> None
        """
        ...

    def add_state_vector(self, arg: qulacs2023.qulacs_core.StateVector, /) -> None: ...
    def add_state_vector_with_coef(
        self, arg0: complex, arg1: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...
    def amplitudes(self) -> list[complex]: ...
    def dim(self) -> int: ...
    def get_amplitude_at_index(self, arg: int, /) -> complex: ...
    def get_entropy(self) -> float: ...
    def get_marginal_probability(self, arg: list[int], /) -> float: ...
    def get_squared_norm(self) -> float: ...
    def get_zero_probability(self, arg: int, /) -> float: ...
    def load(self, arg: list[complex], /) -> None: ...
    def multiply_coef(self, arg: complex, /) -> None: ...
    def n_qubits(self) -> int: ...
    def normalize(self) -> None: ...
    def sampling(
        self, sampling_count: int, seed: Optional[int] = None
    ) -> list[int]: ...
    def set_amplitude_at_index(self, arg0: int, arg1: complex, /) -> None: ...
    def set_computational_basis(self, arg: int, /) -> None: ...
    def set_zero_norm_state(self) -> None: ...
    def set_zero_state(self) -> None: ...
    def to_string(self) -> str: ...

def Swap(arg0: int, arg1: int, /) -> qulacs2023.qulacs_core.Gate: ...

class SwapGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target1(self) -> int: ...
    def target2(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def T(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class TGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def Tdag(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class TdagGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def U1(arg0: int, arg1: float, /) -> qulacs2023.qulacs_core.Gate: ...

class U1Gate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def lambda_(self) -> float: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def U2(arg0: int, arg1: float, arg2: float, /) -> qulacs2023.qulacs_core.Gate: ...

class U2Gate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def lambda_(self) -> float: ...
    def phi(self) -> float: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def U3(
    arg0: int, arg1: float, arg2: float, arg3: float, /
) -> qulacs2023.qulacs_core.Gate: ...

class U3Gate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def lambda_(self) -> float: ...
    def phi(self) -> float: ...
    def theta(self) -> float: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def X(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class XGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def Y(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class YGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def Z(arg: int, /) -> qulacs2023.qulacs_core.Gate: ...

class ZGate:
    """
    None
    """

    def __init__(self, arg: qulacs2023.qulacs_core.Gate, /) -> None: ...
    def copy(self) -> qulacs2023.qulacs_core.Gate: ...
    def gate_type(self) -> qulacs2023.qulacs_core.GateType: ...
    def get_control_qubit_list(self) -> list[int]: ...
    def get_inverse(self) -> qulacs2023.qulacs_core.Gate: ...
    def get_target_qubit_list(self) -> list[int]: ...
    def target(self) -> int: ...
    def update_quantum_state(
        self, arg: qulacs2023.qulacs_core.StateVector, /
    ) -> None: ...

def finalize() -> None: ...
def initialize(
    settings: qulacs2023.qulacs_core.InitializationSettings = ...,
) -> None: ...
