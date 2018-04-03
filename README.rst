.. -*- coding: utf-8 -*-

corelib
=======

.. image:: https://travis-ci.org/guillaume-florent/corelib.svg?branch=master
    :target: https://travis-ci.org/guillaume-florent/corelib

.. image:: https://api.codacy.com/project/badge/Grade/48ceccfeea6a44c8b4487f8f8e9d32be
    :target: https://www.codacy.com/app/guillaume-florent/corelib?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=guillaume-florent/corelib&amp;utm_campaign=Badge_Grade

.. image:: https://anaconda.org/gflorent/corelib/badges/version.svg
    :target: https://anaconda.org/gflorent/corelib

.. image:: https://anaconda.org/gflorent/corelib/badges/latest_release_date.svg
    :target: https://anaconda.org/gflorent/corelib

.. image:: https://anaconda.org/gflorent/corelib/badges/platforms.svg
    :target: https://anaconda.org/gflorent/corelib

.. image:: https://anaconda.org/gflorent/corelib/badges/downloads.svg
    :target: https://anaconda.org/gflorent/corelib

.. image:: http://img.shields.io/badge/Python-2.7_3.*-ff8840.svg
    :target: https://www.python.org/downloads/
    :alt: Python 2.7 3.*

core package
------------

Code common to many projects


units package
-------------

Units conversion package. Convert distance, speed, area, volume, mass, pressure, force, torque, temperature and geo
coordinates. Geo coordinates (latitude and longitude) conversions between common formats (dd.dddd, dd mm.mmmm, dd mm ss)

Usage
~~~~~

convert unit_2 to unit_1 (fictitious example that will not work, only to show the principle):

.. code-block:: python

  unit_1(unit_2=1.)


convert meters to cm:

.. code-block:: python

  import corelib.units.distance
  corelib.units.distance.cm(meters=1.)


.. code-block:: python

  from corelib.units import convert_distance
  from corelib.units.distance import convert
  convert_distance(1., to_unit='cm', from_unit='meters')
  convert(1., to_unit='cm', from_unit='meters')


If a unit is not defined, a KeyError is raised