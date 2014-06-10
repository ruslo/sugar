# Copyright (c) 2014, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(CMakeParseArguments) # cmake_parse_arguments
include(sugar_fatal_error)
include(sugar_generate_warning_flag_by_name)
include(sugar_status_debug)

# MS Visual Studio: http://msdn.microsoft.com/en-us/library/thxezb7y.aspx
# Clang: http://clang.llvm.org/docs/UsersManual.html
# GCC: https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html
function(sugar_generate_warning_flags)
  ### Detect compilers: is_clang, is_msvc, is_gcc
  string(COMPARE EQUAL "${CMAKE_CXX_COMPILER_ID}" "Clang" is_clang)
  string(COMPARE EQUAL "${CMAKE_CXX_COMPILER_ID}" "AppleClang" is_apple_clang)
  if(is_clang OR is_apple_clang)
    set(is_clang TRUE)
  else()
    set(is_clang FALSE)
  endif()
  set(is_msvc ${MSVC})
  set(is_gcc ${CMAKE_COMPILER_IS_GNUCXX})

  if(is_clang OR is_msvc OR is_gcc)
    # Supported compilers
  else()
    sugar_fatal_error("Compiler (${CMAKE_CXX_COMPILER_ID}) is not supported")
  endif()

  set(multi DISABLE ENABLE TREAT_AS_ERROR)
  set(opts CLEAR_GLOBAL)
  cmake_parse_arguments(x "${opts}" "" "${multi}" ${ARGV})

  ### Remove warning flags from global variable
  set(new_cmake_cxx_flags "${CMAKE_CXX_FLAGS}")
  string(REPLACE "/W3" "" new_cmake_cxx_flags "${new_cmake_cxx_flags}")
  string(COMPARE NOTEQUAL "${new_cmake_cxx_flags}" "${CMAKE_CXX_FLAGS}" x)

  if(x)
    if(x_CLEAR_GLOBAL)
      set(CMAKE_CXX_FLAGS "${new_cmake_cxx_flags}" PARENT_SCOPE)
    else()
      message(
          WARNING
          "CMAKE_CXX_FLAGS variable contains warning flag"
          " that may cause a conflict."
          " Consider using CLEAR_GLOBAL suboption to remove warning"
          " flags from CMAKE_CXX_FLAGS."
      )
    endif()
  endif()

  ### Length
  list(LENGTH x_UNPARSED_ARGUMENTS unparsed_length)
  list(LENGTH x_DISABLE disable_length)
  list(LENGTH x_ENABLE enable_length)
  list(LENGTH x_TREAT_AS_ERROR treat_as_error_length)

  ### Find special warning `ALL`
  list(FIND x_DISABLE "ALL" disable_all)
  list(FIND x_ENABLE "ALL" enable_all)
  list(FIND x_TREAT_AS_ERROR "ALL" treat_as_error_all)

  ### Convert to BOOL
  if(disable_all EQUAL -1)
    set(disable_all NO)
  else()
    set(disable_all YES)
  endif()

  if(enable_all EQUAL -1)
    set(enable_all NO)
  else()
    set(enable_all YES)
  endif()

  if(treat_as_error_all EQUAL -1)
    set(treat_as_error_all NO)
  else()
    set(treat_as_error_all YES)
  endif()

  ### If special option ALL present, check there is no others
  if(disable_all AND NOT disable_length EQUAL 1)
    sugar_fatal_error("If ALL present there must be no other warnings")
  endif()

  if(enable_all AND NOT enable_length EQUAL 1)
    sugar_fatal_error("If ALL present there must be no other warnings")
  endif()

  if(treat_as_error_all AND NOT treat_as_error_length EQUAL 1)
    sugar_fatal_error("If ALL present there must be no other warnings")
  endif()

  ### Verify result variable ###
  if(unparsed_length EQUAL 0)
    sugar_fatal_error("Expected result variable")
  endif()
  if(NOT unparsed_length EQUAL 1)
    sugar_fatal_error("Unparsed: ${x_UNPARSED_ARGUMENTS}")
  endif()
  set(result ${x_UNPARSED_ARGUMENTS})
  sugar_status_debug("Generate warnings for variable `${result}`")

  ### Disable all
  if(disable_all)
    if(is_msvc)
      list(APPEND ${result} "/w" "/W0")
    elseif(is_clang OR is_gcc)
      list(APPEND ${result} "-w")
    else()
      sugar_fatal_error("")
    endif()
  endif()

  ### Enable all
  if(enable_all)
    if(is_msvc)
      list(APPEND ${result} "/Wall")
    elseif(is_gcc)
      list(APPEND ${result} "-Wall" "-Wextra" "-Wpedantic")
    elseif(is_clang)
      list(APPEND ${result} "-Wall" "-Weverything" "-pedantic")
    else()
      sugar_fatal_error("")
    endif()
  endif()

  ### All treat as error
  if(treat_as_error_all)
    if(is_msvc)
      list(APPEND ${result} "/WX")
    elseif(is_gcc OR is_clang)
      list(APPEND ${result} "-Werror")
    else()
      sugar_fatal_error("")
    endif()
  endif()

  ### DISABLE and ENABLE must not intersects
  foreach(warning ${x_DISABLE})
    list(FIND x_ENABLE "${warning}" x)
    if(NOT x EQUAL -1)
      sugar_fatal_error(
          "Warning `${warning}` in both DISABLE and ENABLE sections"
      )
    endif()
  endforeach()

  ### DISABLE and TREAT_AS_ERROR must not intersects
  foreach(warning ${x_DISABLE})
    list(FIND x_TREAT_AS_ERROR "${warning}" x)
    if(NOT x EQUAL -1)
      sugar_fatal_error(
          "Warning `${warning}` in both DISABLE and TREAT_AS_ERROR sections"
      )
    endif()
  endforeach()

  ### Generate ENABLE
  foreach(warning ${x_ENABLE})
    sugar_generate_warning_flag_by_name(warning_flags ${warning})
    foreach(x ${warning_flags})
      if(is_msvc)
        list(APPEND ${result} "/w1${x}")
      elseif(is_gcc OR is_clang)
        list(APPEND ${result} "-W${x}")
      else()
        sugar_fatal_error("")
      endif()
    endforeach()
  endforeach()

  ### Generate DISABLE
  foreach(warning ${x_DISABLE})
    sugar_generate_warning_flag_by_name(warning_flags ${warning})
    foreach(x ${warning_flags})
      if(is_msvc)
        list(APPEND ${result} "/wd${x}")
      elseif(is_gcc OR is_clang)
        list(APPEND ${result} "-Wno-${x}")
      else()
        sugar_fatal_error("")
      endif()
    endforeach()
  endforeach()

  ### Generate TREAT_AS_ERROR
  foreach(warning ${x_TREAT_AS_ERROR})
    sugar_generate_warning_flag_by_name(warning_flags ${warning})
    foreach(x ${warning_flags})
      if(is_msvc)
        list(APPEND ${result} "/we${x}")
      elseif(is_gcc OR is_clang)
        list(APPEND ${result} "-Werror=${x}")
      else()
        sugar_fatal_error("")
      endif()
    endforeach()
  endforeach()

  sugar_status_debug("Generated from:")
  sugar_status_debug("  DISABLE: ${x_DISABLE}")
  sugar_status_debug("  ENABLE: ${x_ENABLE}")
  sugar_status_debug("  TREAT_AS_ERROR: ${x_TREAT_AS_ERROR}")
  sugar_status_debug("Generated: ${${result}}")

  set(${result} "${${result}}" PARENT_SCOPE)
endfunction()
