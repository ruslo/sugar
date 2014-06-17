#!/usr/bin/env python3

# Copyright (c) 2014, Ruslan Baratov
# All rights reserved.

"""
* Wiki table for `leathers` C++ project

Expected format:

 name        | Clang    | GCC      | MSVC | Xcode           | Objective-C |
-------------|----------|----------|------|-----------------|-------------|
 cast-align  | **same** | **same** | *no* | *no*            | no          |
 conversion  | **same** | **same** | *no* | GCC_WARN_SHADOW | no          |
 deprecated  | **same** | **same** | 4996 | *no*            | no          |

"""

def generate(main_warnings_table):
  head_name = "name"
  head_clang = "Clang"
  head_gcc = "GCC"
  head_msvc = "MSVC"
  head_xcode = "Xcode"
  head_objc = "Objective-C"

  def calc_max(head, visitor):
    max_len = len(head)
    for x in main_warnings_table:
      cur_len = visitor(x)
      if cur_len > max_len:
        max_len = cur_len
    return max_len + 2

  def name_visitor(table_entry):
    return len(table_entry.warning_name)

  def clang_visitor(table_entry):
    return len(table_entry.clang.wiki_entry(table_entry.warning_name))

  def gcc_visitor(table_entry):
    return len(table_entry.gcc.wiki_entry(table_entry.warning_name))

  def msvc_visitor(table_entry):
    return len(table_entry.msvc.wiki_entry(table_entry.warning_name))

  def xcode_visitor(table_entry):
    return len(table_entry.xcode.wiki_entry(table_entry.warning_name))

  def objc_visitor(table_entry):
    if table_entry.objc:
      return 3 # "yes"
    else:
      return 2 # "no"

  max_name = calc_max(head_name, name_visitor)
  max_clang = calc_max(head_clang, clang_visitor)
  max_gcc = calc_max(head_gcc, gcc_visitor)
  max_msvc = calc_max(head_msvc, msvc_visitor)
  max_xcode = calc_max(head_msvc, xcode_visitor)
  max_objc = calc_max(head_objc, objc_visitor)

  def fill_string(name, max_name):
    result = " " + name + " ";
    assert(max_name >= len(result))
    left = max_name - len(result)
    return result + " " * left

  wiki_file = open("wiki-table.txt", "w")

  s = "{}|{}|{}|{}|{}|{}|\n".format(
      fill_string(head_name, max_name),
      fill_string(head_clang, max_clang),
      fill_string(head_gcc, max_gcc),
      fill_string(head_msvc, max_msvc),
      fill_string(head_xcode, max_xcode),
      fill_string(head_objc, max_objc),
  )
  wiki_file.write(s)

  s = "{}|{}|{}|{}|{}|{}|\n".format(
      '-' * max_name,
      '-' * max_clang,
      '-' * max_gcc,
      '-' * max_msvc,
      '-' * max_xcode,
      '-' * max_objc,
  )
  wiki_file.write(s)

  for entry in main_warnings_table:
    if entry.objc:
      objc = "yes"
    else:
      objc = "no"

    s = "{}|{}|{}|{}|{}|{}|\n".format(
        fill_string(entry.warning_name, max_name),
        fill_string(entry.clang.wiki_entry(entry.warning_name), max_clang),
        fill_string(entry.gcc.wiki_entry(entry.warning_name), max_gcc),
        fill_string(entry.msvc.wiki_entry(entry.warning_name), max_msvc),
        fill_string(entry.xcode.wiki_entry(entry.warning_name), max_xcode),
        fill_string(objc, max_objc),
    )
    wiki_file.write(s)
