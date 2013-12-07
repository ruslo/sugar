# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Example of using sugar_add_gtest command to run ios simulator if ios build
# detected or regular gtest run otherwise.
# If Xcode build detected force ios target.

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

include_directories("${GTEST_INCLUDE_DIRS}")

if(XCODE_VERSION)
  set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.example.sugar.ios.gtest")
  add_executable(simple_test MACOSX_BUNDLE simple_test.cpp)
  sugar_set_xcode_ios_sdkroot(TARGET simple_test)

  # `sugar_add_gtest` will check this variable and if "iphoneos" found
  # `sugar_add_ios_gtest` will be used
  set(CMAKE_OSX_SYSROOT iphoneos)
else()
  # not for iOS (expecting universal libraries...)
  find_package(Threads REQUIRED)
  add_executable(simple_test simple_test.cpp)
endif()
target_link_libraries(
    simple_test
    ${GTEST_BOTH_LIBRARIES}
    ${CMAKE_THREAD_LIBS_INIT}
)

enable_testing()
sugar_add_gtest(SimpleTestName simple_test)
