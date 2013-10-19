Main directory of `cmake` modules.

### Manual add
Modules can be included manually:
```cmake
list(APPEND CMAKE_MODULE_PATH "${SUGAR_ROOT}/cmake/core")
```

### Master file 
Modules can be included automatically by master file [Sugar](https://github.com/ruslo/sugar/blob/master/cmake/Sugar):
```cmake
include($ENV{GITENV_ROOT}/sugar/cmake/Sugar)
```
in this case:
* all directories will be loaded (core, print, utility, ...)
* `GITENV_ROOT` and `SUGAR_ROOT` *cmake* variable will be setted
* [sugar_setup_libraries_paths](https://github.com/ruslo/sugar/blob/master/cmake/core/sugar_setup_libraries_paths.cmake)
will be called at end to define some `<LIBRARIES>_ROOT` variables.

### Priority
1. [SUGAR_ROOT](https://github.com/ruslo/sugar/wiki/Used-variables#sugar_root) setted as cmake variable
2. this file loaded as third party component (from release package), expected directory structure:
<pre>
= CMakeLists.txt # file with include(third_party/sugar/cmake/Sugar)
= third_party/  =
=               = sugar/ = 
=               =        = cmake/ =
=               =        =        = Sugar
</pre>
3. [GITENV_ROOT](https://github.com/ruslo/sugar/wiki/Used-variables#gitenv_root) setted as cmake variable
4. [GITENV_ROOT](https://github.com/ruslo/sugar/wiki/Used-variables#gitenv_root) setted as
environment variable, usual development.
(**Note**: This is used in all [examples](https://github.com/ruslo/sugar/tree/master/examples))
