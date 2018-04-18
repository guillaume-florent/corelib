# coding: utf-8

r"""File and file path handling"""

import os.path
import sys

if sys.version_info > (3, 0):
    PY3 = True
else:
    PY3 = False


def path_from_file(file_origin, relative_path):
    r"""Builds an absolute path from a file using a relative path

    Parameters
    ----------
    file_origin : str
        Full / absolute path to he file from which the path is to be built
    relative_path : str
        The relative path from file_origin

    Returns
    -------
    str
        Absolute file path

    """
    # Check the file exists
    # assert os.path.isfile(file_origin)
    if not os.path.isfile(file_origin):
        msg = "The file_origin parameter refers to a path that does not exist"
        raise ValueError(msg)
    dir_of_file_origin = os.path.dirname(os.path.realpath(file_origin))
    return os.path.abspath(os.path.join(dir_of_file_origin, relative_path))


# Make it possible to use a shorter syntax
p_ = path_from_file


def is_binary(filename):
    """
    Return True if the given filename is binary, False otherwise.

    Parameters
    ----------
    filename : str
        Path to the file

    Raises
    ------
    EnvironmentError    if the file does not exist or cannot be accessed.

    Reference
    ---------
    http://bytes.com/topic/python/answers/21222-determine-file-type-binary-text
    on 6/08/2010

    """
    fin = open(filename, 'rb')
    try:
        CHUNKSIZE = 1024
        while 1:
            chunk = fin.read(CHUNKSIZE)

            if PY3:
                backslash_zero = '\0'.encode()
            else:
                backslash_zero = '\0'

            if backslash_zero in chunk:  # found null byte
                return True
            if len(chunk) < CHUNKSIZE:
                break  # done
    finally:
        fin.close()
    return False
