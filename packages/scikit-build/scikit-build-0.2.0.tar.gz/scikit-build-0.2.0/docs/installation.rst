============
Installation
============

With pip::

    $ pip install scikit-build

To install the latest from source, first obtain the source code::

    $ git clone https://github.com/scikit-build/scikit-build
    $ cd scikit-build

then install with::

    $ pip install .

or::

    $ pip install -e .

for development.


Dependencies
------------

Python Packages
^^^^^^^^^^^^^^^

The project has a few common Python package dependencies. The runtime
dependencies are:

.. include:: ../requirements.txt
   :literal:

the build time dependencies (also required for development) are:

.. include:: ../requirements-dev.txt
   :literal:

Compiler Toolchain
^^^^^^^^^^^^^^^^^^

The `same compiler toolchain used to build the CPython interpreter
<https://docs.python.org/devguide/setup.html#build-dependencies>`_ should also
be available. For example, on *Ubuntu Linux*, this can be installed with::

    $ sudo apt-get install build-essential

On *Mac OSX*, install `XCode <https://developer.apple.com/xcode/>`_ to build
packages for the system Python.

On Windows, install `the version of Visual Studio used to create the target
version of CPython <https://docs.python.org/devguide/setup.html#windows>`_

CMake
^^^^^

`Download standard CMake binaries <https://cmake.org/download>`_ for your platform or build from source
with a C++ compiler if binaries are not available.
