Extension of cmake functionality which is not related to [sugar](https://github.com/ruslo/sugar) library itself

### sugar_add_definitions_debug
Wrapper for `COMPILE_DEFINITIONS_DEBUG` directory property update

### sugar_add_definitions_release
Wrapper for `COMPILE_DEFINITIONS_RELEASE` directory property update

### sugar_check_no_duplicates
Verify that given list not holding duplicate values

### sugar_echo_target
Print all target [properties](http://www.kitware.com/blog/home/post/390)

### sugar_execute_process
Wrapper for [execute_process](http://www.cmake.org/cmake/help/v2.8.11/cmake.html#command:execute_process) command
with verbose error message if run failed.

### sugar_expected_number_of_arguments
By default number of arguments passed to a function not controlled, i.e. `function(my_function A B)` can be
called with 3 arguments. This function help to check this. Example:
```cmake
# Declaration
function(my_function A B)
  sugar_expected_number_of_arguments(${ARGC} 2)
  # ...
endfunction()
```
```cmake
# Usage
my_function(1 2) # OK
my_function(1 2 3) # ERROR
```

### sugar_improper_number_of_arguments
Same as `sugar_expected_number_of_arguments` but check that number is **not** equal to value:
```cmake
function(my_function A B)
  sugar_improper_number_of_arguments(${ARGC} 0)
  sugar_improper_number_of_arguments(${ARGC} 1)
  sugar_improper_number_of_arguments(${ARGC} 2)

  # expected number of arguments > 2
endfunction()
```

### sugar_mark_macosx_resources
Wrapper for setting [MACOSX_PACKAGE_LOCATION](http://www.cmake.org/cmake/help/v2.8.11/cmake.html#prop_sf:MACOSX_PACKAGE_LOCATION)
property

### sugar_set_xcode_ios_sdkroot
* set `Xcode` sdkroot to `iphoneos`
* set `Xcode` sign identity to `iPhone Developer`
* set `Xcode` property `XCODE_ATTRIBUTE_ARCHS` to `$(ARCHS_STANDARD_INCLUDING_64_BIT)`
* if suboption `PLIST` present set target property [MACOSX_BUNDLE_INFO_PLIST](http://www.cmake.org/cmake/help/v2.8.11/cmake.html#prop_tgt:MACOSX_BUNDLE_INFO_PLIST)
* link default frameworks: `CoreGraphics`, `Foundation`, `UIKit`

### sugar_target_add_definitions
Wrapper for updating `COMPILE_DEFINITIONS` target property

### sugar_target_add_framework
Wrapper for adding `-framework ...` to linker flags

### sugar_target_add_linker_flags
Wrapper for setting [LINK_FLAGS](http://www.cmake.org/cmake/help/v2.8.11/cmake.html#prop_tgt:LINK_FLAGS)
target property

### sugar_test_directory_exists
Test directory exists. Get absolute dir path (if path is relative, it may not work), check exist and check
is a directory.

### sugar_test_file_exists
Test file exists. Get absolute file path (if path is relative, it may not work), check exist and check
is not directory.

### sugar_test_target_exists
Wrapper for `if(NOT TARGET ...) message(FATAL_ERROR ...)`

### sugar_test_variable_not_empty
Some kind of assert. Useful in cases when you expect that variable is definitely not empty:
```cmake
sugar_test_variable_not_empty(SOME_LIBRARY_ROOT)
include_directories("${SOME_LIBRARY_ROOT}/some/library/include")
```
