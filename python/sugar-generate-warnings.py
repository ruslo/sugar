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
    "  3. CMake functions for `sugar`:\n"
    "    - sugar_generate_warning_flag_by_name\n"
    "    - sugar_generate_warning_xcode_attr_by_name\n"
    "    - sugar_get_all_xcode_warning_attrs\n\n"
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
  def __init__(self, warning_name, clang, gcc, msvc, xcode, objc):
    self.warning_name = warning_name
    self.clang = clang
    self.gcc = gcc
    self.msvc = msvc
    self.xcode = xcode
    self.objc = objc

"""Create warning with clang/gcc support and xcode attribute"""
def make_xcode(warning_name, xcode):
  clang = SAME
  gcc = SAME
  msvc = NO
  objc = False
  return TableEntry(warning_name, clang, gcc, msvc, make(xcode), objc)

"""Create Objective-C warning with clang/gcc support and xcode attribute"""
def make_objc(warning_name, xcode):
  clang = SAME
  gcc = SAME
  msvc = NO
  objc = True
  return TableEntry(warning_name, clang, gcc, msvc, make(xcode), objc)

"""Create warning with clang/gcc support"""
def make_clang(warning_name):
  clang = SAME
  gcc = SAME
  msvc = NO
  xcode = NO
  objc = False
  return TableEntry(warning_name, clang, gcc, msvc, xcode, objc)


"""Create warning with clang and gcc support and"""
"""support with custom option for msvc"""
def make_clang_gcc_msvc(warning_name, msvc_options):
  clang = SAME
  gcc = SAME
  msvc = make(msvc_options)
  xcode = NO
  return TableEntry(warning_name, clang, gcc, msvc, xcode)

attr_dep_func = "GCC_WARN_ABOUT_DEPRECATED_FUNCTIONS"
attr_miss_field = "GCC_WARN_ABOUT_MISSING_FIELD_INITIALIZERS"
attr_implicit_atomic = "CLANG_WARN_OBJC_IMPLICIT_ATOMIC_PROPERTIES"
attr_objc_missing = "CLANG_WARN_OBJC_MISSING_PROPERTY_SYNTHESIS"
attr_deprecated_impl = "CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS"
attr_explicit_ownership = "CLANG_WARN_OBJC_EXPLICIT_OWNERSHIP_TYPE"
attr_arc_repeat = "CLANG_WARN_OBJC_REPEATED_USE_OF_WEAK"
attr_arc_bridge = "CLANG_WARN__ARC_BRIDGE_CAST_NONARC"

main_warnings_table = [
    make_clang("c++98-compat"),
    make_clang("c++98-compat-pedantic"),
    make_clang("cast-align"),
    make_clang("conditional-uninitialized"),
    make_xcode("conversion", "CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION"),
    make_clang("covered-switch-default"),
    make_clang("deprecated"),
    make_xcode("deprecated-declarations", attr_dep_func),
    make_xcode("deprecated-objc-isa-usage", "CLANG_WARN_DIRECT_OBJC_ISA_USAGE"),
    make_clang("deprecated-register"),
    make_clang("disabled-macro-expansion"),
    make_xcode("documentation", "CLANG_WARN_DOCUMENTATION_COMMENTS"),
    make_clang("documentation-unknown-command"),
    make_xcode("empty-body", "CLANG_WARN_EMPTY_BODY"),
    make_clang("extra-semi"),
    make_clang("global-constructors"),
    make_clang("implicit-fallthrough"),
    make_xcode("four-char-constants", "GCC_WARN_FOUR_CHARACTER_CONSTANTS"),
    make_clang("missing-noreturn"),
    make_xcode("non-virtual-dtor", "GCC_WARN_NON_VIRTUAL_DESTRUCTOR"),
    make_clang("old-style-cast"),
    make_clang("padded"),
    make_clang("shift-sign-overflow"),
    make_xcode("sign-compare", "GCC_WARN_SIGN_COMPARE"),
    make_xcode("switch", "GCC_WARN_CHECK_SWITCH_STATEMENTS"),
    make_clang("switch-enum"),
    make_clang("undef"),
    make_clang("unreachable-code"),
    make_xcode("unused-parameter", "GCC_WARN_UNUSED_PARAMETER"),
    make_clang("used-but-marked-unused"),
    make_clang("weak-vtables"),
    make_xcode("shadow", "GCC_WARN_SHADOW"),
    make_xcode("bool-conversion", "CLANG_WARN_BOOL_CONVERSION"),
    make_xcode("constant-conversion", "CLANG_WARN_CONSTANT_CONVERSION"),
    make_xcode("shorten-64-to-32", "GCC_WARN_64_TO_32_BIT_CONVERSION"),
    make_xcode("enum-conversion", "CLANG_WARN_ENUM_CONVERSION"),
    make_xcode("int-conversion", "CLANG_WARN_INT_CONVERSION"),
    make_xcode("sign-conversion", "CLANG_WARN_IMPLICIT_SIGN_CONVERSION"),
    make_xcode("missing-braces", "GCC_WARN_INITIALIZER_NOT_FULLY_BRACKETED"),
    make_xcode("return-type", "GCC_WARN_ABOUT_RETURN_TYPE"),
    make_xcode("parentheses", "GCC_WARN_MISSING_PARENTHESES"),
    make_xcode("missing-field-initializers", attr_miss_field),
    make_xcode("missing-prototypes", "GCC_WARN_ABOUT_MISSING_PROTOTYPES"),
    make_xcode("newline-eof", "GCC_WARN_ABOUT_MISSING_NEWLINE"),
    make_xcode("pointer-sign", "GCC_WARN_ABOUT_POINTER_SIGNEDNESS"),
    make_xcode("format", "GCC_WARN_TYPECHECK_CALLS_TO_PRINTF"),
    make_xcode("uninitialized", "GCC_WARN_UNINITIALIZED_AUTOS"),
    make_xcode("unknown-pragmas", "GCC_WARN_UNKNOWN_PRAGMAS"),
    make_xcode("unused-function", "GCC_WARN_UNUSED_FUNCTION"),
    make_xcode("unused-label", "GCC_WARN_UNUSED_LABEL"),
    make_xcode("unused-value", "GCC_WARN_UNUSED_VALUE"),
    make_xcode("unused-variable", "GCC_WARN_UNUSED_VARIABLE"),
    make_xcode("exit-time-destructors", "CLANG_WARN__EXIT_TIME_DESTRUCTORS"),
    make_xcode("overloaded-virtual", "GCC_WARN_HIDDEN_VIRTUAL_FUNCTIONS"),
    make_xcode("invalid-offsetof", "GCC_WARN_ABOUT_INVALID_OFFSETOF_MACRO"),
    make_xcode("c++11-extensions", "CLANG_WARN_CXX0X_EXTENSIONS"),
    make_objc("duplicate-method-match", "CLANG_WARN__DUPLICATE_METHOD_MATCH"),
    make_objc("implicit-atomic-properties", attr_implicit_atomic),
    make_objc("objc-missing-property-synthesis", attr_objc_missing),
    make_objc("protocol", "GCC_WARN_ALLOW_INCOMPLETE_PROTOCOL"),
    make_objc("selector", "GCC_WARN_MULTIPLE_DEFINITION_TYPES_FOR_SELECTOR"),
    make_objc("deprecated-implementations", attr_deprecated_impl),
    make_objc("strict-selector-match", "GCC_WARN_STRICT_SELECTOR_MATCH"),
    make_objc("undeclared-selector", "GCC_WARN_UNDECLARED_SELECTOR"),
    make_objc("objc-root-class", "CLANG_WARN_OBJC_ROOT_CLASS"),
    make_objc("explicit-ownership-type", attr_explicit_ownership),
    make_objc("implicit-retain-self", "CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF"),
    make_objc("arc-repeated-use-of-weak", attr_arc_repeat),
    make_objc("receiver-is-weak", "CLANG_WARN_OBJC_RECEIVER_WEAK"),
    make_objc("arc-bridge-casts-disallowed-in-nonarc", attr_arc_bridge),
]

sugar.sugar_warnings_wiki_table_generator.generate(main_warnings_table)
sugar.sugar_warnings_leathers_generator.generate(main_warnings_table)
sugar.sugar_warnings_cmake_flags_generator.generate(main_warnings_table)
