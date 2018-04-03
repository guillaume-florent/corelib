# coding: utf-8

r"""Distance conversions"""

from corelib.units.base import create_code

distances = {"mm": 1e-3, "millimeter": 1e-3, "millimeters": 1e-3, "millimetre": 1e-3, "millimetres": 1e-3,
             "cm": 1e-2, "centimeter": 1e-2, "centimeters": 1e-2, "centimetre": 1e-2, "centimetres": 1e-2,
             "m": 1., "meter": 1., "meters": 1., "metre": 1., "metres": 1.,
             "km": 1000., "kilometer": 1000., "kilometers": 1000., "kilometre": 1000., "kilometres": 1000.,
             # "in": 0.0254,  # in is a reserved keyword in Python
             "inch": 0.0254, "inches": 0.0254,
             "ft": 0.3048, "foot": 0.3048, "feet": 0.3048,
             "yd": 0.9144, "yard": 0.9144, "yards": 0.9144,
             "mi": 1609.344, "mile": 1609.344, "miles": 1609.344,
             "ftm": 1.8288, "fathom": 1.8288, "fathoms": 1.8288,
             "nm": 1852., "nautical_mile": 1852., "nautical_miles": 1852.}

for k in distances.keys():
    # code = fs_units.base.create_code("distances", k)
    # exec code in module.__dict__
    # g = globals()
    exec(create_code("distances", k), globals())


def convert(value, to_unit, from_unit):
    r"""Convenience function for cases where the to_unit and the from_unit are
    in string form

    Parameters
    ----------
    value : float or int
    to_unit : str
        The desired unit
    from_unit : str
        The input unit

    """
    return globals()[to_unit](**{from_unit: value})
