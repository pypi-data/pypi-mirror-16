
This package contains utility functions used by devpi-server and devpi-client.

See http://doc.devpi.net for more information.


Changelog
=========

3.0.1 (2016-07-07)
------------------

- fix issue355: accept PyPy version numbers in package filenames


3.0.0 (2016-05-12)
------------------

- fully implement normalization from PEP-503 to allow pip 8.1.2 to install
  packages with dots in their name

- dropped support for Python 2.6.


2.0.10 (2016-05-11)
-------------------

- revert the normalization change, as it causes other issues


2.0.9 (2016-05-11)
------------------

- fix issue343 and issue344: fully implement normalization from PEP-503 to
  allow pip 8.1.2 to install packages with dots in their name


2.0.8 (2015-11-11)
------------------

- fix URL.joinpath to not add double slashes



