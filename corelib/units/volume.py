# coding: utf-8

r"""Volume conversions"""

from corelib.units.base import create_code


volumes = {"m3": 1., "cubic_meter": 1., "cubic_meters": 1.,
           "l": 0.001, "litre": 0.001, "liter": 0.001, "litres": 0.001, "liters": 0.001,
           "cm3": 1e-6, "centimeter_cube": 1e-6, "centimeters_cube": 1e-6,
           "ml": 1e-6, "millilitre": 1e-6, "millilitres": 1e-6, "milliliter": 1e-6, "milliliters": 1e-6,
           "mm3": 1e-9, "millimeter_cube": 1e-9, "millimeters_cube": 1e-9,
           "pt": 568.26125 * 1e-6, "pint": 568.26125 * 1e-6, "pints": 568.26125 * 1e-6,
           "qt": 1136.5225 * 1e-6, "quart": 1136.5225 * 1e-6, "quarts": 1136.5225 * 1e-6,
           "gal": 4546.09 * 1e-6, "gallon": 4546.09 * 1e-6, "gallons": 4546.09 * 1e-6}

for k in volumes.keys():
    exec(create_code("volumes", k), globals())


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
