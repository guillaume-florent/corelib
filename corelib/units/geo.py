# coding: utf-8

r"""Conversion between geo coordinates"""


def decimal_degrees(degrees=0, minutes=0, seconds=0):
    r"""Convert degrees and decimal minutes or degrees minutes seconds to decimal degrees

    Parameters
    ----------
    degrees : int or float
    minutes : int or float
    seconds : int or float

    Returns
    -------
    float
        decimal degrees

    Notes
    -----
    The intentional use of this function is to have all parameters with the same sign
    >>> decimal_degrees(20, 30, 45)
    However it can be use to substract 20 seconds to 30 degrees in the following way:
    >>> decimal_degrees(degrees=30, seconds=-20.)

    """
    if minutes >= 60 or seconds >= 60:
        raise ValueError("Minutes and seconds should be lesser than 60")
    if degrees > 180 or degrees < -180:
        raise ValueError("Degrees must lie in the -180 to 180 range")
    return degrees + minutes / 60. + seconds / 3600.


def degrees_minutes_seconds(decimal_degree=0):
    r"""Convert decimal degrees to degrees and decimal minutes and degrees minutes seconds

    Parameters
    ----------
    decimal_degree : float

    Returns
    -------
    tuple : int, int, float, float
        degrees
        minutes
        decimal_minutes (e.g. 30.99)
        seconds

    """
    if decimal_degree > 180 or decimal_degree < -180:
        raise ValueError("Degrees must lie in the -180 to 180 range")

    sign = decimal_degree / abs(decimal_degree) if decimal_degree != 0. else 1

    decimal_degree = abs(decimal_degree)
    degree = decimal_degree // 1  # Truncate degree to be an integer
    decimal_minute = (decimal_degree - degree) * 60.  # Calculate the decimal minutes
    minute = decimal_minute // 1  # Truncate minute to be an integer
    second = (decimal_minute - minute) * 60.  # Calculate the decimal seconds
    # Finally, re-impose the appropriate sign
    degree *= sign
    minute *= sign
    decimal_minute *= sign
    second *= sign
    return int(degree), int(minute), decimal_minute, second


