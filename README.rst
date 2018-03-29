.. -*- coding: utf-8 -*-

corelib
=======

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