# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# iOS project example.
# Create project as Xcode: iOS -> Application -> Empty Application

cmake_minimum_required(VERSION 2.8.8)
project(06-example-ios.empty_application CXX)

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_include)
include(sugar_mark_macosx_resources)
include(sugar_set_xcode_ios_sdkroot)

find_package(Boost REQUIRED) # for |boost::ignore_unused_variable_warning|

include_directories(${Boost_INCLUDE_DIRS})

sugar_include("./sources")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/images")

set(PLIST_FILE "${SUGAR_ROOT}/examples/plist/ios/empty.plist.in")
set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.ios.EmptyApplication")

sugar_mark_macosx_resources(${DEFAULT_IOS_IMAGES})

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

add_executable(example MACOSX_BUNDLE ${SOURCES} ${DEFAULT_IOS_IMAGES})
sugar_set_xcode_ios_sdkroot(example ${PLIST_FILE})
