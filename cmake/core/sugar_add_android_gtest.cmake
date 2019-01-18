# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(CMakeParseArguments) # cmake_parse_arguments

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

set(ANDROID_THIS_DIRECTORY "${CMAKE_CURRENT_LIST_DIR}")

function(sugar_add_android_gtest)
  set(ADB_COMMAND "adb")

  set(oneValueArgs NAME RESOURCE_DIR TESTDATA_DIR APP_DEPENDENCY)
  set(multiValueArgs COMMAND)
  cmake_parse_arguments(x "" "${oneValueArgs}" "${multiValueArgs}" ${ARGV})
  string(COMPARE NOTEQUAL "${x_UNPARSED_ARGUMENTS}" "" has_unparsed)
  if(has_unparsed)
    message(FATAL_ERROR "Unparsed: ${x_UNPARSED_ARGUMENTS}")
  endif()

  list(GET x_COMMAND 0 app_target)
  if(NOT TARGET "${app_target}")
    message(FATAL_ERROR "Expected executable target as first argument, but got: ${app_target}")
  endif()

  set(script_loc "${CMAKE_CURRENT_BINARY_DIR}/_3rdParty/AndroidTest/${x_NAME}.cmake")

  list(REMOVE_AT x_COMMAND 0)
  set(APP_ARGUMENTS ${x_COMMAND})

  set(ANDROID_APK_APP_DESTINATION "/data/local/tmp/AndroidApk")
  set(APP_DESTINATION "${ANDROID_APK_APP_DESTINATION}")
  set(APP_DESTINATION "${APP_DESTINATION}/${PROJECT_NAME}/AndroidTest")
  set(APP_DESTINATION "${APP_DESTINATION}/${x_NAME}/${app_target}")

  set(APP_RESOURCES "${x_RESOURCE_DIR}")
  set(APP_TEST_DATA "${x_TESTDATA_DIR}")
  set(APP_DEPENDENCY "${x_APP_DEPENDENCY}")

  # Use:
  # * ADB_COMMAND
  # * APP_ARGUMENTS
  # * APP_DESTINATION
  # * APP_RESOURCES
  # * APP_TEST_DATA
  configure_file(
      "${ANDROID_THIS_DIRECTORY}/templates/AndroidTest.cmake.in"
      "${script_loc}"
      @ONLY
  )

  add_test(
      NAME "${x_NAME}"
      COMMAND
          "${CMAKE_COMMAND}"
          "-DAPP_SOURCE=$<TARGET_FILE:${app_target}>"
          -P
          "${script_loc}"
  )
endfunction()
