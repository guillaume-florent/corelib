# coding: utf-8

r"""Common logic for the conversion modules

This logic is used by every module but temperature.py as temperature conversions
are more complex than multiplying by a conversion coefficient.

"""

code = """def %s(**kwargs):
    if len(kwargs.items()) != 1:
        raise ValueError("Too many keywords")
    try:
        # wrapping in list of keys and values if for Python 3 compatibility
        result = list(kwargs.values())[0] * %s[list(kwargs.keys())[0]] / %s['%s']
    except KeyError:
        raise KeyError("Unknown input unit")
    return result
"""


def create_code(dict_name, key_name):
    r"""Create the code to be compiled on the fly by the conversion modules

    Parameters
    ----------
    dict_name : str
        The name of the dictionary that defines the units
        in the conversion module
    key_name : str
        The key name in the dictionary that defines the units
        in the conversion module

    Returns
    -------
    str
        Python code string

    """
    return code % (key_name, dict_name, dict_name, key_name)
