#!/usr/bin/env python3

# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

import argparse
import os
import re
import sys
import textwrap

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
        Adapt sugar library:

        * add_library -> sugar_add_library
        * add_test -> sugar_add_test
        * add_executable -> sugar_add_executable
        * target_link_libraries -> sugar_target_link_libraries
    ''')
)

args = parser.parse_args()

class Log:
  def __init__(self):
    pass
  def p(self, message):
    print(message)

log = Log()

for root, dirs, files in os.walk('./'):
  if 'CMakeLists.txt' in files:
    filename = os.path.join(root, 'CMakeLists.txt')
    file_id = open(filename)
    log.p('==========================================')
    log.p('Process file: {}'.format(filename))

    input = file_id.read()
    log.p('File content:\n{}'.format(input))

    include_list = []

    output = re.sub(r'\badd_library\b', 'sugar_add_library', input)
    if output != input:
      include_list.append('sugar_add_library')

    input = output
    output = re.sub(r'\badd_test\b', 'sugar_add_gtest', input)
    if output != input:
      include_list.append('sugar_add_gtest')

    input = output
    output = re.sub(r'\badd_executable\b', 'sugar_add_executable', input)
    if output != input:
      include_list.append('sugar_add_executable')

    input = output
    output = re.sub(
        r'\btarget_link_libraries\b', 'sugar_target_link_libraries', input
    )
    if output != input:
      include_list.append('sugar_target_link_libraries')

    include_list.sort()

    for x in include_list:
      log.p('to include: {}'.format(x))

    if include_list:
      includes = '\n'.join('include({})'.format(x) for x in include_list)
      output = re.sub(r'\n(?!#)', '\n\n{}\n'.format(includes), output, count=1)

    log.p('Result content:\n{}'.format(output))
    file_id = open(filename, 'w')
    file_id.write(output)
