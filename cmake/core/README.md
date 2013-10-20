# Core files
### sugar_add_this_to_source_list
Add file from which this function called to [SUGAR_SOURCES](https://github.com/ruslo/sugar/wiki/Used-variables#sugar_sources) list, which can be used later, for example,
for adding loaded `sugar_*.cmake` modules to project list files:
```cmake
add_executable(some_bin ${SOURCES} ${SUGAR_SOURCES})
```
Used by **all** files.

### sugar_setup_gitenv_paths
If [GITENV_ROOT](https://github.com/ruslo/sugar/wiki/Used-variables#gitenv_root) is detected (first try
cmake variable, then environment variable), modify some `<LIBRARIES>_ROOT` cmake variables.
