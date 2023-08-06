Uses cffi to build a simple interface for calling functions in a C file. This
package is designed for convenience and should work only in the very simple
cases. It is used in an educational setting in a mixed Python/C programming
course.

Usage
=====

It is very simple. Say you have a "libfuncs.c" in the working directory

.. code-block::c
    #include<stdio.h>

    int double(int x) {
        return x + x;
    }

We can call the `double` function by relying in the implicit import in the
:mod:`ccall` module.

>>> import ccall as c
>>> c.libfuncs.double(21)
42


Limitations
===========

This software is beta. Use with care!
