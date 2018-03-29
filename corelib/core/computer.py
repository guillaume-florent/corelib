# -*- coding: utf-8 -*-

r"""Machine related data"""

import psutil
import platform
import multiprocessing


def physical_memory():
    r"""Total physical memory

    Returns
    -------
    int : total memory in bytes

    """
    mem = psutil.virtual_memory()
    return mem.total


def processor():
    r"""CPU description

    Returns
    -------
    str

    """
    return platform.processor()


def number_of_cpus():
    r"""Number of CPUs

    Returns
    -------
    int

    """
    return multiprocessing.cpu_count() / 2


def number_of_cores():
    r"""Number of cores for the CPU

    Returns
    -------
    int

    """
    return psutil.cpu_count(logical=False)


def number_of_threads():
    r"""Number of threads for the CPU

    Returns
    -------
    int

    """
    # return multiprocessing.cpu_count()
    return psutil.cpu_count(logical=True)