#!/usr/bin/env python3

# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

import argparse
import os
import re

wiki = 'https://github.com/ruslo/sugar/wiki/Collecting-sources'
base = os.path.basename(__file__)

class Generator:
  def __init__(self):
    self.parser = argparse.ArgumentParser(
        description='Generate sugar.cmake files according to directory struct'
    )

  def parse(self):
    self.parser.add_argument(
        '--top',
        type=str,
        required=True,
        help='top directory of sources'
    )

    self.parser.add_argument(
        '--var',
        type=str,
        required=True,
        help='variable name'
    )

  def make_header_guard(dir):
    dir = dir.upper()
    dir = re.sub(r'\W', '_', dir)
    dir = re.sub('_+', '_', dir)
    dir = dir.lstrip('_')
    dir = dir.rstrip('_')
    dir += '_'
    return dir

  def process_file(dir, relative, source_variable, file_id, filelist, dirlist):
    file_id.write(
        '# This file generated automatically by:\n'
        '#   {}\n'
        '# see wiki for more info:\n'
        '#   {}\n\n'.format(base, wiki)
    )
    relative += '/sugar.cmake'
    hg = Generator.make_header_guard(relative)
    file_id.write(
        'if(DEFINED {})\n'
        '  return()\n'
        'else()\n'
        '  set({} 1)\n'
        'endif()\n\n'.format(hg, hg)
    )
    if filelist:
      file_id.write('include(sugar_files)\n')
    if dirlist:
      file_id.write('include(sugar_include)\n')
    if filelist or dirlist:
      file_id.write('\n')

    if dirlist:
      for x in dirlist:
        file_id.write("sugar_include({})\n".format(x))
      file_id.write('\n')

    if filelist:
      file_id.write("sugar_files(\n")
      file_id.write("    {}\n".format(source_variable))
      for x in filelist:
        file_id.write("    {}\n".format(x))
      file_id.write(")\n")

  def create(self):
    args = self.parser.parse_args()
    source_variable = args.var
    cwd = os.getcwd()
    for rootdir, dirlist, filelist in os.walk(args.top):
      try:
        filelist.remove('sugar.cmake')
      except ValueError:
        pass # ignore if not in list
      try:
        filelist.remove('CMakeLists.txt')
      except ValueError:
        pass # ignore if not in list

      relative = os.path.relpath(rootdir, cwd)
      with open('{}/sugar.cmake'.format(rootdir), 'w') as file_id:
        Generator.process_file(
            rootdir, relative, source_variable, file_id, filelist, dirlist
        )

  def run():
    generator = Generator()
    generator.parse()
    generator.create()

def main():
  generator = sugar.groups_generator.Generator(args.top, args.verbose)
  input_file = open(sugar.groups_generator.input_filename, 'r')
  content = input_file.read()
  for source in content.split(';'):
    if source:
      generator.add(source)

  generator.print_result()

if __name__ == '__main__':
  Generator.run()
