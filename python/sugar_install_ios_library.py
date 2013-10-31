#!/usr/bin/env python3

# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

import argparse
import glob
import os
import subprocess

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

args = parser.parse_args()
target = args.target
dst = args.destination

os.makedirs(dst, exist_ok=True)

def run_xcode(configuration, sdk):
  subprocess.check_call(
      'xcodebuild -target {} -configuration {} -sdk {}'.format(
          target, configuration, sdk
      ),
      shell=True
  )

run_xcode('Debug', 'iphoneos')
run_xcode('Release', 'iphoneos')
run_xcode('Debug', 'iphonesimulator')
run_xcode('Release', 'iphonesimulator')

def detect_file(dir):
  lib_list = glob.glob('./{}/*{}*'.format(dir, target))
  if len(lib_list) == 0:
    print('target "{}" not found in directory "{}"'.format(target, dir))
  if len(lib_list) != 1:
    print('multiple target "{}" found in directory "{}"'.format(target, dir))
  return lib_list[0]

debug_arm = detect_file('Debug-iphoneos')
debug_x86 = detect_file('Debug-iphonesimulator')

debug_result = '{}/lib{}-d.a'.format(dst, target)
subprocess.check_call(
    'lipo -output {} -create {} {}'.format(
        debug_result, debug_arm, debug_x86
    ),
    shell=True
)

release_arm = detect_file('Release-iphoneos')
release_x86 = detect_file('Release-iphonesimulator')

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
