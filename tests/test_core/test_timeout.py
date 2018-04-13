#!/usr/bin/env python
# coding: utf-8

r"""timeout.py tests"""

import pytest

import time
import platform
import multiprocessing

# from corelib.core.timeout import timeout, TimeoutError
from corelib.core.timeout import timeout


@timeout(1)
def f(waiting_time):
    r"""Dummy function that just waits"""
    time.sleep(waiting_time)
    return waiting_time


def test_timeout():
    r"""timeout decorator tests"""
    assert f(0.5) == 0.5

    if platform.system() == "Windows":
        with pytest.raises(multiprocessing.TimeoutError):
            f(2)
    elif platform.system() == "Linux":
        with pytest.raises(TimeoutError):
            f(2)
    else:
        raise NotImplementedError
