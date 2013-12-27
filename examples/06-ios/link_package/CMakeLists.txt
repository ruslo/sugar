# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Link universal library using 'find_package' command

cmake_minimum_required(VERSION 2.8.8)
project(06-example-ios.link_package CXX)

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_add_executable)
include(sugar_include)

sugar_include("./sources") # SOURCES

if(NOT XCODE_VERSION)
  sugar_fatal_error("Xcode only")
else()
  set(CMAKE_OSX_SYSROOT iphoneos)
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

include_directories(${UNIVERSAL_INCLUDE_DIRS})

# creating executable
sugar_add_executable(example ${SOURCES})
target_link_libraries(example ${UNIVERSAL_LIBS})
