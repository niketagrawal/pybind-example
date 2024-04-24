A sandbox repository to experiment structuring files and folders in projects that use pybind11 to create a python wrapper for a C++ code base with CMake based build system.


### Building cpp executable

1. Clone the repository
2. mkdir build/
3. cd build/
4. cmake ..
5. make
6. ./main

### Building python extension module
1. Clone the repository
2. pip install .
3. Open python interpreter
```
import pybind_project_example
pybind_project_example.add(3,4)
```

### Acknowledgements
This example uses the [pybind/scikit_build_example](https://github.com/pybind/scikit_build_example) as the starting point.
