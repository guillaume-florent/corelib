# coding: utf-8

r"""Folder(s) operations"""

from __future__ import print_function

import logging
import os
import os.path
import shutil

logger = logging.getLogger(__name__)


def clear_folder(folder, delete_subdirs=False):
    r"""Delete the contents of a folder

    Parameters
    ----------
    folder : str
        The full path to the folder
    delete_subdirs : bool, optional
        Delete the subdirectories if True, default is False

    """
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                if delete_subdirs:
                    shutil.rmtree(file_path)
        except Exception as e:
            logger.error(e)
