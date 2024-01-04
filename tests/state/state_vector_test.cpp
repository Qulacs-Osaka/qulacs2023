#include <gtest/gtest.h>

#include <Eigen/Core>
#include <Kokkos_Core.hpp>
#include <numeric>
#include <state/state_vector.hpp>

#include "../test_environment.hpp"
#include "util/utility.hpp"

namespace qulacs {

const double eps = 1e-12;

bool same_state(const StateVector& s1, const StateVector& s2) {
    auto s1_cp = s1.amplitudes();
    auto s2_cp = s2.amplitudes();
    assert(s1.n_qubits() == s2.n_qubits());
    for (UINT i = 0; i < s1.dim(); ++i) {
        if (Kokkos::abs(s1_cp[i] - s2_cp[i]) > eps) return false;
    }
    return true;
};

TEST(StateVectorTest, HaarRandomStateNorm) {
    const int n_tries = 20;
    for (int n = 1; n <= n_tries; n++) {
        const auto state = StateVector::Haar_random_state(n);
        ASSERT_NEAR(state.compute_squared_norm(), 1., eps);
    }
}

TEST(StateVectorTest, ZeroNormState) {
    const UINT n = 5;

    StateVector state(StateVector::Haar_random_state(n));
    state.set_zero_norm_state();
    auto state_cp = state.amplitudes();

    for (UINT i = 0; i < state.dim(); ++i) {
        ASSERT_EQ(state_cp[i], Complex(0, 0));
    }
}

TEST(StateVectorTest, ComputationalBasisState) {
    const UINT n = 5;

    StateVector state(StateVector::Haar_random_state(n));
    state.set_computational_basis(31);
    auto state_cp = state.amplitudes();

    for (UINT i = 0; i < state.dim(); ++i) {
        if (i == 31) {
            ASSERT_EQ(state_cp[i], Complex(1, 0));
        } else {
            ASSERT_EQ(state_cp[i], Complex(0, 0));
        }
    }
}

TEST(StateVectorTest, HaarRandomStateSameSeed) {
    const UINT n = 10, m = 5;
    for (UINT i = 0; i < m; ++i) {
        StateVector state1(StateVector::Haar_random_state(n, i)),
            state2(StateVector::Haar_random_state(n, i));
        ASSERT_TRUE(same_state(state1, state2));
    }
}

TEST(StateVectorTest, StateTest_HaarRandomStateWithoutSeed) {
    const UINT n = 10, m = 5;
    for (UINT i = 0; i < m; ++i) {
        StateVector state1(StateVector::Haar_random_state(n)),
            state2(StateVector::Haar_random_state(n));
        ASSERT_FALSE(same_state(state1, state2));
    }
}

TEST(StateVectorTest, AddState) {
    const UINT n = 10;
    StateVector state1(StateVector::Haar_random_state(n));
    StateVector state2(StateVector::Haar_random_state(n));
    auto vec1 = state1.amplitudes();
    auto vec2 = state2.amplitudes();
    state1.add_state_vector(state2);
    auto new_vec = state1.amplitudes();

    for (UINT i = 0; i < state1.dim(); ++i) {
        ASSERT_NEAR(new_vec[i].real(), vec1[i].real() + vec2[i].real(), eps);
        ASSERT_NEAR(new_vec[i].imag(), vec1[i].imag() + vec2[i].imag(), eps);
    }
}

TEST(StateVectorTest, AddStateWithCoef) {
    const std::complex<double> coef(2.5, 1.3);
    const UINT n = 10;
    StateVector state1(StateVector::Haar_random_state(n));
    StateVector state2(StateVector::Haar_random_state(n));
    auto vec1 = state1.amplitudes();
    auto vec2 = state2.amplitudes();

    state1.add_state_vector_with_coef(coef, state2);
    auto new_vec = state1.amplitudes();

    for (UINT i = 0; i < state1.dim(); ++i) {
        ASSERT_NEAR(new_vec[i].real(),
                    vec1[i].real() + coef.real() * vec2[i].real() - coef.imag() * vec2[i].imag(),
                    eps);
        ASSERT_NEAR(new_vec[i].imag(),
                    vec1[i].imag() + coef.real() * vec2[i].imag() + coef.imag() * vec2[i].real(),
                    eps);
    }
}

TEST(StateVectorTest, MultiplyCoef) {
    const UINT n = 10;
    const Complex coef(0.5, 0.2);

    StateVector state(StateVector::Haar_random_state(n));
    auto vec = state.amplitudes();
    state.multiply_coef(coef);
    auto new_vec = state.amplitudes();

    for (UINT i = 0; i < state.dim(); ++i) {
        ASSERT_NEAR(new_vec[i].real(), (coef * vec[i]).real(), eps);
        ASSERT_NEAR(new_vec[i].imag(), (coef * vec[i]).imag(), eps);
    }
}

TEST(StateVectorTest, GetZeroProbability) {
    const UINT n = 10;
    StateVector state(n);
    state.set_computational_basis(1);
    for (UINT i = 2; i <= 10; ++i) {
        StateVector tmp_state(n);
        tmp_state.set_computational_basis(i);
        state.add_state_vector_with_coef(std::sqrt(i), tmp_state);
    }
    state.normalize();
    ASSERT_NEAR(state.get_zero_probability(0), 30.0 / 55.0, eps);
    ASSERT_NEAR(state.get_zero_probability(1), 27.0 / 55.0, eps);
    ASSERT_NEAR(state.get_zero_probability(2), 33.0 / 55.0, eps);
    ASSERT_NEAR(state.get_zero_probability(3), 28.0 / 55.0, eps);
}

TEST(StateVectorTest, EntropyCalculation) {
    const UINT n = 6;
    const UINT dim = 1ULL << n;
    const UINT max_repeat = 10;

    StateVector state(n);
    for (UINT rep = 0; rep < max_repeat; ++rep) {
        state = StateVector::Haar_random_state(n);
        auto state_cp = state.amplitudes();
        ASSERT_NEAR(state.compute_squared_norm(), 1, eps);
        Eigen::VectorXcd test_state(dim);
        for (UINT i = 0; i < dim; ++i) test_state[i] = (Complex)state_cp[i];

        for (UINT target = 0; target < n; ++target) {
            double ent = 0;
            for (UINT ind = 0; ind < dim; ++ind) {
                double prob = norm2(test_state[ind]);
                if (prob > eps) ent += -prob * log(prob);
            }
            ASSERT_NEAR(ent, state.get_entropy(), eps);
        }
    }
}

TEST(StateVectorTest, GetMarginalProbability) {
    const UINT n = 2;
    const UINT dim = 1 << n;
    StateVector state(StateVector::Haar_random_state(n));
    auto state_cp = state.amplitudes();
    std::vector<double> probs;
    for (UINT i = 0; i < dim; ++i) {
        probs.push_back(norm2(state_cp[i]));
    }
    ASSERT_NEAR(state.get_marginal_probability({0, 0}), probs[0], eps);
    ASSERT_NEAR(state.get_marginal_probability({1, 0}), probs[1], eps);
    ASSERT_NEAR(state.get_marginal_probability({0, 1}), probs[2], eps);
    ASSERT_NEAR(state.get_marginal_probability({1, 1}), probs[3], eps);
    ASSERT_NEAR(state.get_marginal_probability({0, 2}), probs[0] + probs[2], eps);
    ASSERT_NEAR(state.get_marginal_probability({1, 2}), probs[1] + probs[3], eps);
    ASSERT_NEAR(state.get_marginal_probability({2, 0}), probs[0] + probs[1], eps);
    ASSERT_NEAR(state.get_marginal_probability({2, 1}), probs[2] + probs[3], eps);
    ASSERT_NEAR(state.get_marginal_probability({2, 2}), 1., eps);
}

TEST(StateVectorTest, SamplingSuperpositionState) {
    const UINT n = 10;
    const UINT nshot = 1024;
    const UINT test_count = 10;
    UINT pass_count = 0;
    for (UINT test_i = 0; test_i < test_count; test_i++) {
        StateVector state(n);
        state.set_computational_basis(0);
        for (UINT i = 1; i <= 4; ++i) {
            StateVector tmp_state(n);
            tmp_state.set_computational_basis(i);
            state.add_state_vector_with_coef(1 << i, tmp_state);
        }
        state.normalize();
        std::vector<size_t> res = state.sampling(nshot);

        std::array<UINT, 5> cnt = {};
        for (UINT i = 0; i < nshot; ++i) {
            ASSERT_GE(res[i], 0);
            ASSERT_LE(res[i], 4);
            cnt[res[i]] += 1;
        }
        bool pass = true;
        for (UINT i = 0; i < 4; i++) {
            std::string err_message = _CHECK_GT(cnt[i + 1], cnt[i]);
            if (err_message != "") {
                pass = false;
                std::cerr << err_message;
            }
        }
        if (pass) pass_count++;
    }
    ASSERT_GE(pass_count, test_count - 1);
}

TEST(StateVectorTest, SamplingComputationalBasis) {
    const UINT n = 10;
    const UINT nshot = 1024;
    StateVector state(n);
    state.set_computational_basis(100);
    auto res = state.sampling(nshot);
    for (UINT i = 0; i < nshot; ++i) {
        ASSERT_TRUE(res[i] == 100);
    }
}

}  // namespace qulacs
