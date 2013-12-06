# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of using sugar_add_gtest command to run ios simulator if ios build
# detected or regular gtest run otherwise

cmake_minimum_required(VERSION 2.8.8)
project(04-example-gtest-universal)

include("$ENV{SUGAR_ROOT}/cmake/Sugar")
include(sugar_add_gtest)
include(sugar_set_xcode_ios_sdkroot)

# Install gtest using this project:
#     * 'https://github.com/hunter-packages/gtest'
# Note that it is just example, you don't need to install gtest manually
# if you're using "hunter" package manager (github.com/ruslo/hunter)
set(GTEST_ROOT "${CMAKE_CURRENT_LIST_DIR}/Install/")
find_package(GTest REQUIRED)

if(XCODE_VERSION)
  set(exe_bundle MACOSX_BUNDLE)
else()
  # not for iOS (expecting universal libraries...)
  find_package(Threads REQUIRED)
endif()

include_directories("${GTEST_INCLUDE_DIRS}")
add_executable(simple_test ${exe_bundle} simple_test.cpp)
target_link_libraries(
    simple_test
    ${GTEST_BOTH_LIBRARIES}
    ${CMAKE_THREAD_LIBS_INIT}
)

set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.ios.gtest")
set(PLIST_FILE "${SUGAR_ROOT}/examples/plist/ios/empty.plist.in")

if(XCODE_VERSION)
  sugar_set_xcode_ios_sdkroot(simple_test ${PLIST_FILE})
  set(CMAKE_OSX_SYSROOT iphoneos)
endif()

enable_testing()
sugar_add_gtest(SimpleTestName simple_test)
