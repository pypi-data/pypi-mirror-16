# CMake generated Testfile for 
# Source directory: /home/matt/src/scikit-build/tests/samples/hello-cython/hello
# Build directory: /home/matt/src/scikit-build/tests/samples/hello-cython/_skbuild/cmake-build/hello
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(hello "/home/matt/bin/venvs/skbuild/bin/python" "-m" "hello")
set_tests_properties(hello PROPERTIES  WORKING_DIRECTORY "/home/matt/src/scikit-build/tests/samples/hello-cython/_skbuild/cmake-install")
