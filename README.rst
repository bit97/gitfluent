.. image:: assets/logo_200w.png

|Python compat| |PyPi| |GHA tests| |Codecov report| |readthedocs|

.. inclusion-marker-do-not-remove

gitfluent
==============

gitfluent is a simple library for working with git repositories following the Git Flow branching model.
It allows to create a new feature or bug branch from the current branch, and to merge it back into the
main branch after the work is done.


Features
========

Installation
============

gitfluent requires Python ``>=3.8`` and can be installed via:

.. code-block:: bash

   python -m pip install gitfluent


Usage
=====

.. code-block:: bash

   python -m gitfluent --help




.. |GHA tests| image:: https://github.com/bit97/fluentgit/workflows/tests/badge.svg
   :target: https://github.com/bit97/fluentgit/actions?query=workflow%3Atests
   :alt: GHA Status
.. |Codecov report| image:: https://codecov.io/github/bit97/fluentgit/coverage.svg?branch=main
   :target: https://codecov.io/github/bit97/fluentgit?branch=main
   :alt: Coverage
.. |readthedocs| image:: https://readthedocs.org/projects/fluentgit/badge/?version=latest
        :target: https://fluentgit.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
.. |Python compat| image:: https://img.shields.io/badge/>=python-3.8-blue.svg
.. |PyPi| image:: https://img.shields.io/pypi/v/gitfluent.svg
        :target: https://pypi.python.org/pypi/gitfluent
