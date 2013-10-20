# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of using gtest

cmake_minimum_required(VERSION 2.8.4)
project(03-example-gtest CXX)
set(CMAKE_VERBOSE_MAKEFILE TRUE)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{GITENV_ROOT}/sugar/cmake/Sugar)

message("GTEST_ROOT from Sugar: ${GTEST_ROOT}")

include(sugar_include)

# GTEST_ROOT cmake variable will be used
find_package(Gtest REQUIRED)

include_directories("${GTEST_INCLUDE_DIRS}")

sugar_include("./sources") # fill SOURCES and UNITTEST_SOURCES

add_executable(run_bin ${SOURCES})

add_executable(test_bin ${UNITTEST_SOURCES})
target_link_libraries(test_bin ${GTEST_BOTH_LIBRARIES})
