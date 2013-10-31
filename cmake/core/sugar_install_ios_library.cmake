# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_execute_process)
include(sugar_expected_number_of_arguments)
include(sugar_fatal_error)
include(sugar_test_target_exists)
include(sugar_test_variable_not_empty)

function(sugar_install_ios_library library_target destination)
  sugar_expected_number_of_arguments(${ARGC} 2)

  if(NOT XCODE_VERSION)
    sugar_fatal_error("Only Xcode")
  endif()

  sugar_test_target_exists(${library_target})

  sugar_test_variable_not_empty(SUGAR_ROOT)

  find_package(PythonInterp 3.2 REQUIRED)

  set(cmd "")
  list(APPEND cmd ${PYTHON_EXECUTABLE})
  list(APPEND cmd ${SUGAR_ROOT}/python/sugar_install_ios_library.py)
  list(APPEND cmd --target)
  list(APPEND cmd ${library_target})
  list(APPEND cmd --destination)
  list(APPEND cmd ${CMAKE_INSTALL_PREFIX}/${destination})

  install(
      CODE
      "execute_process(
          COMMAND
          ${cmd} 
          WORKING_DIRECTORY
          ${PROJECT_BINARY_DIR}
      )"
  )
endfunction()
