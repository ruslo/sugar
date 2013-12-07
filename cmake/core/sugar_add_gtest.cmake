# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_add_ios_gtest)
include(sugar_status_debug)

function(sugar_add_gtest)
  set(iphoneos_found FALSE)
  foreach(x ${CMAKE_OSX_SYSROOT})
    string(FIND "${x}" "iphoneos" result)
    if(NOT ${result} EQUAL "-1")
      set(iphoneos_found TRUE)
    endif()
  endforeach()

  if(iphoneos_found)
    sugar_status_debug("Use sugar_add_ios_gtest")
    sugar_status_debug("ARGV: [${ARGV}]")
    sugar_add_ios_gtest(${ARGV})
  else()
    sugar_status_debug("Use cmake add_test")
    add_test(${ARGV})
  endif()
endfunction()
