#!/usr/bin/env python3

# Copyright (c) 2014, Ruslan Baratov
# All rights reserved.

file_header = """# This file generated automatically:
# https://github.com/ruslo/sugar/wiki/Cross-platform-warning-suppression

# Copyright (c) 2014, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_expected_number_of_arguments)
include(sugar_fatal_error)
include(sugar_status_debug)

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

"""

file_footer = """  message("Unknown warning name: ${warning_name}")
  message("List of known warnings: https://github.com/ruslo/leathers/wiki/List")
  sugar_fatal_error("")
endfunction()
"""

def generate(main_warnings_table):
  cmake_file = open("sugar_generate_warning_flag_by_name.cmake", "w")
  cmake_file.write(file_header)
  for entry in main_warnings_table:
    name = entry.warning_name
    cmake_file.write("  ### {}\n".format(name))
    cmake_file.write(
        """  string(COMPARE EQUAL "{}" "${}" hit)\n""".format(
            name, "{warning_name}"
        )
    )
    cmake_file.write("  if(hit)\n")

    if entry.clang.valid():
      text = entry.clang.cxx_entry(name)
      cmake_file.write("    if(is_clang)\n")
      cmake_file.write("      list(APPEND result \"{}\")\n".format(text))
      cmake_file.write("    endif()\n")

    if entry.gcc.valid():
      text = entry.gcc.cxx_entry(name)
      cmake_file.write("    if(is_gcc)\n")
      cmake_file.write("      list(APPEND result \"{}\")\n".format(text))
      cmake_file.write("    endif()\n")

    if entry.msvc.valid():
      text = entry.msvc.cxx_entry(name)
      cmake_file.write("    if(is_msvc)\n")
      cmake_file.write("      list(APPEND result \"{}\")\n".format(text))
      cmake_file.write("    endif()\n")

    """footer"""
    cmake_file.write("    set(${warning_flags} \"${result}\" PARENT_SCOPE)\n")
    cmake_file.write("    return()\n")
    cmake_file.write("  endif()\n\n")
  cmake_file.write(file_footer)
