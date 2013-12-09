# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_improper_number_of_arguments)
include(sugar_test_target_exists)
include(sugar_test_variable_not_empty)

function(sugar_target_link_libraries target)
  sugar_improper_number_of_arguments(${ARGC} 0)
  sugar_improper_number_of_arguments(${ARGC} 1)

  set(libraries ${ARGV})
  list(REMOVE_AT libraries 0) # remote `target`
  sugar_test_target_exists(${target})

  foreach(x ${libraries})
    if(TARGET ${x})
      get_target_property(sugar_ios ${x} SUGAR_IOS)
      if(sugar_ios)
        get_target_property(path_debug ${x} SUGAR_IOS_PATH_DEBUG)
        get_target_property(path_release ${x} SUGAR_IOS_PATH_RELEASE)
        target_link_libraries(${target} debug ${path_debug})
        target_link_libraries(${target} optimized ${path_release})
        add_dependencies(${target} ${x})
      else()
        target_link_libraries(${target} ${x})
      endif()
    else()
      target_link_libraries(${target} ${x})
    endif()
  endforeach()
endfunction()
