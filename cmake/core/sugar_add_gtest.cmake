# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(CMakeParseArguments) # cmake_parse_arguments

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_add_ios_gtest)
include(sugar_add_android_gtest)
include(sugar_status_debug)

if(HUNTER_ENABLED)
  string(COMPARE EQUAL "${CMAKE_OSX_SYSROOT}" "iphoneos" is_ios)
  if(is_ios)
    hunter_add_package(ios_sim)
  endif()
endif()

function(sugar_add_gtest)
  string(COMPARE EQUAL "${CMAKE_OSX_SYSROOT}" "iphoneos" is_ios)
  if(is_ios)
    sugar_status_debug("Use sugar_add_ios_gtest")
    sugar_status_debug("ARGV: [${ARGV}]")
    cmake_parse_arguments(x "" "NAME" "COMMAND" ${ARGV})
    sugar_add_ios_gtest(${x_NAME} ${x_COMMAND})
  elseif(ANDROID)
    sugar_status_debug("Use android_add_test")
    sugar_status_debug("ARGV: [${ARGV}]")
    sugar_add_android_gtest(${ARGV})
  else()
    sugar_status_debug("Use cmake add_test")
    sugar_status_debug("ARGV: [${ARGV}]")
    add_test(${ARGV})
  endif()
endfunction()
