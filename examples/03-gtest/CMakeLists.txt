# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of using gtest

cmake_minimum_required(VERSION 2.8.4)
project(03-example-gtest CXX)
set(CMAKE_VERBOSE_MAKEFILE TRUE)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{GITENV_ROOT}/sugar/cmake/Sugar)

include(sugar_setup_gitenv_paths)
include(sugar_include)

# Set GTEST_ROOT cmake variable using GITENV_ROOT environment variable
sugar_setup_gitenv_paths()

message("GTEST_ROOT from Sugar: ${GTEST_ROOT}")

# Use GTEST_ROOT cmake variable
find_package(GTest REQUIRED)

include_directories("${GTEST_INCLUDE_DIRS}")

sugar_include("./sources") # fill SOURCES and UNITTEST_SOURCES

add_executable(run_bin ${SOURCES})

add_executable(test_bin ${UNITTEST_SOURCES})
target_link_libraries(test_bin ${GTEST_BOTH_LIBRARIES})
if(UNIX)
  target_link_libraries(test_bin pthread)
endif()
