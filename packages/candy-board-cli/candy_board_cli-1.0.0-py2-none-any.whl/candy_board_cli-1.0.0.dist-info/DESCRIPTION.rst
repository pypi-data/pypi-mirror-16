CANDY Board service CLI
=======================

|GitHub release| |License BSD3|

A CLI tool to communicate with a CANDY Board service running on systemd

pip Installation
----------------

::

    $ pip install candy-board-cli

pip Uninstallation
------------------

::

    $ pip candy-board-cli

Development
-----------

Prerequisites
~~~~~~~~~~~~~

-  `pandoc <http://pandoc.org>`__
-  `pypandoc <https://pypi.python.org/pypi/pypandoc/1.2.0>`__

On Mac OS:

::

    $ brew install pandoc
    $ pip install pypandoc

Local Installation test
~~~~~~~~~~~~~~~~~~~~~~~

::

    $ ./setup.py install --record files.txt

Local Uninstallation test
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ cat files.txt | xargs rm -rf

Revision history
================

-  1.0.0

   -  Initial public release

-  0.0.1

   -  Initial beta release

.. |GitHub release| image:: https://img.shields.io/github/release/CANDY-LINE/candy-board-cli.svg
   :target: https://github.com/CANDY-LINE/candy-board-cli/releases/latest
.. |License BSD3| image:: https://img.shields.io/github/license/CANDY-LINE/candy-board-cli.svg
   :target: http://opensource.org/licenses/BSD-3-Clause


