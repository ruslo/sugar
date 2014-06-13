#!/usr/bin/env python3

# Copyright (c) 2014, Ruslan Baratov
# All rights reserved.

"""
* Wiki table for `leathers` C++ project

Expected format:

 name        | Clang    | GCC      | MSVC |
-------------|----------|----------|------|
 cast-align  | **same** | **same** | *no* |
 conversion  | **same** | **same** | *no* |
 deprecated  | **same** | **same** | 4996 |

"""

def generate(main_warnings_table):
  head_name = "name"
  head_clang = "Clang"
  head_gcc = "GCC"
  head_msvc = "MSVC"

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
    return len(table_entry.clang.wiki_entry())

  def gcc_visitor(table_entry):
    return len(table_entry.gcc.wiki_entry())

  def msvc_visitor(table_entry):
    return len(table_entry.msvc.wiki_entry())

  max_name = calc_max(head_name, name_visitor)
  max_clang = calc_max(head_clang, clang_visitor)
  max_gcc = calc_max(head_gcc, gcc_visitor)
  max_msvc = calc_max(head_msvc, msvc_visitor)

  def fill_string(name, max_name):
    result = " " + name + " ";
    assert(max_name >= len(result))
    left = max_name - len(result)
    return result + " " * left

  wiki_file = open("wiki-table.txt", "w")

  s = "{}|{}|{}|{}|\n".format(
      fill_string(head_name, max_name),
      fill_string(head_clang, max_clang),
      fill_string(head_gcc, max_gcc),
      fill_string(head_msvc, max_msvc),
  )
  wiki_file.write(s)

  s = "{}|{}|{}|{}|\n".format(
      '-' * max_name,
      '-' * max_clang,
      '-' * max_gcc,
      '-' * max_msvc,
  )
  wiki_file.write(s)

  for entry in main_warnings_table:
    s = "{}|{}|{}|{}|\n".format(
        fill_string(entry.warning_name, max_name),
        fill_string(entry.clang.wiki_entry(), max_clang),
        fill_string(entry.gcc.wiki_entry(), max_gcc),
        fill_string(entry.msvc.wiki_entry(), max_msvc),
    )
    wiki_file.write(s)
