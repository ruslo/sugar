# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_expected_number_of_arguments)
include(sugar_test_target_exists)
include(sugar_target_add_linker_flags)

function(sugar_target_add_framework target framework)
  sugar_expected_number_of_arguments(${ARGC} 2)

  sugar_test_target_exists(${target})
  sugar_target_add_linker_flags(${target} "-framework ${framework}")
endfunction()
