# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

if(DEFINED SOURCES_UNITTEST_SUGAR_CMAKE)
  return()
else()
  set(SOURCES_UNITTEST_SUGAR_CMAKE 1)
endif()

sugar_files(
    UNITTEST_SOURCES
    test.cpp
)
