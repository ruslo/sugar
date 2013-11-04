# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of linking to timestamp library with current build time

cmake_minimum_required(VERSION 2.8.8)
project(11-example-timestamp CXX)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG TRUE) # print ALL process messages

include($ENV{SUGAR_ROOT}/cmake/Sugar)
include(sugar_link_timestamp)

add_executable(timestamp_bin "main.cpp")
sugar_link_timestamp(timestamp_bin)
