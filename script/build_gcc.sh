#!/bin/sh

set -eux

GCC_COMMAND=${C_COMPILER:-"gcc"}
GXX_COMMAND=${CXX_COMPILER:-"g++"}

QULACS_USE_OMP=${QULACS_USE_OMP:-"ON"}
QULACS_USE_CUDA=${QULACS_USE_CUDA:-"OFF"}
QULACS_USE_TEST=${QULACS_USE_TEST:-"ON"}
QULACS_USE_EXE=${QULACS_USE_EXE:-"ON"}

CMAKE_OPS="-D CMAKE_C_COMPILER=$GCC_COMMAND
  -D CMAKE_CXX_COMPILER=$GXX_COMMAND \
  -D CMAKE_BUILD_TYPE=Release \
  -D QULACS_USE_OMP=${QULACS_USE_OMP} \
  -D QULACS_USE_CUDA=${QULACS_USE_CUDA} \
  -D QULACS_USE_TEST=${QULACS_USE_TEST}"

mkdir -p ./build
cmake -B build -G Ninja ${CMAKE_OPS}
ninja -C build -j $(nproc)
