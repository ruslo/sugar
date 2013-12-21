# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_improper_number_of_arguments)
include(sugar_status_debug)
include(sugar_test_target_exists)
include(sugar_test_variable_not_empty)

function(sugar_target_link_libraries target)
  sugar_improper_number_of_arguments(${ARGC} 0)
  sugar_improper_number_of_arguments(${ARGC} 1)

  set(libraries ${ARGV})
  list(REMOVE_AT libraries 0) # remove `target`
  sugar_test_target_exists(${target})

  sugar_status_debug("link libraries: ${libraries}")
  sugar_status_debug("to target: ${target}")

  get_target_property(sugar_ios ${target} SUGAR_IOS)
  if(sugar_ios)
    get_target_property(real_target ${target} SUGAR_IOS_BASE_TARGET)
    if(NOT real_target)
      # optimized variant
      set(real_target ${target})
    endif()
  else()
    set(real_target ${target})
  endif()

  list(GET libraries 0 x)
  list(REMOVE_AT libraries 0)
  string(COMPARE EQUAL "${x}" "debug" lib_debug)
  string(COMPARE EQUAL "${x}" "optimized" lib_optimized)

  if(lib_debug)
    list(GET libraries 0 x)
    list(REMOVE_AT libraries 0)
    target_link_libraries(${real_target} debug "${x}")
    if(libraries)
      sugar_target_link_libraries(${real_target} ${libraries})
    endif()
    return()
  endif()

  if(lib_optimized)
    list(GET libraries 0 x)
    list(REMOVE_AT libraries 0)
    target_link_libraries(${real_target} optimized "${x}")
    if(libraries)
      sugar_target_link_libraries(${real_target} ${libraries})
    endif()
    return()
  endif()

  # `x` is a library
  if(NOT TARGET ${x})
    target_link_libraries(${real_target} ${x})
    if(libraries)
      sugar_target_link_libraries(${real_target} ${libraries})
    endif()
    return()
  endif()

  # `x` is a target
  get_target_property(sugar_ios ${x} SUGAR_IOS)
  if(sugar_ios)
    get_target_property(base_target ${x} SUGAR_IOS_BASE_TARGET)
    if(NOT base_target)
      # optimized variant
      set(base_target ${x})
    endif()
    get_target_property(link_dep_libs ${base_target} LINK_LIBRARIES)
    if(NOT link_dep_libs)
      unset(link_dep_libs) # remove NOTFOUND if empty
    endif()
    add_dependencies(${target} ${x})
    get_target_property(path_debug ${x} SUGAR_IOS_PATH_DEBUG)
    get_target_property(path_release ${x} SUGAR_IOS_PATH_RELEASE)
    set(
        real_link
        debug
        ${path_debug}
        optimized
        ${path_release}
        ${link_dep_libs}
    )
  else()
    set(real_link ${x})
  endif()
  target_link_libraries(${real_target} ${real_link})
  if(libraries)
    sugar_target_link_libraries(${real_target} ${libraries})
  endif()
endfunction()
