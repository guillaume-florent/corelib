# coding: utf-8

r"""Area conversions"""

from corelib.units.base import create_code

areas = {"m2": 1., "square_meter": 1., "square_meters": 1.,
         "cm2": 1e-4, "square_centimeter": 1e-4, "square_centimeters": 1e-4,
         "mm2": 1e-6, "square_millimeter": 1e-6, "square_millimeters": 1e-6}

for k in areas.keys():
    exec(create_code("areas", k), globals())


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
