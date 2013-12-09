// Copyright (c) 2013, Ruslan Baratov
// All rights reserved.

#include <iostream> // std::cout

int foo() {
#ifdef NDEBUG
  std::cout << "Release" << std::endl;
#else
  std::cout << "Debug" << std::endl;
#endif
  return 0x42;
}
