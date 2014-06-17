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

"""Create warning with clang/gcc support, xcode attribute, msvc"""
def make_xcode_msvc(warning_name, xcode, msvc):
  clang = SAME
  gcc = SAME
  objc = False
  return TableEntry(warning_name, clang, gcc, make(msvc), make(xcode), objc)

"""Create warning with clang and gcc support and"""
"""support with custom option for msvc"""
def make_clang_msvc(warning_name, msvc_options):
  clang = SAME
  gcc = SAME
  msvc = make(msvc_options)
  xcode = NO
  objc = False
  return TableEntry(warning_name, clang, gcc, msvc, xcode, objc)

"""Create warning for msvc"""
def make_msvc(warning_name, msvc_options):
  clang = NO
  gcc = NO
  msvc = make(msvc_options)
  xcode = NO
  objc = False
  return TableEntry(warning_name, clang, gcc, msvc, xcode, objc)

attr_arc_bridge = "CLANG_WARN__ARC_BRIDGE_CAST_NONARC"
attr_arc_repeat = "CLANG_WARN_OBJC_REPEATED_USE_OF_WEAK"
attr_conversion = "CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION"
attr_dep_func = "GCC_WARN_ABOUT_DEPRECATED_FUNCTIONS"
attr_deprecated_impl = "CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS"
attr_explicit_ownership = "CLANG_WARN_OBJC_EXPLICIT_OWNERSHIP_TYPE"
attr_implicit_atomic = "CLANG_WARN_OBJC_IMPLICIT_ATOMIC_PROPERTIES"
attr_miss_field = "GCC_WARN_ABOUT_MISSING_FIELD_INITIALIZERS"
attr_non_virt = "GCC_WARN_NON_VIRTUAL_DESTRUCTOR"
attr_objc_missing = "CLANG_WARN_OBJC_MISSING_PROPERTY_SYNTHESIS"

main_warnings_table = [
    # compatibility-c++98
    make_clang("c++98-compat"),
    make_clang("c++98-compat-pedantic"),

    # special-members
    make_msvc("assign-base-inaccessible", "4626"),
    make_msvc("assign-could-not-be-generated", "4512"),
    make_msvc("copy-ctor-could-not-be-generated", "4625"),
    make_msvc("dflt-ctor-base-inaccessible", "4623"),
    make_msvc("dflt-ctor-could-not-be-generated", "4510"),
    make_msvc("user-ctor-required", "4610"),

    # inline
    make_msvc("automatic-inline", "4711"),
    make_msvc("force-not-inlined", "4714"),
    make_msvc("not-inlined", "4710"),
    make_msvc("unreferenced-inline", "4514"),

    #
    make_msvc("behavior-change", "4350"),
    make_xcode("bool-conversion", "CLANG_WARN_BOOL_CONVERSION"),
    make_xcode("c++11-extensions", "CLANG_WARN_CXX0X_EXTENSIONS"),
    make_clang("cast-align"),
    make_msvc("catch-semantic-changed", "4571"),
    make_clang("conditional-uninitialized"),
    make_msvc("constant-conditional", "4127"),
    make_xcode("constant-conversion", "CLANG_WARN_CONSTANT_CONVERSION"),
    make_xcode_msvc("conversion", attr_conversion, "4244"),
    make_msvc("conversion-loss", "4244"),
    make_msvc("conversion-loss-return", "4242"),
    make_clang("covered-switch-default"),
    make_clang("deprecated"),
    make_xcode_msvc("deprecated-declarations", attr_dep_func, "4996"),
    make_xcode("deprecated-objc-isa-usage", "CLANG_WARN_DIRECT_OBJC_ISA_USAGE"),
    make_clang("deprecated-register"),
    make_msvc("digraphs-not-supported", "4628"),
    make_clang("disabled-macro-expansion"),
    make_xcode("documentation", "CLANG_WARN_DOCUMENTATION_COMMENTS"),
    make_clang("documentation-unknown-command"),
    make_xcode("empty-body", "CLANG_WARN_EMPTY_BODY"),
    make_xcode("enum-conversion", "CLANG_WARN_ENUM_CONVERSION"),
    make_xcode("exit-time-destructors", "CLANG_WARN__EXIT_TIME_DESTRUCTORS"),
    make_msvc("expression-has-no-effect", "4555"),
    make_clang("extra-semi"),
    make_xcode("format", "GCC_WARN_TYPECHECK_CALLS_TO_PRINTF"),
    make_xcode("four-char-constants", "GCC_WARN_FOUR_CHARACTER_CONSTANTS"),
    make_clang("global-constructors"),
    make_msvc("ill-formed-comma-expr", "4548"),
    make_clang("implicit-fallthrough"),
    make_msvc("inherits-via-dominance", "4250"),
    make_xcode("int-conversion", "CLANG_WARN_INT_CONVERSION"),
    make_xcode("invalid-offsetof", "GCC_WARN_ABOUT_INVALID_OFFSETOF_MACRO"),
    make_msvc("is-defined-to-be", "4574"),
    make_msvc("layout-changed", "4371"),
    make_xcode("missing-braces", "GCC_WARN_INITIALIZER_NOT_FULLY_BRACKETED"),
    make_xcode("missing-field-initializers", attr_miss_field),
    make_clang("missing-noreturn"),
    make_xcode("missing-prototypes", "GCC_WARN_ABOUT_MISSING_PROTOTYPES"),
    make_msvc("name-length-exceeded", "4503"),
    make_xcode("newline-eof", "GCC_WARN_ABOUT_MISSING_NEWLINE"),
    make_msvc("no-such-warning", "4619"),
    make_xcode_msvc("non-virtual-dtor", attr_non_virt, "4265"),
    make_msvc("object-layout-change", "4435"),
    make_clang("old-style-cast"),
    make_xcode("overloaded-virtual", "GCC_WARN_HIDDEN_VIRTUAL_FUNCTIONS"),
    make_clang_msvc("padded", "4820"),
    make_xcode("parentheses", "GCC_WARN_MISSING_PARENTHESES"),
    make_xcode("pointer-sign", "GCC_WARN_ABOUT_POINTER_SIGNEDNESS"),
    make_xcode("return-type", "GCC_WARN_ABOUT_RETURN_TYPE"),
    make_xcode("shadow", "GCC_WARN_SHADOW"),
    make_clang("shift-sign-overflow"),
    make_xcode("shorten-64-to-32", "GCC_WARN_64_TO_32_BIT_CONVERSION"),
    make_xcode_msvc("sign-compare", "GCC_WARN_SIGN_COMPARE", "4389"),
    make_xcode("sign-conversion", "CLANG_WARN_IMPLICIT_SIGN_CONVERSION"),
    make_msvc("signed-unsigned-compare", "4388"),
    make_msvc("signed-unsigned-mismatch", "4365"),
    make_msvc("static-ctor-not-thread-safe", "4640"),
    make_xcode_msvc("switch", "GCC_WARN_CHECK_SWITCH_STATEMENTS", "4062"),
    make_clang_msvc("switch-enum", "4061"),
    make_msvc("this-used-in-init", "4355"),
    make_clang_msvc("undef", "4668"),
    make_xcode("uninitialized", "GCC_WARN_UNINITIALIZED_AUTOS"),
    make_xcode("unknown-pragmas", "GCC_WARN_UNKNOWN_PRAGMAS"),
    make_clang("unreachable-code"),
    make_msvc("unreachable-code-simple", "4702"),
    make_msvc("unsafe-conversion", "4191"),
    make_xcode("unused-function", "GCC_WARN_UNUSED_FUNCTION"),
    make_xcode("unused-label", "GCC_WARN_UNUSED_LABEL"),
    make_xcode_msvc("unused-parameter", "GCC_WARN_UNUSED_PARAMETER", "4100"),
    make_xcode("unused-value", "GCC_WARN_UNUSED_VALUE"),
    make_xcode("unused-variable", "GCC_WARN_UNUSED_VARIABLE"),
    make_clang("used-but-marked-unused"),
    make_clang("weak-vtables"),

    ### Objective-C
    make_objc("arc-bridge-casts-disallowed-in-nonarc", attr_arc_bridge),
    make_objc("arc-repeated-use-of-weak", attr_arc_repeat),
    make_objc("deprecated-implementations", attr_deprecated_impl),
    make_objc("duplicate-method-match", "CLANG_WARN__DUPLICATE_METHOD_MATCH"),
    make_objc("explicit-ownership-type", attr_explicit_ownership),
    make_objc("implicit-atomic-properties", attr_implicit_atomic),
    make_objc("implicit-retain-self", "CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF"),
    make_objc("objc-missing-property-synthesis", attr_objc_missing),
    make_objc("objc-root-class", "CLANG_WARN_OBJC_ROOT_CLASS"),
    make_objc("protocol", "GCC_WARN_ALLOW_INCOMPLETE_PROTOCOL"),
    make_objc("receiver-is-weak", "CLANG_WARN_OBJC_RECEIVER_WEAK"),
    make_objc("selector", "GCC_WARN_MULTIPLE_DEFINITION_TYPES_FOR_SELECTOR"),
    make_objc("strict-selector-match", "GCC_WARN_STRICT_SELECTOR_MATCH"),
    make_objc("undeclared-selector", "GCC_WARN_UNDECLARED_SELECTOR"),
]

sugar.sugar_warnings_wiki_table_generator.generate(main_warnings_table)
sugar.sugar_warnings_leathers_generator.generate(main_warnings_table)
sugar.sugar_warnings_cmake_flags_generator.generate(main_warnings_table)
