#!/usr/bin/env python
# coding: utf-8

r"""mass.py tests"""

from corelib.units.mass import kg


def test_mass():
    r"""Test expected values"""
    expected_value = 1000
    atol = 1e-10
    assert expected_value - atol <= kg(tons=1.) <= expected_value + atol
