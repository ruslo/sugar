# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# iOS project example.
# Create project as Xcode: iOS -> Application -> Empty Application

cmake_minimum_required(VERSION 2.8.11)
project(06-example-ios.empty_application CXX)

### Emulate toolchain
set(CMAKE_OSX_SYSROOT iphoneos)
set(CMAKE_XCODE_EFFECTIVE_PLATFORMS "-iphoneos;-iphonesimulator")
set(CMAKE_DEBUG_POSTFIX d)
### -- end

include("$ENV{SUGAR_ROOT}/cmake/Sugar")

include(sugar_include)

include_directories("${SUGAR_ROOT}/examples")

sugar_include("./sources")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/images")

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

add_executable(example ${SOURCES} ${DEFAULT_IOS_IMAGES})

set_target_properties(
    example
    PROPERTIES
    MACOSX_BUNDLE YES
    MACOSX_BUNDLE_INFO_PLIST "${SUGAR_ROOT}/examples/plist/ios/empty.plist.in"
    MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.ios.EmptyApplication"
    XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY "iPhone Developer"
    RESOURCE "${DEFAULT_IOS_IMAGES}"
)
