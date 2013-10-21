# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_improper_number_of_arguments)
include(sugar_status_print)
include(sugar_test_target_exists)

function(sugar_target_add_definitions target)
  sugar_improper_number_of_arguments(${ARGC} 0)
  sugar_improper_number_of_arguments(${ARGC} 1)

  sugar_test_target_exists(${target})

  set(definitions ${ARGV})
  list(REMOVE_AT definitions 0) # remove 'target' variable

  set_property(
      TARGET
      ${target}
      APPEND
      PROPERTY
      COMPILE_DEFINITIONS
      ${definitions}
  )
endfunction()
