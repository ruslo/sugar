# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Detecting rapidjson with GITENV_ROOT

cmake_minimum_required(VERSION 2.8.4)
project(09-example-rapidjson CXX)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{GITENV_ROOT}/sugar/cmake/Sugar)

include(sugar_setup_gitenv_paths)

sugar_setup_gitenv_paths()
include_directories(${RAPIDJSON_INCLUDE_DIRS})

add_executable(json_bin "./main.cpp")
