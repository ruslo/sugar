# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of build and install universal ("fat", iphone + simulator) iOS library
# + workaround for http://public.kitware.com/Bug/view.php?id=12506

# Note:
#     leading underscore need for test.py build this project first,
#     because link_library example use it

cmake_minimum_required(VERSION 2.8.4)
project(06-example-ios.universal_library CXX)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_include)
include(sugar_install_ios_library)

sugar_include("./sources")

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

add_library(universal_lib_example ${SOURCES})

set_target_properties(
    universal_lib_example
    ${target}
    PROPERTIES
    XCODE_ATTRIBUTE_SDKROOT
    "iphoneos"
)

install(FILES "./sources/A.hpp" DESTINATION "./include")
sugar_install_ios_library(universal_lib_example "./lib/ios/")
