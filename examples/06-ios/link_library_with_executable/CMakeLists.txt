# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Link library and executable in one project

cmake_minimum_required(VERSION 2.8.8)
project(06-example-ios.link_library_with_executable CXX)

include("$ENV{SUGAR_ROOT}/cmake/Sugar")

include(sugar_add_executable)
include(sugar_add_library)
include(sugar_target_link_libraries)

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

set(CMAKE_DEBUG_POSTFIX d)
set(CMAKE_OSX_SYSROOT "iphoneos")

sugar_add_library(foo foo.cpp)

sugar_add_executable(boo boo.cpp)
sugar_target_link_libraries(boo foo)
