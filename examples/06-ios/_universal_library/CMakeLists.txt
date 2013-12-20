# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of build and install universal ("fat", iphone + simulator) iOS library
# + workaround for http://public.kitware.com/Bug/view.php?id=12506

# Note:
#     leading underscore need for test.py build this project first,
#     because link_library example use it

cmake_minimum_required(VERSION 2.8.8)
project(06-example-ios.universal_library CXX)

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_add_ios_library)
include(sugar_include)
include(sugar_install_ios_library)

sugar_include("./sources")

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

set(CMAKE_DEBUG_POSTFIX d)

sugar_add_ios_library(universal_lib_example ${SOURCES})

install(FILES "./sources/A.hpp" DESTINATION "./include")
sugar_install_ios_library(universal_lib_example "./lib/ios/")
