# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_fatal_error)

# By default number of arguments passed to a function not controlled.
# i.e. |function(my_function A B)| can be called with 3 arguments.
# This function help to check this.
#
# Example:
#     function(my_function A B)
#       sugar_expected_number_of_arguments(${ARGC} 2)
#       # ...
#     endfunction()
#
#     my_function(1 2) # OK
#     my_function(1 2 3) # ERROR
function(sugar_expected_number_of_arguments given expected)
  # Do some self check.
  if(NOT ${ARGC} EQUAL 2)
    sugar_fatal_error(
        "Incorrect usage of 'sugar_expected_number_of_arguments', "
        "expected '2' arguments but given '${ARGC}'."
    )
  endif()

  if(NOT ${given} EQUAL ${expected})
    sugar_fatal_error(
        FATAL_ERROR
        "Incorrect number of arguments '${given}', expected '${expected}'."
    )
  endif()
endfunction()
