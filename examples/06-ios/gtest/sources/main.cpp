// Copyright (c) 2013, Ruslan Baratov
// All rights reserved.

#include <iostream> // std::cout
#include <gtest/gtest.h> // TEST

TEST(testcase, testname0) {
  ASSERT_EQ(3, 3);
}

TEST(testcase, testname1) {
  ASSERT_EQ(3, 3);
}

TEST(testcase, testname2) {
  ASSERT_EQ(3, 3);
}

TEST(testcase, testname3) {
#ifdef NDEBUG
  std::cout << "NDEBUG mode" << std::endl;
#endif
  ASSERT_EQ(3, 3);
}

TEST(testcase, testname4) {
  ASSERT_EQ(3, 3);
}
