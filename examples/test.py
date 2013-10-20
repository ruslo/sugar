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
    sys.exit("Path '{}' not found (see {})".format(py_modules_path))
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

args = parser.parse_args()

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

if detail.os_detect.windows:
  sys.exit("Not tested (see {})".format(help_wiki))
  configs.append(Config('Visual Studio', '', 'msvc', 'nmake')) # ???
else:
  configs.append(Config(
      'Unix Makefiles', '-DCMAKE_BUILD_TYPE=Debug', 'make-debug', 'make'
  ))
  configs.append(Config(
      'Unix Makefiles', '-DCMAKE_BUILD_TYPE=Release', 'make-release', 'make'
  ))
  configs.append(Config('Unix Makefiles', '', 'make-default', 'make'))

if detail.os_detect.macosx:
  configs.append(Config('Xcode', '', 'xcode', 'xcodebuild'))

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

    detail.command.run([
        'cmake', '-G', '{}'.format(config.generator), config.additional, '../..'
    ])
    print('running make')
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
