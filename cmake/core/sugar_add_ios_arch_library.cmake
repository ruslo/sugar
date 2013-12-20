# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_improper_number_of_arguments)
include(sugar_set_xcode_ios_sdkroot)
include(sugar_test_variable_not_empty)

function(sugar_add_ios_arch_library libname)
  sugar_improper_number_of_arguments(${ARGC} 0)
  sugar_improper_number_of_arguments(${ARGC} 1)

  sugar_test_variable_not_empty(SUGAR_IOS_ARCH)

  set(libsources ${ARGV})
  list(REMOVE_AT libsources 0) # remove libname

  add_library(${libname} ${libsources})
  sugar_set_xcode_ios_sdkroot(TARGET ${libname})
  # Build only one architecture
  set_target_properties(
      ${libname}
      PROPERTIES
      XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH
      "YES"
  )
  # Specify archs
  set_target_properties(
      ${libname}
      PROPERTIES
      XCODE_ATTRIBUTE_ARCHS
      "${SUGAR_IOS_ARCH}"
  )
  set_target_properties(
      ${libname}
      PROPERTIES
      XCODE_ATTRIBUTE_VALID_ARCHS
      "${SUGAR_IOS_ARCH}"
  )
  set_target_properties(
      ${libname}
      PROPERTIES
      OSX_ARCHITECTURES
      "${SUGAR_IOS_ARCH}"
  )

  get_target_property(path_debug ${libname} LOCATION_DEBUG)
  get_target_property(path_release ${libname} LOCATION_RELEASE)

  string(COMPARE EQUAL "${SUGAR_IOS_ARCH}" "i386" is_i386_simulator)
  string(COMPARE EQUAL "${SUGAR_IOS_ARCH}" "x86_64" is_x64_simulator)

  if(is_i386_simulator OR is_x64_simulator)
    set(sdk "iphonesimulator")
  else()
    set(sdk "iphoneos")
  endif()

  string(
      REGEX
      REPLACE
      "/DEBUG/"
      "/Debug-${sdk}/"
      path_debug
      "${path_debug}"
  )

  string(
      REGEX
      REPLACE
      "/RELEASE/"
      "/Release-${sdk}/"
      path_release
      "${path_release}"
  )

  set_target_properties(
      ${libname}
      PROPERTIES
      SUGAR_IOS
      TRUE
      SUGAR_IOS_PATH_DEBUG
      "${path_debug}"
      SUGAR_IOS_PATH_RELEASE
      "${path_release}"
  )
endfunction()
