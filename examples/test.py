#!/usr/bin/env python3

# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

help_wiki = "https://github.com/ruslo/sugar/wiki/Examples-testing"

import os
import argparse
import re
import sys
import subprocess

try:
  gitenv_root = os.environ["GITENV_ROOT"]
  if not gitenv_root:
    sys.exit("GITENV_ROOT is empty (see {})".format(help_wiki))
  py_modules_path = os.path.join(gitenv_root, 'configs', 'python')
  if not os.path.exists(py_modules_path):
    sys.exit("Path '{}' not found (see {})".format(py_modules_path, help_wiki))
  sys.path.append(py_modules_path)
except KeyError:
  sys.exit("Please setup GITENV_ROOT varialble (see: {})".format(help_wiki))

import detail.command
import detail.trash
import detail.os_detect
import detail.argparse

top_dir = os.getcwd()

parser = argparse.ArgumentParser()

parser.add_argument(
    '--dir',
    type=detail.argparse.is_dir,
    nargs='?',
    help="directory to test (test all by default)"
)

parser.add_argument(
    '--exclude',
    type=detail.argparse.is_dir,
    nargs='*',
    help="exclude this directory patterns"
)

parser.add_argument(
    '--libcxx',
    action='store_true',
    help='compile and link with libcxx library'
)

args = parser.parse_args()

print('exclude directories: {}'.format(args.exclude))

# test:
#  Unix Makefiles _builds/make-debug
#  Xcode _builds/xcode
#  Visual Studio 11 _builds/msvc

class Config:
  def __init__(self, generator, additional, directory, build):
    self.generator = generator
    self.additional = additional
    self.directory = directory
    self.build = build

configs = []

if args.libcxx:
  stdlib_flag = "'-stdlib=libc++'"
  libcxx_flag = "-DCMAKE_CXX_FLAGS={}".format(stdlib_flag)

  # differ from CMAKE_CXX_FLAGS for Xcode
  libcxx_flag += " -DCMAKE_EXE_LINKER_FLAGS={}".format(stdlib_flag)
else:
  libcxx_flag = ''

if detail.os_detect.windows:
  sys.exit("Not tested (see {})".format(help_wiki))
  configs.append(Config('Visual Studio', '', 'msvc', 'nmake')) # ???
else:
  debug_opt = '-DCMAKE_BUILD_TYPE=Debug {}'.format(libcxx_flag)
  release_opt = '-DCMAKE_BUILD_TYPE=Release {}'.format(libcxx_flag)
  default_opt = '{}'.format(libcxx_flag)

  configs.append(Config('Unix Makefiles', default_opt, 'make-default', 'make'))
  configs.append(Config(
      'Unix Makefiles', release_opt, 'make-release', 'make'
  ))
  configs.append(Config(
      'Unix Makefiles', debug_opt, 'make-debug', 'make'
  ))

if detail.os_detect.macosx:
  default_opt = '{}'.format(libcxx_flag)
  configs.append(Config('Xcode', default_opt, 'xcode', 'xcodebuild'))

done_list = []

def run_cmake_test(root, config):
  build_dir=os.path.join(root, '_builds', config.directory)
  detail.trash.trash(build_dir, ignore_not_exist=True)

  os.makedirs(build_dir)
  os.chdir(build_dir)

  try:
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')
    print('------------- running cmake in "{}"'.format(build_dir))
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    command = ['cmake', '-G', '{}'.format(config.generator)]
    command += config.additional.split()
    command.append('../..')
    detail.command.run(command)
    print('running make ({})'.format(config.additional))
    detail.command.run([config.build])
    print('done')
  except subprocess.CalledProcessError:
    sys.exit('run failed in "{}" directory'.format(root))

  done_list.append('dir = {}, generator = {}'.format(root, config.generator))

  os.chdir(top_dir)

for root, dirs, files in os.walk('./'):
  for filename in files:
    if filename != 'CMakeLists.txt':
      continue
    if args.dir and not re.match(args.dir, root):
      print('skip "{}" directory (not fit "{}")'.format(root, args.dir))
      continue

    excluded = False
    for exclude_dir in args.exclude:
      if exclude_dir and re.match(exclude_dir, root):
        print('skip "{}" directory (excluded)'.format(root))
        excluded = True
        break
    if excluded:
      continue

    file_path = os.path.join(root, filename)
    print('check file = {}'.format(file_path))
    file_id = open(file_path)
    content = file_id.read()
    if not re.search(r'\nproject(.*)\n', content):
      continue

    for config in configs:
      run_cmake_test(root, config)

print('DONE LIST:')
for x in done_list:
  print(x)
