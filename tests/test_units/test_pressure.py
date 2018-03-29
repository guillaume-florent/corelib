#!/usr/bin/env python
# coding: utf-8

r"""pressure.py tests"""

from corelib.units.pressure import millibar


def test_pressures():
    r"""Test expected values"""
    expected_value = 1e3
    atol = 1e-10
    assert expected_value - atol <= millibar(bar=1.) <= expected_value + atol
