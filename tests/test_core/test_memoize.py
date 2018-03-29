#!/usr/bin/env python
# coding: utf-8

r"""Tests for the core.memoize.py module

Using Fibonacci with a long enough sequence to make memoizing worth it.

"""

# import pytest
import time

from corelib.core.memoize import memoize, Memoize


def f(n):
    r"""Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1)+f(n-2)


@memoize
def f_memoized(n):
    r"""Same as f but memoized"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f_memoized(n-1)+f_memoized(n-2)


# Memoize is for instance methods
class A(object):
    @Memoize
    def f_Memoized(self, n):
        r"""Same as f but as a Memoized instance method"""
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.f_Memoized(n-1)+self.f_Memoized(n-2)


def test_speedup():
    r"""Make sure memoization brings a speedup"""
    nb = 33

    t0 = time.time()
    f(nb)
    t1 = time.time()

    tm0 = time.time()
    f_memoized(nb)
    tm1 = time.time()

    assert tm1 - tm0 < t1 - t0

    a = A()
    tM0 = time.time()
    a.f_Memoized(nb)
    tM1 = time.time()

    assert tM1 - tM0 < t1 - t0
