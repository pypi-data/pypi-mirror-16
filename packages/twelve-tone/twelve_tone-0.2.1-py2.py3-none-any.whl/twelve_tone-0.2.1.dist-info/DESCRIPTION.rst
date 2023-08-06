========
Overview
========



Twelve-tone matrix to generate dodecaphonic melodies.

Following a process created by the composer Arnold Schoenberg, this library
computes a matrix to create twelve-tone serialism melodies which compose each
of the 12 semitones of the chromatic scale with equal importance.

* Save your compositions to MIDI
* Free software: BSD license

Installation
============

::

    pip install twelve-tone

Quick Start
===========

::

    >>> from twelve_tone.composer import Composer
    >>> c = Composer()
    >>> c.compose()
    >>> c.get_melody()
    ['C# / Db', 'A# / Bb', 'F', 'D', 'G# / Ab', 'D# / Eb', 'F# / Gb',
        'A', 'C', 'G', 'B', 'E']

After you have composed a matrix of tone rows, you can save the composition to
MIDI:

::

    >>> c.compose()
    >>> c.save_to_midi(filename='TWELVE_TONE.mid')

The new MIDI file will be created in your current working directory. If you do
not specify a `filename` for your file, it will default to `example.mid`.

Documentation
=============

https://python-twelve-tone.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


Changelog
=========

0.1.0 (2016-08-20)
-----------------------------------------

* First release on PyPI.


