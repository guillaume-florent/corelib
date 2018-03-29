#!/usr/bin/env python
# coding: utf-8

r"""area.py tests"""

from corelib.units.area import cm2, convert
from corelib.units import convert_area


def test_areas():
    r"""Test expected values"""
    expected_value = 1e4
    atol = 1e-10
    assert expected_value - atol <= cm2(m2=1.) <= expected_value + atol


def test_convert_function():
    r"""Test shortcut/api convert function"""
    expected_value = 1e4
    atol = 1e-10
    assert expected_value - atol <= convert(1., "cm2", "m2") <= expected_value + atol
    assert expected_value - atol <= convert(1., to_unit="cm2", from_unit="m2") <= expected_value + atol


def test_convert_area_function():
    r"""Test shortcut/api convert function"""
    expected_value = 1e4
    atol = 1e-10
    assert expected_value - atol <= convert_area(1., "cm2", "m2") <= expected_value + atol
    assert expected_value - atol <= convert_area(1., to_unit="cm2", from_unit="m2") <= expected_value + atol
