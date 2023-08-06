Changelog
=========

dev
---

* -

0.4 (2016-08-04)
----------------

* Added support for decompilation of raw machine code (the ``raw`` mode).
* Added support for generating and downloading of control-flow graphs.
* Added support for generating and downloading of a call graph.
* Added support for selecting the format of the generated call and control-flow
  graphs.
* Added support for selecting a different style for naming of variables.
* Added support for selecting the type of optimizations to be performed by the
  decompiler.
* Added support for decompilation of unreachable functions.
* Added support for disabling the emission of addresses in the generated code.
* Added support for selecting functions to be decompiled.
* Added support for selecting address ranges to be decompiled.
* Added support for choosing what should be decoded in selective decompilation.
* Improved error messages in exceptions.

0.3 (2016-07-17)
----------------

* Added access to warnings in decompilation phases and their emission in the
  ``decompiler`` tool.
* Added obtaining of the compiled version of the input C file (provided that
  the input was a C file).
* Added support for selecting the compiler to be used when compiling C source
  files.
* Added support for selecting the optimizations to be used when compiling C
  source files.
* Added support for selecting whether C files should be compiled with debugging
  information.
* Added support for selecting whether compiled C files should be stripped.
* Added support for printing script versions via the ``-V``/``--version``
  parameter.

0.2 (2016-06-12)
----------------

* Added support for passing a PDB file to decompilations.
* Added support for selecting the target high-level language.
* Added support for selecting the architecture.
* Added support for selecting the file format.
* Added a new method to the ``Test`` service: ``echo()``. It echoes back the
  parameters passed via the `test/echo
  <https://retdec.com/api/docs/test.html#parameter-passing>`_ service.
* Added a `summary
  <https://retdec-python.readthedocs.io/en/latest/status.html>`_ of the
  supported parts of the `retdec.com API
  <https://retdec.com/api/docs/index.html>`_ into the `documentation
  <https://retdec-python.readthedocs.io/en/latest/>`_.
* ``Decompiler.start_decompilation()`` and ``Fileinfo.start_analysis()`` raise
  ``MissingParameterError`` when the input file is not given.
* Re-formatted the progress-log output from the ``decompiler`` tool to ensure
  that the ``[OK]`` parts are aligned properly.

0.1 (2015-09-13)
----------------

Initial release.
