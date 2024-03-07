#include <Kokkos_Core.hpp>
#include <Kokkos_StdAlgorithms.hpp>

#include "../types.hpp"
#include "update_ops.hpp"
#include "util/utility.hpp"

namespace qulacs {
namespace internal {
void single_qubit_dense_matrix_gate(UINT target_qubit_index,
                                    const matrix_2_2& matrix,
                                    StateVector& state) {
    Kokkos::parallel_for(
        state.dim() >> 1, KOKKOS_LAMBDA(const UINT it) {
            UINT basis_0 = internal::insert_zero_to_basis_index(it, target_qubit_index);
            UINT basis_1 = basis_0 | (1ULL << target_qubit_index);
            Complex val0 = state._raw[basis_0];
            Complex val1 = state._raw[basis_1];
            Complex res0 = matrix.val[0][0] * val0 + matrix.val[0][1] * val1;
            Complex res1 = matrix.val[1][0] * val0 + matrix.val[1][1] * val1;
            state._raw[basis_0] = res0;
            state._raw[basis_1] = res1;
        });
}
}  // namespace internal
}  // namespace qulacs
