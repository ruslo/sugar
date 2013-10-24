# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Cocoa project example.
# Create project as Xcode: OS X -> Application -> Cocoa Application

cmake_minimum_required(VERSION 2.8.4)
project(07-cocoa-application.example CXX)
set(SUGAR_STATUS_PRINT TRUE) # print process messages
set(SUGAR_STATUS_DEBUG FALSE) # print ALL process messages

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_include)
include(sugar_mark_macosx_resources)
include(sugar_target_add_framework)

find_package(Boost REQUIRED) # for |boost::ignore_unused_variable_warning|

include_directories(${Boost_INCLUDE_DIRS})

if(NOT XCODE_VERSION)
  message(WARNING "___ MAY NOT WORK, NEED TO BUILD IN XCODE ___")
endif()

sugar_include("./sources") # fill SOURCES
sugar_include("./resources") # fill RESOURCES

sugar_mark_macosx_resources(${RESOURCES})

add_executable(
    cocoa-test-application
    MACOSX_BUNDLE
    ${SOURCES}
    ${RESOURCES}
)

set_target_properties(
    cocoa-test-application
    PROPERTIES
    MACOSX_BUNDLE_INFO_PLIST
    "${SUGAR_ROOT}/examples/plist/macosx/default.plist.in"
)

sugar_target_add_framework(cocoa-test-application "AppKit")
