# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_add_ios_executable)

function(sugar_add_executable execname)
  string(COMPARE EQUAL "${CMAKE_OSX_SYSROOT}" "iphoneos" is_ios)
  if(is_ios)
    sugar_add_ios_executable(${ARGV})
  else()
    add_executable(${ARGV})
  endif()
endfunction()
