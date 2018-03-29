#!/usr/bin/env python
# coding: utf-8

r"""torque.py tests"""

from corelib.units.torque import Nm


def test_torque():
    r"""Test expected values"""
    expected_value = 1.
    atol = 1e-10
    assert expected_value - atol <= Nm(newton_metre=1.) <= expected_value + atol