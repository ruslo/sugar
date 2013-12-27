# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(CMakeParseArguments) # CMAKE_PARSE_ARGUMENTS

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_fatal_error)
include(sugar_install_ios_library)
include(sugar_status_debug)
include(sugar_test_target_exists)

function(sugar_install_library)
  string(COMPARE EQUAL "${CMAKE_OSX_SYSROOT}" "iphoneos" is_ios)
  if(NOT is_ios)
    # If target is not iOS use regular cmake install
    sugar_status_debug("Use cmake install: ${ARGV}")
    install(${ARGV})
    return()
  endif()

  sugar_status_debug("Use ios-workaround install: ${ARGV}")

  CMAKE_PARSE_ARGUMENTS(
      lib_install "" "DESTINATION" "TARGETS" ${ARGV}
  )

  if(lib_install_UNPARSED_ARGUMENTS)
    sugar_fatal_error("Unparsed: ${lib_install_UNPARSED_ARGUMENTS}")
  endif()

  if(NOT lib_install_TARGETS)
    sugar_fatal_error("TARGETS is mandatory parameter")
  endif()

  if(NOT lib_install_DESTINATION)
    sugar_fatal_error("DESTINATION is mandatory parameter")
  endif()

  foreach(lib ${lib_install_TARGETS})
    sugar_test_target_exists(${lib})
    sugar_install_ios_library(${lib} ${lib_install_DESTINATION})
  endforeach()
endfunction()
