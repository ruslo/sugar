# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# iOS project example.
# Create project as Xcode: iOS -> Application -> Single View Application

cmake_minimum_required(VERSION 2.8.4)
project(06-example-ios.single_view_application CXX)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_include)
include(sugar_mark_macosx_resources)
include(sugar_set_xcode_ios_sdkroot)

find_package(Boost REQUIRED) # for |boost::ignore_unused_variable_warning|

include_directories(${Boost_INCLUDE_DIRS})

sugar_include("./sources")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/images")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/storyboards")

set(RESOURCES ${DEFAULT_IOS_IMAGES} ${IOS_STORYBOARDS_RESOURCES})
sugar_mark_macosx_resources(${RESOURCES})

set(PLIST_FILE "${SUGAR_ROOT}/examples/plist/ios/storyboard.plist.in")
set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.ios.SingleViewApplication")

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

add_executable(example MACOSX_BUNDLE ${SOURCES} ${RESOURCES})
sugar_set_xcode_ios_sdkroot(example ${PLIST_FILE})
