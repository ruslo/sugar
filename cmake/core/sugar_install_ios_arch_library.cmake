# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_expected_number_of_arguments)
include(sugar_fatal_error)
include(sugar_test_target_exists)
include(sugar_test_variable_not_empty)

function(sugar_install_ios_arch_library library_target destination)
  sugar_expected_number_of_arguments(${ARGC} 2)

  if(NOT XCODE_VERSION)
    sugar_fatal_error("Only Xcode")
  endif()

  sugar_test_variable_not_empty(SUGAR_IOS_ARCH)

  sugar_test_target_exists(${library_target})

  get_target_property(is_ios ${library_target} SUGAR_IOS)
  if(NOT is_ios)
    sugar_fatal_error(
        "Property SUGAR_IOS not found."
        "Please use sugar_add_ios_library/sugar_add_library to create library."
    )
  endif()

  get_target_property(path_debug ${library_target} SUGAR_IOS_PATH_DEBUG)
  get_target_property(path_release ${library_target} SUGAR_IOS_PATH_RELEASE)

  string(COMPARE EQUAL "${SUGAR_IOS_ARCH}" "i386" is_i386_simulator)
  string(COMPARE EQUAL "${SUGAR_IOS_ARCH}" "x86_64" is_x64_simulator)

  if(is_i386_simulator OR is_x64_simulator)
    set(sdk "iphonesimulator")
  else()
    set(sdk "iphoneos")
  endif()

  install(
      CODE
      "execute_process(
          COMMAND
          xcodebuild
          -target
          ${library_target}
          -configuration
          Release
          -sdk
          ${sdk}
          WORKING_DIRECTORY
          ${PROJECT_BINARY_DIR}
      )"
  )

  install(
      CODE
      "execute_process(
          COMMAND
          xcodebuild
          -target
          ${library_target}
          -configuration
          Debug
          -sdk
          ${sdk}
          WORKING_DIRECTORY
          ${PROJECT_BINARY_DIR}
      )"
  )

  install(
      FILES
      "${path_debug}"
      DESTINATION
      "${destination}"
  )

  install(
      FILES
      "${path_release}"
      DESTINATION
      "${destination}"
  )
endfunction()
