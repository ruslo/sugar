# Examples
## Prepare
Every example expect that `SUGAR_ROOT` environment variable is set:
```bash
> git clone https://github.com/ruslo/sugar
> export SUGAR_ROOT="`pwd`/sugar"
> cd sugar/examples/NN-example/
> mkdir _builds
> (cd _builds/ && rm -rf * && cmake ..)
> make -C _builds/
```
Note that in general there is no need to set any environment variable, only include `Sugar` master file:
```cmake
include(/path/to/sugar/cmake/Sugar)
```

## Description
* 00 (detect): create empty project and include [Sugar](https://github.com/ruslo/sugar/blob/master/cmake/Sugar) master file, print updated variables
* 01 (simple): introduction to [collecting](https://github.com/ruslo/sugar/tree/master/cmake/collecting) system, used functions:
[sugar_include](https://github.com/ruslo/sugar/tree/master/cmake/collecting#sugar_include), [sugar_files](https://github.com/ruslo/sugar/tree/master/cmake/collecting#sugar_files)
* 02 (common): creating two targets with common sources, first fill sources variables, then create targets
* 03 (ios-gtest): wrapper for running gtest executable on iOS simulator, used functions:
[sugar_add_ios_gtest](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_add_ios_gtest)
* 04 (gtest-universal): if iOS build detected, use simulator to run gtest executable (see previous example), otherwise use
regular test system, used function:
[sugar_add_gtest](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_add_gtest)
* 05 (groups): generating groups for `Xcode` and `Visual Studio`, used function: [sugar_groups_generate](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_groups_generate)
* 06 (ios): building ios application (`Xcode`)
 * `empty_application` (like `Xcode`: `iOS` -> `Application` -> `Empty Application`)
 * `single_view_application` (like `Xcode`: `iOS` -> `Application` -> `Single View Application`)
 * `_universal_library` build/install universal library (i386 + arm, iphoneos + iphonesimulator)
 * `link_library` link universal library to ios target.
See [wiki](https://github.com/ruslo/sugar/wiki/Building-universal-ios-library) for detailed description.
 * `link_package` link universal library using `find_package` command
 * `link_library_with_executable` link universal library (inside one project), used function:
[sugar_target_link_libraries](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_target_link_libraries)
* 07 (cocoa): building macosx application (`Xcode`)
* 08 (doxygen): example of adding doxygen generation target,
used function: [sugar_doxygen_generate](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_doxygen_generate)
* *TODO*: more...

*Note*: mark `used functions` show only first appearance of function in examples
## Run all
`test.py` script can run all examples using different generators (`Make`, `Xcode`, ...)
and configurations (`Debug`, `Release`). See this [wiki](https://github.com/ruslo/sugar/wiki/Examples-testing)
