=========================================
textbisect - Binary search in a text file
=========================================

.. image:: https://travis-ci.org/aptiko/textbisect.svg?branch=master
    :alt: Build button
    :target: https://travis-ci.org/aptiko/textbisect

Description
===========

This Python 3 module provides functionality to search inside sorted text
files.  The lines of the files need not be all of the same length. The
module contains the following functions:

* ``text_bisect_left(a, x, lo=0, hi=None, key=lambda x: x)`` locates the
  insertion point for line *x* in seekable filelike object *a*
  consisting of a number of lines; *x* must be specified without a
  trailing newline. *a* must use ``\n`` as the newline character and
  must not perform any line endings translation (use ``open(...,
  newline='\n')``).  The parameters *lo* and *hi*, if specified, must be
  absolute positions within object *a*, and specify which part of *a* to
  search; the default is to search the entire *a*. The character pointed
  to by *hi* (or the last character of the object, if *hi* is
  unspecified) must be a newline. *key* is a function that is used to
  compare each line of *a* with *x*; line endings are removed from the
  lines of *a* before comparison. *a* must be sorted or the result will
  be undefined. If *x* compares equal to a line in *a*, the returned
  insertion point is the beginning of that line. The initial position of
  *a* is discarded. The function returns the insertion point, which is
  an integer between *lo* and *hi+1*, pointing to the beginning of a
  line; when it exits, *a* is positioned there.

* ``text_bisect_right()`` is the same as ``text_bisect_left()``, except
  that if *x* compares equal to a line in *a*, the returned insertion
  point is the beginning of the next line.

* ``text_bisect()`` is the same as ``text_bisect_right()``.

License
=======

| Copyright (C) 2016 Antonis Christofides

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
