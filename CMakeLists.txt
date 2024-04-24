# # Require CMake 3.15+ (matching scikit-build-core) Use new versions of all
# # policies up to CMake 3.27
# cmake_minimum_required(VERSION 3.15...3.27)

# # Scikit-build-core sets these values for you, or you can just hard-code the
# # name and version.
# project(
#   ${SKBUILD_PROJECT_NAME}
#   VERSION ${SKBUILD_PROJECT_VERSION}
#   LANGUAGES CXX)

# # Find the module development requirements (requires FindPython from 3.17 or
# # scikit-build-core's built-in backport)
# find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
# find_package(pybind11 CONFIG REQUIRED)

# # Add a library using FindPython's tooling (pybind11 also provides a helper like
# # this)
# python_add_library(_core MODULE src/main.cpp WITH_SOABI)
# target_link_libraries(_core PRIVATE pybind11::headers)

# # This is passing in the version as a define just as an example
# target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})

# # The install directory is the output (wheel) directory
# install(TARGETS _core DESTINATION pybind_project_example)


cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(PYBIND11_NEWPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)
find_package(Python COMPONENTS Interpreter Development REQUIRED)

add_executable(main src/main.cpp)



target_link_libraries(main PRIVATE pybind11::headers ${Python_LIBRARIES})
target_include_directories(main PRIVATE ${Python_INCLUDE_DIRS})
# Ceate executable for main.cpp





pybind11_add_module(_core src/main.cpp)

install(TARGETS _core LIBRARY DESTINATION .)