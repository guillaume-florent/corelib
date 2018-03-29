# coding: utf-8

r"""Profiling related functions and decorators"""

import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def timeit(f):
    r"""Decorator that reports the time spent in a function

    Parameters
    ----------
    f : function
        The function to time

    """
    @wraps(f)
    def f_timer(*args, **kwargs):
        r"""Wrapping function"""
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        timing_message = "** {function_name} took {seconds} seconds"
        logger.info(timing_message.format(function_name=f.__name__,
                                          seconds=end - start))
        return result
    return f_timer

