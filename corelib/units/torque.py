# coding: utf-8

r"""Torque conversions"""

from corelib.units.base import create_code

torques = {"Nm": 1., "newton_metre": 1., "newton_metres": 1., "newton_meter": 1., "newton_meters": 1.}

for k in torques.keys():
    exec(create_code("torques", k), globals())


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
