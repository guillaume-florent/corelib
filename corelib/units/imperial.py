# coding: utf-8

r"""Parse and convert imperial distance units"""

from fractions import Fraction

from corelib.units.distance import convert


def convert_imperial_str(value, to_unit):
    r"""Convert a distance expressed in the imperial system
    (feet, inches, fraction of an inch) into the specified unit
    
    Parameters
    ----------
    value : str
        String representation of the imperial distance
    to_unit : str
        The desired (metric based) unit

    """
    split_on_inches = value.strip().split("''")
    # print("split_on_inches : %s" % str(split_on_inches))
    # print("split_on_inches[0].split(''') : %s" % str(split_on_inches[0].split("'")))
    if len(split_on_inches[0].split("'")) == 2:
        feet = float(split_on_inches[0].split("'")[0])
    elif len(split_on_inches[0].split("'")) == 1:
        feet = 0.
    else:
        raise ValueError

    # print("feet : %f" % feet)
    if "'" in split_on_inches[0]:
        inches_int = int(split_on_inches[0].split("'")[1])
    else:
        inches_int = int(split_on_inches[0])
    # print("inches_int : %s" % str(inches_int))
    if len(split_on_inches) == 2 and split_on_inches[1] != "":
        inches_frac = float(Fraction(split_on_inches[1]))
    else:
        inches_frac = 0.
    # print("inches_frac : %s" % str(inches_frac))
    inches_float = inches_int + inches_frac

    return convert_imperial(feet=feet, inches=inches_float, to_unit=to_unit)


def convert_imperial(feet=0., inches=0., to_unit="mm"):
    r"""Convert a distance expressed in the imperial system
    (feet, inches, fraction of an inch) into the specified unit
    
    Parameters
    ----------
    feet : float
        Feet
    inches : float
        Inches
    to_unit : str
        The desired (metric based) unit

    """
    return convert(feet, from_unit="feet", to_unit=to_unit) + convert(inches, from_unit="inches", to_unit=to_unit)


if __name__ == "__main__":
    print(convert_imperial(feet=1., inches=2.5, to_unit="mm"))
    print(convert_imperial_str(value="1'2''1/2", to_unit="mm"))

    print(convert_imperial(feet=1., inches=2, to_unit="mm"))
    print(convert_imperial_str(value="1'2''", to_unit="mm"))

    print(convert_imperial(feet=1., inches=2.625, to_unit="mm"))
    print(convert_imperial_str(value="1'2''5/8", to_unit="mm"))

    print(convert_imperial(feet=0., inches=1., to_unit="mm"))
    print(convert_imperial_str(value="1''", to_unit="mm"))

    print(convert_imperial(feet=0., inches=1.5, to_unit="mm"))
    print(convert_imperial_str(value="1''1/2", to_unit="mm"))
