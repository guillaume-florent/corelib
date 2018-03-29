# coding: utf-8

r"""Force conversions"""

from corelib.units.base import create_code

forces = {"N": 1., "newton": 1., "newtons": 1.,
          "kgf": 9.81, "kilogram_force": 9.81, "kilograms_force": 9.81}

for k in forces.keys():
    exec(create_code("forces", k), globals())


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
