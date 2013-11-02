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
  set(one_value_args TARGETS DESTINATION)
  CMAKE_PARSE_ARGUMENTS(
      lib_install "" "${one_value_args}" "" ${ARGV}
  )

  if(lib_install_UNPARSED_ARGUMENTS)
    sugar_fatal_error("Unparsed: ${lib_install_UNPARSED_ARGUMENTS}")
  endif()

  if(NOT lib_install_TARGETS)
    sugar_fatal_error("TARGETS is mandatory parameter")
  else()
    sugar_test_target_exists(${lib_install_TARGETS})
  endif()

  if(NOT lib_install_DESTINATION)
    sugar_fatal_error("DESTINATION is mandatory parameter")
  endif()

  set(iphoneos_found FALSE)
  foreach(x ${CMAKE_OSX_SYSROOT})
    string(FIND "${x}" "iphoneos" result)
    if(NOT ${result} EQUAL "-1")
      set(iphoneos_found TRUE)
    endif()
  endforeach()

  # If target is not iOS use regular cmake install
  if(NOT iphoneos_found)
    sugar_status_debug("Use cmake install: ${lib_install_TARGETS}")
    install(
        TARGETS ${lib_install_TARGETS} DESTINATION ${lib_install_DESTINATION}
    )
    return()
  endif()

  sugar_status_debug("Use ios-workaround install: ${lib_install_TARGETS}")
  sugar_install_ios_library(${lib_install_TARGETS} ${lib_install_DESTINATION})
endfunction()
