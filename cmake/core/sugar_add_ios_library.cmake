# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_improper_number_of_arguments)
include(sugar_set_xcode_ios_sdkroot)

function(sugar_add_ios_library libname)
  sugar_improper_number_of_arguments(${ARGC} 0)
  sugar_improper_number_of_arguments(${ARGC} 1)

  set(libsources ${ARGV})
  list(REMOVE_AT libsources 0) # remove libname
  set(name_base ${libname}_BASE)

  set(name_release "${CMAKE_STATIC_LIBRARY_PREFIX}")
  set(name_release "${name_release}${libname}")
  set(name_release "${name_release}${CMAKE_STATIC_LIBRARY_SUFFIX}")

  set(name_debug "${CMAKE_STATIC_LIBRARY_PREFIX}")
  set(name_debug "${name_debug}${libname}${CMAKE_DEBUG_POSTFIX}")
  set(name_debug "${name_debug}${CMAKE_STATIC_LIBRARY_SUFFIX}")

  set(build_dir "iOS-universal")

  # Add real library
  add_library(${name_base} ${libsources})
  sugar_set_xcode_ios_sdkroot(TARGET ${name_base})
  # Build all listed architectures
  set_target_properties(
      ${name_base}
      PROPERTIES
      XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH
      "NO"
  )
  set_target_properties(${name_base} PROPERTIES DEBUG_POSTFIX "")
      # simplify search and rule creation

  # Add "fake" library
  get_target_property(location_base ${name_base} LOCATION_DEBUG)
  sugar_status_debug("LOCATION_DEBUG: ${location_base}")
  string(
      REGEX
      REPLACE
      ".*/DEBUG/"
      ""
      base_name
      "${location_base}"
  )
  string(
      REGEX
      REPLACE
      "/DEBUG/.*"
      ""
      base_dir
      "${location_base}"
  )
  sugar_status_debug("Base name: ${base_name}")
  sugar_status_debug("Base dir: ${base_dir}")
  set(xcode_command xcodebuild -target "${name_base}")
  set(
      bin_name
      "$<$<CONFIG:Release>:${name_release}>$<$<CONFIG:Debug>:${name_debug}>"
  )
  add_custom_target(
      ${libname}
      COMMAND
      ${CMAKE_COMMAND}
      -E
      make_directory
      ${PROJECT_BINARY_DIR}/$<CONFIGURATION>-${build_dir}
      COMMAND
      ${xcode_command} -configuration $<CONFIGURATION> -sdk iphoneos
      COMMAND
      ${xcode_command} -configuration $<CONFIGURATION> -sdk iphonesimulator
      COMMAND
      lipo
      -output
      ${PROJECT_BINARY_DIR}/$<CONFIGURATION>-${build_dir}/${bin_name}
      -create
      ${base_dir}/$<CONFIGURATION>-iphoneos/${base_name}
      ${base_dir}/$<CONFIGURATION>-iphonesimulator/${base_name}
      WORKING_DIRECTORY
      ${PROJECT_BINARY_DIR}
  )

  set_target_properties(
      ${libname}
      PROPERTIES
      SUGAR_IOS
      TRUE
      SUGAR_IOS_BASE_TARGET
      ${name_base}
      SUGAR_IOS_PATH_DEBUG
      ${PROJECT_BINARY_DIR}/Debug-${build_dir}/${name_debug}
      SUGAR_IOS_PATH_RELEASE
      ${PROJECT_BINARY_DIR}/Release-${build_dir}/${name_release}
  )
endfunction()
