# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

# Empty project. Test SUGAR_ROOT detected.

cmake_minimum_required(VERSION 2.8.4)
project(00-example-detect)

include($ENV{GITENV_ROOT}/sugar/cmake/Sugar)

message("Say hello: '${SUGAR_ROOT}'")
