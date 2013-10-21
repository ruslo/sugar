// Copyright (c) 2013, Ruslan Baratov
// All rights reserved.

#include <stdlib.h> // EXIT_SUCCESS
#include <iostream> // std::cout
#include <rapidjson/document.h> // Document

int main() {
  const char* json = "{ \"hello\": \"world\" }";

  rapidjson::Document d;
  d.Parse<0>(json);

  std::cout << d["hello"].GetString() << std::endl;
  return EXIT_SUCCESS;
}
