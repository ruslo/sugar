#!/usr/bin/env python3

# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

import argparse
import os
import re
import subprocess
import sys
import tempfile

parser = argparse.ArgumentParser(
    description="""
        ios-device launcher. Expected that application is gtest.
        If output is looks like passed test - exit with 0,
        otherwise exit with 1
        """
)

parser.add_argument(
    '--deploy',
    type=str,
    required=True,
    help='full path to ios-deploy'
)

parser.add_argument(
    '--target',
    type=str,
    required=True,
    help='name of target to launch'
)

parser.add_argument(
    '--args',
    type=str,
    nargs='*',
    help='arguments passed to application'
)

parser.add_argument(
    '--configuration',
    type=str,
    required=True,
    help='build configuration (e.g. Release, Debug)'
)

parser.add_argument(
    '--verbose',
    action='store_true',
    help='print a lot info'
)

args = parser.parse_args()

class Log:
  def __init__(self):
    self.verbose = args.verbose
  def p(self, message):
#    if self.verbose:
      print(message)

log = Log()

build_command = ['xcodebuild', '-sdk', 'iphoneos', '-arch', 'arm64']
build_command.append('-target')
build_command.append(args.target)
build_command.append('-configuration')
build_command.append(args.configuration)
subprocess.check_call(build_command)

application = '{}.app'.format(args.target)

def find_application(dir):
  for root, dirs, unused_filenames in os.walk(os.getcwd()):
    if not dir in dirs:
      continue
    walk_base = os.path.join(root, dir)
    for root_new, dirs_new, unused_filenames in os.walk(walk_base):
      if application in dirs_new:
        return os.path.join(root_new, application)
  message = '{} not found in {}'.format(application, dir)
  sys.exit(message)

app = find_application('{}-iphoneos'.format(args.configuration))

log.p('app found: {}'.format(app))

def try_run_device(application):
  launch_command = [
      args.deploy,
      '--noninteractive', 
      '--uninstall', 
      '--debug', 
      '--bundle', 
      application,
  ]
  if args.args:
    launch_command.append('--args')
    for x in args.args:
      launch_command.append(x)

  return subprocess.check(launch_command)

result = try_run_device(app)
log.p('exit code: {}'.format(result))
sys.exit(result)
