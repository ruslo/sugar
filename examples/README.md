# Examples
## Prepare
Easiest way to test examples is to use [gitenv](https://github.com/ruslo/gitenv):
```bash
> git clone https://github.com/ruslo/gitenv
> cd gitenv/
> git submodule update --init sugar/
> git submodule update --init any/other/modules/you/need/to/test
> export GITENV_ROOT=`pwd`
> export SUGAR_ROOT="${GITENV_ROOT}/sugar"
> cd sugar/examples/NN-example/
> mkdir _builds
> (cd _builds/ && rm -rf * && cmake ..)
> make -C _builds/
```
If example not using `sugar_setup_gitenv_paths` function, environment variable `SUGAR_ROOT` is enough:
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
* 03 (gtest): example of detecting `GTEST_ROOT` with [gitenv](https://github.com/ruslo/gitenv),
used function: [sugar_setup_gitenv_paths](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_setup_gitenv_paths)
* 04 (boost.detect): example of detecting `BOOST_ROOT` with [gitenv](https://github.com/ruslo/gitenv)
* 05 (groups): generating groups for `Xcode` and `Visual Studio`, used function: [sugar_groups_generate](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_groups_generate)
* 06 (ios): building ios application (`Xcode`),
used function: [sugar_mark_macosx_resources](https://github.com/ruslo/sugar/tree/master/cmake/utility#sugar_mark_macosx_resources),
[sugar_set_xcode_ios_sdkroot](https://github.com/ruslo/sugar/tree/master/cmake/utility#sugar_set_xcode_ios_sdkroot)
* 07 (cocoa): building macosx application (`Xcode`)
* 08 (doxygen): example of adding doxygen generation target,
used function: [sugar_doxygen_generate](https://github.com/ruslo/sugar/tree/master/cmake/core#sugar_doxygen_generate)
* 09 (rapidjson): example of detecting `RAPIDJSON_INCLUDE_DIRS` with [gitenv](https://github.com/ruslo/gitenv)
* *TODO*: more...

## Run all
`test.py` script can run all examples using different generators (`Make`, `Xcode`, ...)
and configurations (`Debug`, `Release`). See this [wiki](https://github.com/ruslo/sugar/wiki/Examples-testing)
