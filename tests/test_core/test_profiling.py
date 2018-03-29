#!/usr/bin/env python
# coding: utf-8

r"""Tests for the core.profiling.py module"""

import logging

# import pytest

from corelib.core.profiling import timeit

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s :: %(levelname)6s ::'
                           '%(module)20s :: %(lineno)3d :: %(message)s')


@timeit
def dummy():
    r"""Just a dummy function to profile"""
    for x in range(500000):
        x**2


def test_timeit():
    r"""Just call the function"""
    dummy()
