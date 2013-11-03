#!/usr/bin/env python3

# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

import argparse
import glob
import os
import subprocess
import sys

parser = argparse.ArgumentParser(
    description='Workaround for not working ios install command'
)

parser.add_argument(
    '--target',
    type=str,
    required=True,
    help='install target'
)

parser.add_argument(
    '--destination',
    type=str,
    required=True,
    help='destination directory'
)

parser.add_argument(
    '--verbose',
    action='store_true',
    help='print a lot info'
)

class Log:
  def __init__(self, verbose):
    self.verbose = verbose
  def p(self, message):
    if self.verbose:
      print(message)

debug_prefix = 'd'

args = parser.parse_args()
target = args.target
dst = args.destination

log = Log(args.verbose)

log.p('target: {}'.format(target))
log.p('destination: {}'.format(dst))

os.makedirs(dst, exist_ok=True)

def run_xcode(configuration, sdk):
  if sdk == 'iphonesimulator':
    arch = '-arch i386'
  else:
    arch = ''
  subprocess.check_call(
      'xcodebuild -target {} -configuration {} -sdk {} {}'.format(
          target, configuration, sdk, arch
      ),
      shell=True
  )

run_xcode('Debug', 'iphoneos')
run_xcode('Release', 'iphoneos')
run_xcode('Debug', 'iphonesimulator')
run_xcode('Release', 'iphonesimulator')

def detect_file(dir):
  cwd = os.getcwd()
  target_file = 'lib{}.a'.format(target)
  target_file_postfix = 'lib{}d.a'.format(target)
  for root, dirs, files in os.walk(cwd):
    if not dir in dirs:
      continue
    for target_root, x, target_files in os.walk(os.path.join(root, dir)):
      if target_file in target_files:
        return os.path.join(target_root, target_file)
      if target_file_postfix in target_files:
        return os.path.join(target_root, target_file_postfix)
  print('working directory: {}'.format(cwd))
  sys.exit(
      'file "{}" not found in directory "{}"'.format(target_file, dir)
  )

debug_arm = detect_file('Debug-iphoneos')
debug_x86 = detect_file('Debug-iphonesimulator')

log.p('detected debug files:\n  {}\n  {}'.format(debug_arm, debug_x86))

debug_result = '{}/lib{}{}.a'.format(dst, target, debug_prefix)
subprocess.check_call(
    'lipo -output {} -create {} {}'.format(
        debug_result, debug_arm, debug_x86
    ),
    shell=True
)

release_arm = detect_file('Release-iphoneos')
release_x86 = detect_file('Release-iphonesimulator')

log.p('detected release files:\n  {}\n  {}'.format(release_arm, release_x86))

release_result = '{}/lib{}.a'.format(dst, target)
subprocess.check_call(
    'lipo -output {} -create {} {}'.format(
        release_result, release_arm, release_x86
    ),
    shell=True
)

print(
    'Install universal library done:\n    {}\n    {}'.format(
        debug_result, release_result
    )
)
