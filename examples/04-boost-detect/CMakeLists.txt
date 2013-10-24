# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of boost detection

cmake_minimum_required(VERSION 2.8.4)
project(04-example-boost-detect CXX)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_setup_gitenv_paths)
sugar_setup_gitenv_paths()

set(Boost_USE_STATIC_LIBS ON)
find_package(Boost REQUIRED COMPONENTS thread system)

message("Boost include dirs: ${Boost_INCLUDE_DIRS}")

include_directories(${Boost_INCLUDE_DIRS})

add_executable(detect_bin "./main.cpp")
target_link_libraries(detect_bin ${Boost_LIBRARIES})
