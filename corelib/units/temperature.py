# coding: utf-8

r"""Temperature conversions"""


def farenheit(**kwargs):
    r"""Conversion to farenheit degrees"""
    if len(kwargs.items()) != 1:
            raise ValueError("Too many keywords")

    if list(kwargs.keys())[0] in ["celsius", "C"]:
        return (list(kwargs.values())[0] * 9./5) + 32.
    elif list(kwargs.keys())[0] in ["kelvin", "kelvins", "K"]:
        return (list(kwargs.values())[0] - 273.15) * 9./5 + 32
    else:
        raise KeyError("Unknown input unit")


def F(**kwargs):
    r"""Conversion to farenheit degrees"""
    return farenheit(**kwargs)


def farenheits(**kwargs):
    r"""Conversion to farenheit degrees"""
    return farenheit(**kwargs)


def celsius(**kwargs):
    r"""Conversion to celsius degrees"""
    if len(kwargs.items()) != 1:
            raise ValueError("Too many keywords")

    if list(kwargs.keys())[0] in ["farenheit", "F"]:
        return (list(kwargs.values())[0] - 32.) * 5./9
    elif list(kwargs.keys())[0] in ["kelvin", "kelvins", "K"]:
        return list(kwargs.values())[0] - 273.15
    else:
        raise KeyError("Unknown input unit")


def C(**kwargs):
    r"""Conversion to celsius degrees"""
    return celsius(**kwargs)


def kelvin(**kwargs):
    r"""Conversion to kelvin degrees"""
    if len(kwargs.items()) != 1:
            raise ValueError("Too many keywords")

    if list(kwargs.keys())[0] in ["farenheit", "F"]:
        return (list(kwargs.values())[0] - 32.) * 5./9 + 273.15
    elif list(kwargs.keys())[0] in ["celsius", "C"]:
        return list(kwargs.values())[0] + 273.15
    else:
        raise KeyError("Unknown input unit")


def K(**kwargs):
    r"""Conversion to Kelvin degrees"""
    return kelvin(**kwargs)


def kelvins(**kwargs):
    r"""Conversion to kelvin degrees"""
    return kelvin(**kwargs)


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
