A Python interface to CryptoSys PKI Pro
=======================================

This is a free interface to the core CryptoSys PKI Pro library, which
must be installed on your system. CryptoSys PKI Pro is available from
http://www.cryptosys.net/pki/.

Requires: Python 2 only (probably requires 2.6 or above) on Windows
platforms only.

All code in is one module ``cryptosyspki.py`` for simplicity of
distribution. All methods are static methods.

This is designed to use in Python's REPL environment (we were attempting
to write our own but gave up because Python is easier and better).

We've kept the naming convention similar to the C# interface
http://www.cryptosys.net/pki/dotnetpki/ which in turn mirrored the C
function names, using the Python "style" of lowercase and underscores
for method names.

::

    FOO_BarBaz (C function) --> Foo.BarBaz (C# method) --> Foo.bar_baz (Py)

But we've taken the opportunity to rename a few awkwardly-named
functions from the C# code (usually caused by our own bad early
decisions back in the day or convoluted attempts to add new features).

Please treat this release as provisional regarding the naming of the
methods. We would very much like feedback on the code, especially
suggestions on naming that reduce the amount of typing or make things
simpler. Contact us at http://www.cryptosys.net/contact/.

For the moment, we reserve the right to change the method names if we
can see a better way (in our opinion, of course).

The in-line documention is deliberately sparse. Please refer to the main
manual for more details of each method
http://www.cryptosys.net/pki/manpki/. There is a cross-reference table
on our website.

There is a series of tests in ``test\test_pki.py``. This requires a
rather complicated setup with a subdirectory ``work`` in the same folder
as the ``test_pki.py`` file which should contain all the required test
files, available separately in the file ``pkiPythonTestFiles.zip``. The
test function then creates a temporary subdirectory which is deleted
automatically.

::

    test/
        test_pki.py  # this module
        work/        # this _must_ exist
            <all required test files>
            pki.tmp.XXXXXXXX/    # created by `setup_temp_dir()`
                <copy of all required test files>
                <files created by tests>

We've tested this using the Python 2.7.11 interpreter and IDLE, the
PyDev environment in Eclipse, and using ``py.test``.

To use in Python's REPL:

::

    >>> from cryptosyspki import *
    >>> Gen.version()
    110100
    >>> Hash.hex_from_data('abc')
    'a9993e364706816aba3e25717850c26c9cd0d89d'
    >>> Hash.hex_from_data('abc', Hash.Alg.SHA256)
    'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
    >>> h = Hash.data('abc')
    >>> print Cnv.tohex(h)
    A9993E364706816ABA3E25717850C26C9CD0D89D

If you don't like ``import *`` and find ``cryptosyspki`` a bit long to
type each time, try

::

    >>> import cryptosyspki as pki
    >>> pki.Gen.version()
    110100

The source code has been checked by ``flake8`` ignoring error codes
``E501,E701,E221,E222`` "line too long", "multiple statements on one
line (colon)", "multiple spaces before/after operator" (correspondence
on these issues will not be entered into!).

And, yes, we use the old Python 2 ``print`` statement a lot because we
like it and hate the new ``print()`` function, so please don't write in
suggesting we should use ``from __future__`` to make it a function.

| David Ireland
| DI Management Services Pty Ltd
| Australia
| <www.di-mgt.com.au> <www.cryptosys.net>
| 25 May 2015 (updated 27 August 2016)
