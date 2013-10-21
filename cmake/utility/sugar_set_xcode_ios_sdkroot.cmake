# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_expected_number_of_arguments)
include(sugar_status_print)
include(sugar_target_add_framework)
include(sugar_test_file_exists)

function(sugar_set_xcode_ios_sdkroot target plist)
  sugar_expected_number_of_arguments(${ARGC} 2)

  set_target_properties(
      ${target}
      PROPERTIES
      XCODE_ATTRIBUTE_SDKROOT
      "iphoneos"
  )

  set_target_properties(
      ${target}
      PROPERTIES
      XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY
      "iPhone Developer"
  )

  sugar_status_print("Info.plist source: ${plist}")
  sugar_test_file_exists("${plist}")
  set_target_properties(
      ${target}
      PROPERTIES
      MACOSX_BUNDLE_INFO_PLIST
      "${plist}"
  )

  # add default frameworks
  sugar_target_add_framework(${target} CoreGraphics)
  sugar_target_add_framework(${target} Foundation)
  sugar_target_add_framework(${target} UIKit)
endfunction()
