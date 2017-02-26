cmake_minimum_required (VERSION 2.8)

install(DIRECTORY cmake DESTINATION share/sugar/)
install(FILES sugar-config.cmake DESTINATION share/sugar/)

enable_testing()
