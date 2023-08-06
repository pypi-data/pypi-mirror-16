Changelog
=========


v0.2.0 (2016-08-02)
-------------------

- Add ``DateTime.datetime`` property that returns a native datetime.
- Add ``DateTime.fromgmtime`` that creates a ``DateTime`` from a UTC based ``time.struct_time``.
- Add ``DateTime.fromlocaltime`` that creates a ``DateTime`` from a local ``time.struct_time``.
- Add ``DateTime.isleap`` method that returns whether its year is a leap year.
- Add ``DateTime.leapdays`` that calculates the number of leap days between its year and another year.
- Add ``DateTime.start_of/end_of`` and other variants that return the start of end of a time frame:

  - ``start/end_of_century``
  - ``start/end_of_decade``
  - ``start/end_of_year``
  - ``start/end_of_month``
  - ``start/end_of_day``
  - ``start/end_of_hour``
  - ``start/end_of_minute``
  - ``start/end_of_second``

- Add ``DateTime.span`` that returns the start and end of a time frame.
- Add ``DateTime.span_range`` that returns a range of spans.
- Add ``DateTime.range`` that returns a range of datetimes.
- Add ``DateTime.add`` and ``DateTime.sub`` methods.
- Add ``years`` and ``months`` arguments to ``DateTime.shift/add/sub``.
- Drop support for milliseconds from ``DateTime.shift/add/sub``. **breaking change**
- Make ``DateTime.parse/format`` understand a subset of `Unicode date patterns <http://www.unicode.org/reports/tr35/tr35-19.html#Date_Field_Symbol_Table>`_.
- Set defaults for year (1970), month (1), and day (1) arguments to new ``DateTime`` objects. Creating a new ``DateTime`` now defaults to the start of the POSIX epoch.


v0.1.2 (2016-07-26)
-------------------

- Don't pin install requirements to a specific version; use ``>=`` instead.


v0.1.1 (2016-07-26)
-------------------

- Fix bug in ``DateTime.naive`` that resulted in a DateTime object being returned instead of a native datetime.


v0.1.0 (2016-07-26)
-------------------

- First release.
