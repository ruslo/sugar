# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of using 'sugar_add_ios_gtest'

# To run this example build gtest for iOS and set environment or cmake
# variable to GTEST_ROOT. As alternative toolchain files may be used.
# See https://github.com/ruslo/polly

cmake_minimum_required(VERSION 2.8.4)
project(06-example-ios.gtest CXX)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_add_ios_gtest)
include(sugar_include)
include(sugar_mark_macosx_resources)
include(sugar_set_xcode_ios_sdkroot)

sugar_include("./sources")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/images")

set(PLIST_FILE "${SUGAR_ROOT}/examples/plist/ios/empty.plist.in")
set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.ios.Gtest")

sugar_mark_macosx_resources(${DEFAULT_IOS_IMAGES})

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

find_package(GTest REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS})

add_executable(example MACOSX_BUNDLE ${SOURCES} ${DEFAULT_IOS_IMAGES})
target_link_libraries(example ${GTEST_BOTH_LIBRARIES})
sugar_set_xcode_ios_sdkroot(example ${PLIST_FILE})

enable_testing()
sugar_add_ios_gtest(MyTest example)
