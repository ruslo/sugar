# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_expected_number_of_arguments)
include(sugar_test_variable_not_empty)

macro(sugar_setup_libraries_paths)
  sugar_expected_number_of_arguments(${ARGC} 0)
  if(DEFINED GITENV_ROOT)
    sugar_test_variable_not_empty(GITENV_ROOT)

    set(Boost_NO_SYSTEM_PATH TRUE) # disable searching in system dirs
    set(BOOST_ROOT "${GITENV_ROOT}/boost/install")

    set(GMOCK_ROOT "${GITENV_ROOT}/google/gmock")
    set(GTEST_ROOT "${GITENV_ROOT}/google/gtest")
    set(BREAKPAD_ROOT "${GITENV_ROOT}/google/breakpad")
    set(SAFE_NUMERICS_ROOT "${GITENV_ROOT}/safe_numerics")
    set(SOBER_ROOT "${GITENV_ROOT}/ruslo/sober")
  endif()
endmacro()
