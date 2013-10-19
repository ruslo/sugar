### sugar_files
Collect files in current directory to given variable.

### sugar_include
Load `sugar.cmake` file from given directory.

# Usage:

Used in `sugar.cmake` files. Example:
```cmake
# sugar.cmake is "include" file, so it need to be protected by header guards:
if(DEFINED SOURCES_SUGAR_CMAKE)
  return()
else()
  set(SOURCES_SUGAR_CMAKE 1)
endif()

include(sugar_files) # load 'sugar_files.cmake' with 'sugar_files' macro
include(sugar_include) # load 'sugar_include.cmake' with 'sugar_include' macro

sugar_include("./directory_1") # load ./directory_1/sugar.cmake
sugar_include("./directory_2") # load ./directory_2/sugar.cmake

# collect sources from current directory to 'SOURCES' variable
sugar_files(
    SOURCES
    main.cpp
    A.hpp
    B.hpp
    A.cpp
    B.cpp
)

```
