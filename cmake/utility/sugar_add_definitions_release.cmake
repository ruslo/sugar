# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_expected_number_of_arguments)

macro(sugar_add_definitions_release definition)
  sugar_expected_number_of_arguments(${ARGC} 1)
  set_property(
      DIRECTORY
      APPEND
      PROPERTY
      COMPILE_DEFINITIONS_RELEASE
      "${definition}"
  )
endmacro()
