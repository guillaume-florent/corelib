# coding: utf-8

r"""Python code related tools"""

import ast
import sys


def py3():
    r"""Determine if runtime is Python3

    Returns
    -------
    bool

    """
    if sys.version_info > (3, 0):
        return True
    else:
        return False


def is_valid_python(code):
    r"""Checks that a string is valid Python code

    Parameters
    ----------
    code : str
        The Python code as a string

    Returns
    -------
    bool
        True if the code is valid, False otherwise

    """
    try:
        ast.parse(code)
    # except SyntaxError as se:
    #     raise se
    except SyntaxError:
        return False
    return True


def init_from_args(being_inited):
    """Initializes attributes of 'being_inited' to a name and value
    equal to the __init__ function parameters.
    It is mostly used to avoid having to write:
    def __init__(self, param1=value1, param2=value2, ....):
        self.param1 = value1
        self.param2 = value2
        ....

    and to (simply) write:

    def __init__(self, param1=value1, param2=value2, ....):
        init_from_args(self)

    instead.
    """
    # import ipdb
    # ipdb.set_trace()

    # Works only in Python 2, not in Python 3
    # code_object = being_inited.__class__.__init__.im_func.func_code

    code_object = being_inited.__class__.__init__.__code__
    for k, v in sys._getframe(1).f_locals.items():
        if k != 'self' \
           and k in code_object.co_varnames[1:code_object.co_argcount]:
            setattr(being_inited, k, v)
