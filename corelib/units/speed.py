# coding: utf-8

r"""Speed conversions"""

from corelib.units.base import create_code

speeds = {"ms": 1., "mps": 1., "meter_per_second": 1., "meters_per_second": 1.,
          "kmh": 1000./3600., "kilometer_per_hour": 1000./3600., "kilometers_per_hour": 1000./3600.,
          "kt": 1852./3600., "knt": 1852./3600., "knts": 1852./3600., "knot": 1852./3600., "knots": 1852./3600.}

for k in speeds.keys():
    exec(create_code("speeds", k), globals())


def convert(value, to_unit, from_unit):
    r"""Convenience function for cases where the to_unit and the from_unit are in string form

    Parameters
    ----------
    value : float or int
    to_unit : str
        The desired unit
    from_unit : str
        The input unit

    """
    return globals()[to_unit](**{from_unit: value})
