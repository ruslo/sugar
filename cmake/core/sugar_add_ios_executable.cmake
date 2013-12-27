# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_improper_number_of_arguments)
include(sugar_set_xcode_ios_sdkroot)

function(sugar_add_ios_executable execname)
  sugar_improper_number_of_arguments(${ARGC} 0)
  sugar_improper_number_of_arguments(${ARGC} 1)

  set(sources ${ARGV})
  list(REMOVE_AT sources 0) # remove 'execname' variable

  add_executable(${execname} MACOSX_BUNDLE ${sources})
  sugar_set_xcode_ios_sdkroot(TARGET ${execname})
  if(NOT MACOSX_BUNDLE_GUI_IDENTIFIER)
    set_target_properties(
        ${execname}
        PROPERTIES
        MACOSX_BUNDLE_GUI_IDENTIFIER
        "com.example.fixme"
    )
  endif()
endfunction()
