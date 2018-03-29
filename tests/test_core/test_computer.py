#!/usr/bin/env python
# coding: utf-8

r"""Tests for the computer.py module

Warning
-------

The expected results are for an Intel Core i7 - 2670QM 2.2 GHz

1 processor
4 cores
8 threads

Todo
----

Run the test on a dual CPU motherboard

"""

from corelib.core.computer import physical_memory, processor, number_of_cores, \
    number_of_threads


def test_physical_memory():
    r"""Test total physical memory"""
    # Old PC Asus G53
    # assert physical_memory() == 4271013888

    # New PC Asus G502VS
    assert physical_memory() == 17112649728


def test_processor():
    r"""Test processor description"""
    # Old PC Asus G53
    # assert processor() == "Intel64 Family 6 Model 42 Stepping 7, GenuineIntel"

    # New PC Asus G502VS
    assert processor() == "Intel64 Family 6 Model 94 Stepping 3, GenuineIntel"


def test_nb_cores():
    r"""Test number of cores"""
    assert number_of_cores() == 4


def test_nb_threads():
    r"""Test number of threads"""
    assert number_of_threads() == 8
