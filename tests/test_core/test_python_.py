#!/usr/bin/env python
# coding: utf-8

r"""Tests for the core.python_.py module"""

# import pytest

from corelib.core.python_ import is_valid_python, init_from_args


def test_is_valid_python():
    r"""Test Python code (as string) validity"""
    assert is_valid_python("a = 1") is True
    assert is_valid_python("a == 1") is True
    assert is_valid_python("a === 1") is False


class A(object):
    r"""Dummy class for testing"""
    def __init__(self, one, two, three, four=4):
        init_from_args(self)


def test_init_from_args():
    r"""The kwarg is left to its default value"""
    a = A(1, 2, 3)
    assert hasattr(a, "one")
    assert hasattr(a, "two")
    assert hasattr(a, "three")
    assert hasattr(a, "four")
    assert a.one == 1
    assert a.two == 2
    assert a.three == 3
    assert a.four == 4


def test_init_from_args_and_kwargs():
    r"""The kwarg is assigned a value different from default"""
    a_bis = A(1, 2, 3, four='four')
    assert hasattr(a_bis, "one")
    assert hasattr(a_bis, "two")
    assert hasattr(a_bis, "three")
    assert hasattr(a_bis, "four")
    assert a_bis.one == 1
    assert a_bis.two == 2
    assert a_bis.three == 3
    assert a_bis.four == 'four'
