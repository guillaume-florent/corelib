# coding: utf-8

r"""Utility functions for testing"""


def equals_tolerance(value, target_value, tolerance):
    r"""Checks if a value is within a tolerance of a target value

    Parameters
    ----------
    value : float
    target_value : float
    tolerance : float

    """
    if target_value - tolerance <= value <= target_value + tolerance:
        return True
    else:
        return False


def equals_relative(value, target_value, pct_error):
    r"""Checks if a value is within a percentage error of a target value

    Parameters
    ----------
    value : float
    target_value : float
    pct_error : float

    """
    return equals_tolerance(value, target_value, target_value / 100 * pct_error)
