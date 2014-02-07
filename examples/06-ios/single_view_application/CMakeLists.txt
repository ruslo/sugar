# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# iOS project example.
# Create project as Xcode: iOS -> Application -> Single View Application

cmake_minimum_required(VERSION 2.8.11)
project(06-example-ios.single_view_application CXX)

include("$ENV{SUGAR_ROOT}/cmake/Sugar")

include(sugar_include)

include_directories("${SUGAR_ROOT}/examples")

sugar_include("./sources")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/images")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/storyboards")

set(RESOURCES ${DEFAULT_IOS_IMAGES} ${IOS_STORYBOARDS_RESOURCES})

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

add_executable(example MACOSX_BUNDLE ${SOURCES} ${RESOURCES})

set_target_properties(
    example
    PROPERTIES
    MACOSX_BUNDLE YES
    MACOSX_BUNDLE_INFO_PLIST "${SUGAR_ROOT}/examples/plist/ios/storyboard.plist.in"
    MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.ios.SingleViewApplication"
    XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY "iPhone Developer"
    XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY "1,2" # Universal (iPad + iPhone)
    RESOURCE "${RESOURCES}"
)
