Bear Installation Tool
======================

coala features a Bear Installation Tool that helps installing bears one by one
or all of them. This tool is helpful as it also manages to install the bears'
external dependencies.

Installation
============

To install the tool, simply run:

::

    $ pip3 install cpm

Usage
=====


To use the tool, you need to give it arguments.

To install bears, simply run ``cpm --install`` followed by names of bears,
or by ``all``. Therefore:

::

    $ cpm --install all

will install all the available bears, whereas

::

    $ cpm --install CPPCheckBear PEP8Bear

will install the specified bears only.

To see the full list of available bears, run

::

    $ cpm --show


For more information, run

::

    $ cpm --help
