# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# iOS project example.
# Create project as Xcode: iOS -> Application -> Single View Application

cmake_minimum_required(VERSION 2.8.11)
project(06-example-ios.single_view_application CXX)

include("$ENV{SUGAR_ROOT}/cmake/Sugar")

include(sugar_include)
include(sugar_set_xcode_ios_sdkroot)

include_directories("${SUGAR_ROOT}/examples")

sugar_include("./sources")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/images")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/storyboards")

set(RESOURCES ${DEFAULT_IOS_IMAGES} ${IOS_STORYBOARDS_RESOURCES})

set(PLIST_FILE "${SUGAR_ROOT}/examples/plist/ios/storyboard.plist.in")
set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.ios.SingleViewApplication")

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

add_executable(example MACOSX_BUNDLE ${SOURCES} ${RESOURCES})
sugar_set_xcode_ios_sdkroot(TARGET example PLIST ${PLIST_FILE})

set_target_properties(
    example
    PROPERTIES
    XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY "1,2" # Universal (iPad + iPhone)
    RESOURCE "${RESOURCES}"
)
