Extension of cmake functionality which is not related to [sugar](https://github.com/ruslo/sugar) library itself

### sugar_check_no_duplicates
Verify that given list not holding duplicate values

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

### sugar_test_file_exists
Test file exists. Get absolute file path (if path is relative, it may not work), check exist and check
is not directory.

### sugar_test_variable_not_empty
Some kind of assert. Useful in cases when you expect that variable is definitely not empty:
```cmake
sugar_test_variable_not_empty(BOOST_ROOT)
include("${BOOST_ROOT}/boost/config.hpp")
```
