#!/usr/bin/env python3

# Copyright (c) 2014, Ruslan Baratov
# All rights reserved.

import argparse
import sugar.sugar_warnings_wiki_table_generator
import sugar.sugar_warnings_leathers_generator
import sugar.sugar_warnings_cmake_flags_generator

parser = argparse.ArgumentParser(
    description="This script will generate next files using\n"
    "internal table `main_warnings_table` as source:\n\n"
    "  1. Wiki table for `leathers` C++ project\n"
    "  2. Suppression include files for `leathers` C++ project\n"
    "  3. CMake function `sugar_generate_warning_flag_by_name` for `sugar`\n\n"
    "Links:\n\n"
    "  https://github.com/ruslo/leathers\n"
    "  https://github.com/ruslo/sugar\n",
    formatter_class=argparse.RawTextHelpFormatter
)

args = parser.parse_args()

"""This is the type of table entry describing compiler support of warning"""
class CompilerEntryType:
  NO = 1 # This type of warning is not supported by compiler
  SAME = 2 # Compiler option is same as warning name
  CUSTOM = 3 # Supported by custom option

"""This table entry describe compiler support of warning"""
class CompilerEntry:
  def __init__(self, entry_type, custom_option):
    self.entry_type = entry_type;
    self.custom_option = custom_option
    length = len(self.custom_option)
    if self.entry_type == CompilerEntryType.CUSTOM:
      assert(length > 0)
    else:
      assert(length == 0)

  def wiki_entry(self):
    if self.entry_type == CompilerEntryType.NO:
      return "*no*"
    if self.entry_type == CompilerEntryType.SAME:
      return "**same**"
    assert(self.entry_type == CompilerEntryType.CUSTOM)
    assert(len(self.custom_option) > 0)
    return self.custom_option

  def cxx_entry(self, name):
    assert(self.valid())
    if self.entry_type == CompilerEntryType.SAME:
      return name
    assert(self.entry_type == CompilerEntryType.CUSTOM)
    return self.custom_option

  def valid(self):
    return self.entry_type != CompilerEntryType.NO

NO = CompilerEntry(CompilerEntryType.NO, "")
SAME = CompilerEntry(CompilerEntryType.SAME, "")

def make(custom_option):
  assert(len(custom_option) > 0)
  return CompilerEntry(CompilerEntryType.CUSTOM, custom_option)

"""This table entry contains warning name
and support for different compilers"""
class TableEntry:
  def __init__(self, warning_name, clang, gcc, msvc):
    self.warning_name = warning_name
    self.clang = clang
    self.gcc = gcc
    self.msvc = msvc

"""Create warning with clang and gcc support"""
def make_clang_gcc(warning_name):
  clang = SAME
  gcc = SAME
  msvc = NO
  return TableEntry(warning_name, clang, gcc, msvc)

"""Create warning with clang and gcc support and"""
"""support with custom option for msvc"""
def make_clang_gcc_msvc(warning_name, msvc_options):
  clang = SAME
  gcc = SAME
  msvc = make(msvc_options)
  return TableEntry(warning_name, clang, gcc, msvc)

main_warnings_table = [
    make_clang_gcc("c++98-compat"),
    make_clang_gcc("c++98-compat-pedantic"),
    make_clang_gcc("cast-align"),
    make_clang_gcc("conditional-uninitialized"),
    make_clang_gcc("conversion"),
    make_clang_gcc("covered-switch-default"),
    make_clang_gcc("deprecated"),
    make_clang_gcc("deprecated-register"),
    make_clang_gcc("disabled-macro-expansion"),
    make_clang_gcc("documentation"),
    make_clang_gcc("documentation-unknown-command"),
    make_clang_gcc("extra-semi"),
    make_clang_gcc("global-constructors"),
    make_clang_gcc("implicit-fallthrough"),
    make_clang_gcc("missing-noreturn"),
    make_clang_gcc("non-virtual-dtor"),
    make_clang_gcc("old-style-cast"),
    make_clang_gcc("padded"),
    make_clang_gcc("shift-sign-overflow"),
    make_clang_gcc("switch-enum"),
    make_clang_gcc("undef"),
    make_clang_gcc("unreachable-code"),
    make_clang_gcc("unused-parameter"),
    make_clang_gcc("used-but-marked-unused"),
    make_clang_gcc("weak-vtables"),
]

sugar.sugar_warnings_wiki_table_generator.generate(main_warnings_table)
sugar.sugar_warnings_leathers_generator.generate(main_warnings_table)
sugar.sugar_warnings_cmake_flags_generator.generate(main_warnings_table)
