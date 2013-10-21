# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_improper_number_of_arguments)
include(sugar_test_target_exists)

function(sugar_target_add_linker_flags target)
  sugar_improper_number_of_arguments(${ARGC} 0)
  sugar_improper_number_of_arguments(${ARGC} 1)

  sugar_test_target_exists(${target})

  set(flags ${ARGV})
  list(REMOVE_AT flags 0) # remove 'target' variable

  set_property(
      TARGET
      ${target}
      APPEND_STRING
      PROPERTY
      LINK_FLAGS
      " ${flags}"
  )
endfunction()
