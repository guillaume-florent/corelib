#!/usr/bin/python
# coding: utf-8

r"""Example distance conversion"""

from corelib.units.distance import cm, inches

# convert 12.0 inches to centimeters
print(cm(inches=12.0))

# convert 55 cm to inches
print(inches(cm=55))
