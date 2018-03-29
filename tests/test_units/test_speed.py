#!/usr/bin/env python
# coding: utf-8

r"""speed.py tests"""

from corelib.units.speed import kmh


def test_speed():
    r"""Test expected values"""
    expected_value = 1.852
    atol = 1e-10
    assert expected_value - atol <= kmh(knots=1.) <= expected_value + atol
