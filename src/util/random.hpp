#pragma once

#include <random>

#include "../types.hpp"

class Random {
    std::uniform_real_distribution<double> uniform_dist;
    std::normal_distribution<double> normal_dist;
    std::mt19937_64 mt;

public:
    Random();

    Random(UINT seed);

    double uniform();

    double normal();

    UINT int64();

    std::uint32_t int32();
};