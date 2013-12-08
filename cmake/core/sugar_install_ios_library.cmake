# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_expected_number_of_arguments)
include(sugar_fatal_error)
include(sugar_find_python3)
include(sugar_test_target_exists)
include(sugar_test_variable_not_empty)

function(sugar_install_ios_library library_target destination)
  sugar_expected_number_of_arguments(${ARGC} 2)

  if(NOT XCODE_VERSION)
    sugar_fatal_error("Only Xcode")
  endif()

  sugar_test_target_exists(${library_target})
  get_target_property(is_ios ${library_target} SUGAR_IOS)
  if(NOT is_ios)
    sugar_fatal_error(
        "Property SUGAR_IOS not found."
        "Please use sugar_add_ios_library to create library."
    )
  endif()

  get_target_property(path_debug ${library_target} SUGAR_IOS_PATH_DEBUG)
  get_target_property(path_release ${library_target} SUGAR_IOS_PATH_RELEASE)

  install(
      CODE
      "execute_process(
          COMMAND
          ${CMAKE_COMMAND}
          --build
          .
          --target
          ${library_target}
          --config
          Release
          WORKING_DIRECTORY
          ${PROJECT_BINARY_DIR}
      )"
  )

  install(
      CODE
      "execute_process(
          COMMAND
          ${CMAKE_COMMAND}
          --build
          .
          --target
          ${library_target}
          --config
          Debug
          WORKING_DIRECTORY
          ${PROJECT_BINARY_DIR}
      )"
  )

  install(
      FILES
      "${path_debug}"
      DESTINATION
      "${destination}"
      CONFIGURATIONS
      Debug
  )

  install(
      FILES
      "${path_release}"
      DESTINATION
      "${destination}"
      CONFIGURATIONS
      Release
  )
endfunction()
