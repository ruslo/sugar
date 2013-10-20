# Examples
## Prepare
Easiest way to test examples is to use [gitenv](https://github.com/ruslo/gitenv):
```bash
> git clone https://github.com/ruslo/gitenv
> cd gitenv/
> git submodule update --init sugar/
> export GITENV_ROOT=`pwd`
> cd sugar/examples/NN-example/
> mkdir _builds
> (cd _builds/ && rm -rf * && cmake ..)
> make -C _builds/

```
otherwise set [Sugar](https://github.com/ruslo/sugar/blob/master/cmake/Sugar) master file location manually,
overwrite this line:
```cmake
include($ENV{GITENV_ROOT}/sugar/cmake/Sugar)
```

## Description
* 00 (detect): create empty project and include `Sugar` master file, print updated variables.
* 01 (simple): introduction to [collecting](https://github.com/ruslo/sugar/tree/master/cmake/collecting) system, used functions: `sugar_include`, `sugar_files`
* 02 (common): creating two targets with common sources, first fill sources variables, then create targets
* 03 (gtest): example of detecting `GTEST_ROOT` with [gitenv](https://github.com/ruslo/gitenv)

## Run all
`test.py` script can run all examples using different generators (`Make`, `Xcode`, ...)
and configurations (`Debug`, `Release`). See this [wiki](https://github.com/ruslo/sugar/wiki/Examples-testing)
