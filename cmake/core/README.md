# Core files

### sugar_add_ios_gtest
Wrapper for running gtest executable on iOS simulator (i386). See [examples]
(https://github.com/ruslo/sugar/tree/master/examples#description) *ios-gtest* and *gtest-universal*.

### sugar_add_gtest
Use `sugar_add_ios_gtest` if iOS build detected, otherwise use `add_test`.

### sugar_add_this_to_source_list
Add file from which this function called to [SUGAR_SOURCES](https://github.com/ruslo/sugar/wiki/Used-variables#sugar_sources)
list. This variable can be used later, for example,
for adding loaded `sugar_*.cmake` modules to project list files:
```cmake
add_executable(some_bin ${SOURCES} ${SUGAR_SOURCES})
```
Used by **all** files.

### sugar_doxygen_generate
Add documentation target with `Doxyfile.in` for exe/lib target.
* target/directory properties `COMPILE_DEFINITIONS{_DEBUG,_RELEASE}*` used for making [PREDEFINED](http://www.stack.nl/~dimitri/doxygen/manual/config.html#cfg_predefined)
* target property [INCLUDE_DIRECTORIES](http://www.cmake.org/cmake/help/v2.8.11/cmake.html#prop_tgt:INCLUDE_DIRECTORIES) used for making [STRIP_FROM_PATH](http://www.stack.nl/~dimitri/doxygen/manual/config.html#cfg_strip_from_path)
* ...

#### Usage:
```cmake
add_executable(exe_target ${exe_target_sources})
sugar_doxygen_generate(TARGET exe_target DOXYTARGET doc DOXYFILE ${path_to_doxyfile_in})
```
Add specifier `DEVELOPER` for more verbose documentation, for example with enabled:
[INTERNAL_DOCS](http://www.stack.nl/~dimitri/doxygen/manual/config.html#cfg_internal_docs),
[CALL_GRAPH](http://www.stack.nl/~dimitri/doxygen/manual/config.html#cfg_call_graph),
[CALLER_GRAPH](http://www.stack.nl/~dimitri/doxygen/manual/config.html#cfg_caller_graph), ...:
```cmake
sugar_doxygen_generate(DEVELOPER TARGET exe_target DOXYTARGET internal-doc DOXYFILE ${path_to_doxyfile_in})
```

* [Example](https://github.com/ruslo/sugar/tree/master/examples#08-doxygen)

### sugar_groups_generate
Automatically generate [source groups](http://www.cmake.org/cmake/help/v2.8.11/cmake.html#command:source_group)
according to directory structure, for `Xcode` and `Visual Studio` IDE.
