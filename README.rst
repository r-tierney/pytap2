``pytap2`` - Object oriented interface to Linux Tun/Tap devices
===============================================================

.. image:: https://github.com/johnthagen/pytap2/workflows/python/badge.svg
    :target: https://github.com/johnthagen/pytap2/actions

.. image:: https://codeclimate.com/github/johnthagen/pytap2/badges/gpa.svg
   :target: https://codeclimate.com/github/johnthagen/pytap2

.. image:: https://codeclimate.com/github/johnthagen/pytap2/badges/issue_count.svg
   :target: https://codeclimate.com/github/johnthagen/pytap2

.. image:: https://codecov.io/github/johnthagen/pytap2/coverage.svg
    :target: https://codecov.io/github/johnthagen/pytap2

.. image:: https://img.shields.io/pypi/v/pytap2.svg
    :target: https://pypi.python.org/pypi/pytap2

.. image:: https://img.shields.io/pypi/status/pytap2.svg
    :target: https://pypi.python.org/pypi/pytap2

.. image:: https://img.shields.io/pypi/pyversions/pytap2.svg
    :target: https://pypi.python.org/pypi/pytap2/

Fork of `PyTap <https://pypi.python.org/pypi/PyTap/>`_ that supports Python 3.

Requirements
------------

Either the ``iproute2`` ( Recommended/default ) or the ``ifconfig`` command line utility must be installed for ``pytap2`` to operate.

To install ``iproute2`` on Debian/Ubuntu ( recommended ):

.. code:: shell-session

    $ sudo apt install iproute2

To install ``ipconfig`` on RHEL/Rocky Linux/Fedora:

.. code:: shell-session

    $ sudo yum install iproute2


To install ``ifconfig`` on Debian/Ubuntu: ( not recommended )

.. code:: shell-session

    $ sudo apt install net-tools

To install ``ifconfig`` on RHEL/Rocky Linux/Fedora:

.. code:: shell-session

    $ sudo yum install net-tools

Installation
------------

You can install, upgrade, and uninstall ``pytap2`` with these commands:

.. code:: shell-session

    $ pip install pytap2
    $ pip install --upgrade pytap2
    $ pip uninstall pytap2

Usage
-----

Using as a context manager automatically brings up the device and closes it at the
end of the ``with`` block.

.. code:: python

    from pytap2 import TapDevice

    with TapDevice() as device:
        device.ipconfig(mtu=1300)
        device.write(b'0000')

Or manually call ``up()`` and ``close()``.

.. code:: python

    from pytap2 import TapDevice

    device = TapDevice()
    device.up()
    device.ipconfig(mtu=1300)
    device.write(b'0000')
    device.close()

The ``fileno()`` method is defined, so that the device object can be passed directly
to `select() <https://docs.python.org/library/select.html#select.select>`_.

Releases
--------

Unreleased
^^^^^^^^^^

- Support Python 3.12.

2.3.0 - 2023-04-28
^^^^^^^^^^^^^^^^^^

- Drop Python 3.7 and support Python 3.11
- Support Mypy type checking for users

2.2.0 - 2021-11-06
^^^^^^^^^^^^^^^^^^

- Drop Python 3.6 and support Python 3.10.
- Document dependency on ``ifconfig``

2.1.0 - 2020-12-30
^^^^^^^^^^^^^^^^^^

- Drop Python 3.5 and support Python 3.9.
- Switch to GitHub Actions for CI.

2.0.0 - 2020-03-29
^^^^^^^^^^^^^^^^^^

- Drop Python 2.7.

1.6.0 - 2019-12-15
^^^^^^^^^^^^^^^^^^

- Drop Python 3.4 and support Python 3.8.
- Include license file.

1.5.0 - 2018-07-09
^^^^^^^^^^^^^^^^^^

Support Python 3.7.

1.4.0 - 2017-10-24
^^^^^^^^^^^^^^^^^^

Allow disabling packet information header (``IFF_NO_PI``) and default ``read()`` to read entire
MTU worth of data plus the packet information header if present.

1.3.0 - 2017-07-31
^^^^^^^^^^^^^^^^^^

Add ``fileno()`` method to support ``select()`` calls.

1.2.0 - 2017-06-19
^^^^^^^^^^^^^^^^^^

Context manager support added.

1.1.0 - 2017-06-17
^^^^^^^^^^^^^^^^^^

Allow ``read()`` to be called with a specific number of bytes to read.


1.0.0 - 2017-06-16
^^^^^^^^^^^^^^^^^^

Initial release that supports Python 2 and 3.
