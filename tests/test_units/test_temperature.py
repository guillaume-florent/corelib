#!/usr/bin/env python
# coding: utf-8

r"""temperature.py tests"""

from corelib.units.temperature import celsius, C, farenheit, farenheits, F, K, convert


def test_temperature():
    r"""Test expected values"""
    expected_value = 0.
    atol = 1e-10
    assert expected_value - atol <= celsius(farenheit=32.) <= expected_value + atol
    assert expected_value - atol <= C(farenheit=32.) <= expected_value + atol

    expected_value = 32.
    atol = 1e-10
    assert expected_value - atol <= farenheit(C=0.) <= expected_value + atol
    assert expected_value - atol <= farenheits(C=0.) <= expected_value + atol
    assert expected_value - atol <= F(C=0.) <= expected_value + atol

    expected_value = 273.15
    atol = 1e-10
    assert expected_value - atol <= K(celsius=0.) <= expected_value + atol


def test_convert():
    r"""Test the convert function"""
    expected_value = 273.15
    atol = 1e-10
    assert expected_value - atol <= convert(0., "K", "celsius") <= expected_value + atol
