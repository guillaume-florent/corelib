#!/usr/bin/python
# coding: utf-8

r"""Example distance conversion"""

import fsunits.distance

# convert 12.0 inches to centimeters
print(fsunits.distance.cm(inches=12.0))

# convert 55 cm to inches
print(fsunits.distance.inches(cm=55))
