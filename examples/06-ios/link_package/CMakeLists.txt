# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Link universal library using 'find_package' command

cmake_minimum_required(VERSION 2.8.8)
project(06-example-ios.link_package CXX)

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_include)
include(sugar_mark_macosx_resources)
include(sugar_set_xcode_ios_sdkroot)

sugar_include("./sources")
sugar_include("${SUGAR_ROOT}/examples/resources/ios/images")

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
endif()

# add path for searching *.cmake file
list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")
set(
    UNIVERSAL_ROOT
    "${SUGAR_ROOT}/examples/06-ios/_universal_library/install"
)

# 1. include module 'FindUniversalLib.cmake' from CMAKE_MODULE_PATH
# 2. use UNIVERSAL_ROOT to search libraries
# 3. set result variables: UNIVERSAL_INCLUDE_DIRS, UNIVERSAL_LIBS
find_package(UniversalLib)

set(PLIST_FILE "${SUGAR_ROOT}/examples/plist/ios/empty.plist.in")
set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.ios.LinkLibrary")

sugar_mark_macosx_resources(${DEFAULT_IOS_IMAGES})

include_directories(${UNIVERSAL_INCLUDE_DIRS})

# creating executable
add_executable(example MACOSX_BUNDLE ${SOURCES} ${DEFAULT_IOS_IMAGES})
sugar_set_xcode_ios_sdkroot(example ${PLIST_FILE})
target_link_libraries(example ${UNIVERSAL_LIBS})
