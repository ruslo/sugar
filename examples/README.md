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
* 05 (groups): generating groups for `Xcode` and `Visual Studio`, used function: [sugar_groups_generate](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_groups_generate)
* 06 (ios): building ios application (`Xcode`)
 * `empty_application` (like `Xcode`: `iOS` -> `Application` -> `Empty Application`), used function:
[sugar_mark_macosx_resources](https://github.com/ruslo/sugar/tree/master/cmake/utility#sugar_mark_macosx_resources),
[sugar_set_xcode_ios_sdkroot](https://github.com/ruslo/sugar/tree/master/cmake/utility#sugar_set_xcode_ios_sdkroot)
 * `single_view_application` (like `Xcode`: `iOS` -> `Application` -> `Single View Application`)
 * `_universal_library` build/install universal library (i386 + arm, iphoneos + iphonesimulator), used function:
[sugar_install_ios_library](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_install_ios_library)
 * `link_library` link universal library to ios target. 
See [wiki](https://github.com/ruslo/sugar/wiki/Building-universal-ios-library) for detailed description.
 * `link_package` link universal library using `find_package` command
 * `universal_library_osx_sysroot` create universal library by set `CMAKE_OSX_SYSROOT` to `iphoneos` and
using [sugar_install_library](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_install_library) function
* 07 (cocoa): building macosx application (`Xcode`)
* 08 (doxygen): example of adding doxygen generation target,
used function: [sugar_doxygen_generate](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_doxygen_generate)
* *TODO*: more...

*Note*: mark `used functions` show only first appearance of function in examples
## Run all
`test.py` script can run all examples using different generators (`Make`, `Xcode`, ...)
and configurations (`Debug`, `Release`). See this [wiki](https://github.com/ruslo/sugar/wiki/Examples-testing)
