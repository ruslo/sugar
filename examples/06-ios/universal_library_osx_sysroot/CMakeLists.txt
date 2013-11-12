# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Build universal library with 'sugar_install_library'

cmake_minimum_required(VERSION 2.8.8)
project(06-example-ios.universal_library_osx_sysroot CXX)

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_include)
include(sugar_install_library)

sugar_include("./sources")

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

add_library(universal_lib_example ${SOURCES})

set(CMAKE_OSX_SYSROOT "iphoneos")

install(FILES "./sources/A.hpp" DESTINATION "./include")
sugar_install_library(TARGETS universal_lib_example DESTINATION "./lib/ios/")
