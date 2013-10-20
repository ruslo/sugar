// Copyright (c) 2013, Ruslan Baratov
// All rights reserved.

#include <stdlib.h> // EXIT_SUCCESS
#include <iostream> // std::cout
#include <boost/asio.hpp> // boost::asio::io_service
#include <boost/thread.hpp> // boost::thread

void print_hello();

int main() {
  boost::asio::io_service io_service;

  boost::thread thread(print_hello);
  thread.join();

  return EXIT_SUCCESS;
}

void print_hello() {
  std::cout << "hello" << std::endl;
}
