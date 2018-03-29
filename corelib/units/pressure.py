# coding: utf-8

r"""Pressure conversions"""

from corelib.units.base import create_code

pressures = {"Pa": 1., "pascal": 1., "pascals": 1.,
             "hPa": 100., "hectopascal": 100., "hectopascals": 100.,
             "bar": 1e5, "bars": 1e5,
             "millibar": 100., "millibars": 100.,
             "mmHg": 133.322387415, "millimeter_of_mercury": 133.322387415, "millimeters_of_mercury": 133.322387415}

for k in pressures.keys():
    exec(create_code("pressures", k), globals())


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
