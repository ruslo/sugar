# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of creating two targets with common sources

cmake_minimum_required(VERSION 2.8.8)
project(02-example-common CXX)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_include)

# Load "./sources/sugar.cmake" and fill variables:
#     MODULE_A_SOURCES
#     MODULE_B_SOURCES
sugar_include("./sources")

# Add ./sources directory to compiler include path (i.e. -I./sources)
include_directories("./sources")

# Add subdirectories with targets
add_subdirectory("./sources/module_a/main")
add_subdirectory("./sources/module_b/main")
