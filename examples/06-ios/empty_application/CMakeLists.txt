# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# iOS project example.
# Create project as Xcode: iOS -> Application -> Empty Application

cmake_minimum_required(VERSION 2.8.4)
project(06-example-ios.empty_application CXX)
set(CMAKE_VERBOSE_MAKEFILE TRUE)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{GITENV_ROOT}/sugar/cmake/Sugar)

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

if(XCODE_VERSION)
  add_executable(example MACOSX_BUNDLE ${SOURCES} ${DEFAULT_IOS_IMAGES})
  sugar_set_xcode_ios_sdkroot(example ${PLIST_FILE})
else()
  # for build testing
endif()
