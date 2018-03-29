#!/usr/bin/env python
# coding: utf-8

r"""Tests for the core.files.py module"""

from os import remove
from os.path import isfile

import pytest

from corelib.core.files import path_from_file, is_binary


def test_happy_path():
    r"""The file_origin of path_from_file exists"""
    new_f = path_from_file(__file__, "tmp.txt")
    with open(new_f, "w") as nf:
        nf.write("\n")
    assert isfile(new_f) is True
    remove(new_f)
    assert isfile(new_f) is False


def test_wrong_file():
    r"""The file_origin of path_from_file does not exist"""
    with pytest.raises(ValueError):
        _ = path_from_file("C:/unknown_file.txt", "tmp.txt")


def test_is_binary():
    r"""Test if the files are binary or ASCII"""
    assert is_binary(path_from_file(__file__,
                                    "files/stl/board_binary.stl")) is True
    assert is_binary(path_from_file(__file__,
                                    "files/stl/board.stl")) is False
