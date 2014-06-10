# Copyright (c) 2014, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_expected_number_of_arguments)
include(sugar_fatal_error)
include(sugar_status_debug)

### https://github.com/ruslo/leathers/wiki/List
function(sugar_generate_warning_flag_by_name warning_flags warning_name)
  sugar_expected_number_of_arguments(${ARGC} 2)

  sugar_status_debug("Flags by name: ${warning_name}")

  ### Check preconditions
  if(is_clang OR is_msvc OR is_gcc)
    # Supported compilers
  else()
    sugar_fatal_error("")
  endif()

  string(COMPARE EQUAL "ALL" "${warning_name}" is_all)
  if(is_all)
    # Skip this (already processed)
    set(${warning_flags} "" PARENT_SCOPE)
    return()
  endif()

  set(result "")

  ### cast_align
  string(COMPARE EQUAL "cast_align" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "cast-align")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### conversion
  string(COMPARE EQUAL "conversion" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "cast-align")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### deprecated
  string(COMPARE EQUAL "deprecated" "${warning_name}" hit)
  if(hit)
    if(is_msvc)
      list(APPEND result "4996")
    endif()
    if(is_clang OR is_gcc)
      list(APPEND result "deprecated-register")
      list(APPEND result "deprecated")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### direct_ivar_access
  string(COMPARE EQUAL "direct_ivar_access" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "direct-ivar-access")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### disabled_macro_expansion
  string(COMPARE EQUAL "disabled_macro_expansion" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "disabled-macro-expansion")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### enum_not_handled_in_switch
  string(COMPARE EQUAL "enum_not_handled_in_switch" "${warning_name}" hit)
  if(hit)
    if(is_msvc)
      list(APPEND result "4061")
      list(APPEND result "4062")
    endif()
    if(is_clang OR is_gcc)
      list(APPEND result "switch")
      list(APPEND result "switch-enum")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### exit_time_destructors
  string(COMPARE EQUAL "exit_time_destructors" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "exit-time-destructors")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### explicit_ownership_type
  string(COMPARE EQUAL "explicit_ownership_type" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "explicit-ownership-type")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### extended_offsetof
  string(COMPARE EQUAL "extended_offsetof" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "extended-offsetof")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### format_nonliteral
  string(COMPARE EQUAL "format_nonliteral" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "format-nonliteral")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### global_constructors
  string(COMPARE EQUAL "global_constructors" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "global-constructors")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### gnu
  string(COMPARE EQUAL "gnu" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "gnu")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### implicit_fallthrough
  string(COMPARE EQUAL "implicit_fallthrough" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "implicit-fallthrough")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### missing_prototypes
  string(COMPARE EQUAL "missing_prototypes" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "missing-prototypes")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### missing_variable_declarations
  string(COMPARE EQUAL "missing_variable_declarations" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "missing-variable-declarations")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### over_aligned
  string(COMPARE EQUAL "over_aligned" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "over-aligned")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### padded
  string(COMPARE EQUAL "padded" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "padded")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### pedantic
  string(COMPARE EQUAL "pedantic" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "pedantic")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### selector
  string(COMPARE EQUAL "selector" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "selector")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### sign_conversion
  string(COMPARE EQUAL "sign_conversion" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "sign-conversion")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### unreachable_code
  string(COMPARE EQUAL "unreachable_code" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "unreachable-code")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### unused_function
  string(COMPARE EQUAL "unused_function" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "unused-function")
      list(APPEND result "unused-member-function")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### unused_macros
  string(COMPARE EQUAL "unused_macros" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "unused-macros")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### unused_parameter
  string(COMPARE EQUAL "unused_parameter" "${warning_name}" hit)
  if(hit)
    if(is_msvc)
      list(APPEND result "4100")
    endif()
    if(is_clang OR is_gcc)
      list(APPEND result "unused-parameter")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### unused_variable
  string(COMPARE EQUAL "unused_variable" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "unused-variable")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### used_but_marked_unused
  string(COMPARE EQUAL "used_but_marked_unused" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "used-but-marked-unused")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### weak_template_vtables
  string(COMPARE EQUAL "weak_template_vtables" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "weak-template-vtables")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  ### weak_vtables
  string(COMPARE EQUAL "weak_vtables" "${warning_name}" hit)
  if(hit)
    if(is_clang OR is_gcc)
      list(APPEND result "weak-vtables")
    endif()

    set(${warning_flags} "${result}" PARENT_SCOPE)
    return()
  endif()

  message("Unknown warning name: ${warning_name}")
  message("List of known warnings: https://github.com/ruslo/leathers/wiki/List")
  sugar_fatal_error("")
endfunction()
