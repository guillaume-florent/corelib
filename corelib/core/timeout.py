# coding: utf-8

r"""timeout decorators for Windows and Linux

Beware that the Windows and the Linux decorator versions
do not raise the same exception if the timeout is exceeded

"""

import platform
# import errno
# import os
import signal

import multiprocessing
import multiprocessing.pool
from functools import wraps


def timeout(max_timeout):
    r"""Use the right timeout based on platform.system()

    Parameters
    ----------
    max_timeout : int or float
        The maximum time in seconds for the decorated function to complete

    """
    if platform.system() == "Windows":
        return timeout_windows(max_timeout)
    elif platform.system() == "Linux":
        return timeout_linux(max_timeout)
    else:
        raise NotImplementedError


def timeout_windows(max_timeout):
    """Timeout decorator, parameter in seconds.

    Parameters
    ----------
    max_timeout : int or float
        The maximum time in seconds for the decorated function to complete

    Raises
    ------
    multiprocessing.TimeoutError
        if the function call exceeds max_timeout

    """
    def timeout_decorator(item):
        """Wrap the original function."""
        @wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator


class TimeoutError(Exception):
    r"""Error for the Linux version of the timeout decorator"""
    pass


def timeout_linux(max_timeout):
    """Timeout decorator, parameter in seconds.

    Parameters
    ----------
    max_timeout : int or float
        The maximum time in seconds for the decorated function to complete

    Raises
    ------
    TimeoutError
        if the function call exceeds max_timeout

    """
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(max_timeout)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator
