cmake_minimum_required(VERSION 2.8)
project(sugar)

set(
    project_config
    "${CMAKE_CURRENT_BINARY_DIR}/generated/${PROJECT_NAME}Config.cmake"
)

set(config_install_dir "lib/cmake/${PROJECT_NAME}")
set(MODULE_INSTALL_DIR "cmake/module")

include(CMakePackageConfigHelpers)

# Use:
# * PROJECT_NAME
# * MODULE_INSTALL_DIR
configure_package_config_file(
    cmake/template/Config.cmake.in
    ${project_config}
    INSTALL_DESTINATION "${config_install_dir}"
    PATH_VARS MODULE_INSTALL_DIR
)

install(
    DIRECTORY
        cmake/module/collecting/
        cmake/module/core/
        cmake/module/print/
        cmake/module/utility/
    DESTINATION ${MODULE_INSTALL_DIR}
    FILES_MATCHING
    PATTERN "${PROJECT_NAME}_*.cmake"
)

install(FILES ${project_config} DESTINATION ${config_install_dir})
