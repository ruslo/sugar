# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Doxygen documentation generation example.
#
# Just run `make *-doc` after cmake done.
#
# Commands:
#     http://www.stack.nl/~dimitri/doxygen/manual/commands.html

cmake_minimum_required(VERSION 2.8.8)
project(08-example-doxygen CXX)

include($ENV{SUGAR_ROOT}/cmake/Sugar)

include(sugar_add_definitions_debug)
include(sugar_add_definitions_release)
include(sugar_doxygen_generate)
include(sugar_include)
include(sugar_target_add_definitions)

include_directories("./sources")

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release) # set default build type
endif()

sugar_include("./sources")

add_executable(prog ${SOURCES})

# macro expansion can be checked in attributes of class C
add_definitions(-DA_DIRECTORY_MACRO=1)
sugar_target_add_definitions(prog "A_TARGET_MACRO=1")
sugar_add_definitions_debug("A_DEBUG=1")
sugar_add_definitions_release("A_NDEBUG=1")

sugar_doxygen_generate(
    DEVELOPER
    TARGET
    prog
    DOXYTARGET
    internal-doc
    DOXYFILE
    ${SUGAR_ROOT}/examples/Doxyfile.in
)

sugar_doxygen_generate(
    TARGET
    prog
    DOXYTARGET
    public-doc
    DOXYFILE
    ${SUGAR_ROOT}/examples/Doxyfile.in
)
