# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of generating groups for Xcode and MSVC

cmake_minimum_required(VERSION 2.8.4)
project(05-example-groups CXX)
set(CMAKE_VERBOSE_MAKEFILE TRUE)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_include)

sugar_include("./sources")

include_directories("./sources")

add_subdirectory("./sources/module_a/main")
add_subdirectory("./sources/module_b/main")
