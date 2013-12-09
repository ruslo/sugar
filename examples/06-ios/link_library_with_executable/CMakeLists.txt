# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Link library and executable in one project

cmake_minimum_required(VERSION 2.8.8)
project(06-example-ios.link_library_with_executable CXX)

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_add_ios_library)
include(sugar_set_xcode_ios_sdkroot)
include(sugar_target_link_libraries)

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.LinkLibraryWithExecutable")

set(CMAKE_DEBUG_POSTFIX d)
set(CMAKE_OSX_SYSROOT "iphoneos")

sugar_add_ios_library(foo foo.cpp)

add_executable(boo MACOSX_BUNDLE boo.cpp)
sugar_target_link_libraries(boo foo)
sugar_set_xcode_ios_sdkroot(TARGET boo)
