Extension of cmake functionality which is not related to [sugar](https://github.com/ruslo/sugar) library itself

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

### sugar_test_variable_not_empty
Some kind of assert. Useful in cases when you expect that variable is definitely not empty:
```cmake
sugar_test_variable_not_empty(BOOST_ROOT)
include("${BOOST_ROOT}/boost/config.hpp")
```
