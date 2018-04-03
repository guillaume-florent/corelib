# coding: utf-8

r"""Mass conversions"""

from corelib.units.base import create_code

masses = {"kg": 1., "kilogram": 1., "kilograms": 1.,
          "g": 1e-3, "gram": 1e-3, "grams": 1e-3,
          "t": 1000., "ton": 1000., "tons": 1000.,
          "oz": 28.349523125 * 1e-3, "ounce": 28.349523125 * 1e-3, "ounces": 28.349523125 * 1e-3,
          "lb": 0.45359237, "pound": 0.45359237, "pounds": 0.45359237,
          "st": 6.35029318, "stone": 6.35029318, "stones": 6.35029318}

for k in masses.keys():
    exec(create_code("masses", k), globals())


def convert(value, to_unit, from_unit):
    r"""Convenience function for cases where the to_unit and the from_unit
    are in string form

    Parameters
    ----------
    value : float or int
    to_unit : str
        The desired unit
    from_unit : str
        The input unit

    """
    return globals()[to_unit](**{from_unit: value})
