Spans
=====


Spans is a pure Python implementation of PostgreSQL's range types [#]_. Range types
are conveinent when working with intervals of any kind. Every time you've found
yourself working with date_start and date_end, an interval may have been what
you were actually looking for.

Spans has successfully been used in production since its first release
30th August, 2013.

Here is an example on how to use ranges to determine if something happened in
the 90s.

.. code-block:: python

    >>> from spans import daterange
    >>> from datetime import date
    >>> the90s = daterange(date(1990, 1, 1), date(2000, 1, 1))
    >>> date(1996, 12, 4) in the90s
    True
    >>> date(2000, 1, 1) in the90s
    False
    >>> the90s.union(daterange(date(2000, 1, 1), date(2010, 1, 1)))
    daterange([datetime.date(1990, 1, 1), datetime.date(2010, 1, 1))))

If you are making a booking application for a bed and breakfast hotel and want
to ensure no room gets double booked:

.. code-block:: python

    from collections import defaultdict
    from datetime import date
    from spans import daterange

    # Add a booking from 2013-01-14 through 2013-01-15
    bookings = defaultdict(list, {
        1 : [daterange(date(2013, 1, 14), date(2013, 1, 16))]
    }

    def is_valid_booking(bookings, room, new_booking):
        return not any(booking.overlap(new_booking for booking in bookings[room])

    print is_valid_booking(
        bookings, 1, daterange(date(2013, 1, 14), date(2013, 1, 18))) # False
    print is_valid_booking(
        bookings, 1, daterange(date(2013, 1, 16), date(2013, 1, 18))) # True

The library supports ranges and sets of ranges. A ``range`` has no discontinuities
between its endpoints. For some applications this is a requirement and hence the
``rangeset`` type exists.

Apart from the above mentioned overlap operation; ranges support ``union``,
``difference``, ``intersection``, ``contains``, ``startswith``, ``endswith``,
``left_of`` and ``right_of``.

Built-in ranges:

- ``intrange``
- ``floatrange``
- ``strrangerange`` - For ``unicode`` strings
- ``daterange``
- ``datetimerange``
- ``timedeltarange``

For each one of the ``range`` types a ``rangeset`` type exists as well:

- ``intrangeset``
- ``floatrangeset``
- ``strrangerangeset``
- ``daterangeset``
- ``datetimerangeset``
- ``timedeltarangeset``

Motivation
----------
For a recent project of mine I started using PostgreSQL's ``tsrange`` type and
needed an equivalent in Python. These range types attempt to mimick PostgreSQL's
behavior in every way. Deviating from it is considered as a bug and should be
reported.

Installation
------------
Spans exists on PyPI.

.. code-block:: bash

    $ pip install Spans

Documentation
-------------
`Documentation <http://spans.readthedocs.org/en/latest/>`_ is hosted on Read the
Docs.

Use with Psycopg2
-----------------
To use these range types with Psycopg2 the PsycoSpans library exists [#]_.

Custom range types
------------------
Using your own types for ranges are easy, just extend a base class and you're
good to go:

.. code-block:: python

    from spans.types import range_, discreterange
    from spans.settypes import rangeset, discreterangeset

    class intrange(discreterange):
        __slots__ = ()
        type = int
        step = 1

    class intrangeset(discreterangeset):
        __slots__ = ()
        type = intrange

    class floatrange(range_):
        __slots__ = ()
        type = float

    class floatrangeset(rangeset):
        __slots__ = ()
        type = floatrange

For a deeper set of examples please refer to ``types.py`` and ``settypes.py``.

.. [#] http://www.postgresql.org/docs/9.2/static/rangetypes.html
.. [#] https://www.github.com/runfalk/psycospans

.. Include changelog on PyPI

Changelog
=========
Version are structured like the following: ``<major>.<minor>.<bugfix>``. The
first `0.1` release does not properly adhere to this. Unless explicitly stated,
changes are made by `Andreas Runfalk <https://github.com/runfalk>`_.

Version 0.3.0
-------------
Released on 26th August, 2016

- Added documentation for ``__iter__()``
- Fixed intersection of multiple range sets not working correctly
  (`bug #3 <https://github.com/runfalk/spans/issues/3>`_)
- Fixed iteration of ``rangeset`` returning an empty range
  when ``rangeset`` is empty
  (`bug #4 <https://github.com/runfalk/spans/issues/4>`_)

.. warning::
   This change is backwards incompatible to code that expect rangesets to always
   return at least one set when iterating.

Version 0.2.1
-------------
Released on 27th June, 2016

- Fixed ``rangeset`` not returning ``NotImplemented`` when
  comparing to classes that are not sub classes of ``rangeset``, pull request
  `#2 <https://github.com/runfalk/spans/pull/2>`_
  (`Michael Krahe <https://github.com/der-michik>`_)
- Updated license in ``setup.py`` to follow
  `recommendations <https://packaging.python.org/en/latest/distributing/#license>`_
  by PyPA

Version 0.2.0
-------------
Released on 22nd December, 2015

- Added ``__len__()`` to range sets
  (`Michael Krahe <https://github.com/der-michik>`_)
- Added ``contains()`` to range sets
  (`Michael Krahe <https://github.com/der-michik>`_)
- Added `Sphinx <http://sphinx-doc.org/>`_ style doc strings to all methods
- Added proper Sphinx documentation
- Added unit tests for uncovered parts, mostly error checking
- Added `wheel <https://www.python.org/dev/peps/pep-0427/>`_ to PyPI along with
  source distribution
- Fixed a potential bug where comparing ranges of different types would result
  in an infinite loop
- Changed meta class implementation for range sets to allow more mixins for
  custom range sets

Version 0.1.4
-------------
Released on 15th May, 2015

- Added ``.last`` property to
  ``discreterange``
- Added ``from_date()`` helper to
  ``daterange``
- Added more unit tests
- Improved pickle implementation
- Made type checking more strict for date ranges to prevent ``datetime`` from
  being allowed in ``daterange``

Version 0.1.3
-------------
Released on 27th February, 2015

- Added ``offset()`` to some range types
- Added ``offset()`` to some range set types
- Added sanity checks to range boundaries
- Fixed incorrect ``__slots__`` usage, resulting in ``__slots__`` not being used
  on most ranges
- Fixed pickling of ranges and range sets
- Simplified creation of new rangesets, by the use of the meta class
  ``metarangeset``

Version 0.1.2
-------------
Released on 13th June, 2014

- Fix for inproper version detection on Ubuntu's bundled Python interpreter

Version 0.1.1
-------------
Released on 12th June, 2014

- Readme fixes
- Syntax highlighting for PyPI page

Version 0.1.0
-------------
Released on 30th August, 2013

- Initial release


