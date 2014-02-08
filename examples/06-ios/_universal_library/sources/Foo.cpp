// Copyright (c) 2013, Ruslan Baratov
// All rights reserved.

#include "A.hpp"

#include <iostream> // std::cout

void A::print_info() {
#ifdef NDEBUG
  std::cout << "Hello from libA.a (release)" << std::endl;
#else
  std::cout << "Hello from libA.a (debug)" << std::endl;
#endif
}
