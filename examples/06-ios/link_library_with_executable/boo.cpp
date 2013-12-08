// Copyright (c) 2013, Ruslan Baratov
// All rights reserved.

#include <iostream> // std::cout
#include <cstdlib> // EXIT_SUCCESS

int foo();

int main() {
  std::cout << "foo: " << foo() << std::endl;
  return EXIT_SUCCESS;
}
