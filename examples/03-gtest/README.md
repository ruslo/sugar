For this example `gtest` need to be build (Assumed that [gitenv](https://github.com/ruslo/gitenv) already cloned):
```bash
> cd ${GITENV_ROOT}
> git submodule update --init google/gtest/ && cd google/gtest
> cmake . && make
```

Note: [FindGTest](http://www.cmake.org/cmake/help/v2.8.11/cmake.html#module:FindGTest) designed so, that
both libraries must be located in gtest root directory.
