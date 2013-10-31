# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

if(DEFINED FIND_UNIVERSAL_LIB_CMAKE)
  return()
else()
  set(FIND_UNIVERSAL_LIB_CMAKE 1)
endif()

# Simple version of Find module.
# Usually more variables need to check (like REQUIRED)

include(sugar_test_variable_not_empty)
sugar_test_variable_not_empty(UNIVERSAL_ROOT)

set(UNIVERSAL_INCLUDE_DIRS "${UNIVERSAL_ROOT}/include")

find_library(
    UNIVERSAL_RELEASE
    NAMES
    universal_lib_example
    PATHS
    "${UNIVERSAL_ROOT}/lib/ios"
)

find_library(
    UNIVERSAL_DEBUG
    NAMES
    universal_lib_example-d
    PATHS
    "${UNIVERSAL_ROOT}/lib/ios"
)

if(NOT UNIVERSAL_RELEASE OR NOT UNIVERSAL_DEBUG)
  sugar_fatal_error("Universal library not found (install it!)")
endif()

set(UNIVERSAL_LIBS debug ${UNIVERSAL_DEBUG} optimized ${UNIVERSAL_RELEASE})
