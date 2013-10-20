For this example `boost` need to be build and placed to `${GITENV_ROOT}/boost/install` directory:
```bash
./bootstrap.sh --with-toolset=clang --with-libraries=filesystem,system,thread --prefix=${GITENV_ROOT}/boost/install
./b2 -d+2 link=static threading=multi variant=release,debug --layout=tagged cxxflags="-std=c++11 -stdlib=libc++ -ftemplate-depth=1024" linkflags="-stdlib=libc++" toolset=clang
./b2 -d+2 link=static threading=multi variant=release,debug --layout=tagged install
```
