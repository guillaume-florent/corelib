# coding: utf-8

r"""Procedures parallelization"""

import logging
import time
from itertools import product
from multiprocessing import Process
from corelib.core.computer import number_of_cores

logger = logging.getLogger(__name__)


def chunks(l, n):
    """Yield successive n-sized chunks from l.

    Parameters
    ----------
    l : list
        The list to split in_ chunks
    n : int
        The target numbers of items in_ each chunk

    Returns
    -------
    list
        List of chunks

    """
    pieces = []
    for i in range(0, len(l), n):
        pieces.append(l[i:i + n])
    return pieces


def nb_per_process(cases_len):
    r"""Target number of 'cases' per process that optimizes parallelization

    Parameters
    ----------
    cases_len : int
        Total number of cases to deal with

    Returns
    -------
    Target number of cases by process

    """
    # print("Computer has %i CPUs" % number_of_cpus())
    msg = "Computer has %i cores" % number_of_cores()
    logger.info("Computer has %i cores" % number_of_cores())

    if cases_len % number_of_cores() == 0:
        return int(cases_len / number_of_cores())
    else:
        return int(cases_len / number_of_cores() + 1)


def parallel_run(iter_func, atomic_func, iter_args, args):
    r"""Launch a parallel run
    
    Parameters
    ----------
    iter_func : callable
        Function that deals with the iteration over the cases.
        This is the function that could be directly used with the list of all
        cases if no parallelization was intended.
    atomic_func : Callable
        Procedure that actually does something for a case
    iter_args : list[list]
        List of lists of possible values of the case defining params
    args : list
        Other args

    """
    all_cases = list(product(*iter_args))
    cases_decomposition = chunks(all_cases, nb_per_process(len(all_cases)))
    msg = "Decomposed in %i parts" % len(cases_decomposition)
    logger.info(msg)

    for i, cases_partial in enumerate(cases_decomposition):
        msg = "  #%i -> %i cases" % (i, len(cases_partial))
        logger.info(msg)

    processes = []

    for i, cases_partial in enumerate(cases_decomposition):
        p = Process(target=iter_func, args=(atomic_func, cases_partial, args, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


def __sample_iter_func(atomic_func, cases, other_args, process_nb=-1):
    r"""Sample iteration function
    
    Parameters
    ----------
    atomic_func : callable
    cases : list
    other_args : list
    process_nb : int

    """
    for j, case in enumerate(cases):
        msg = "%s [process %i - %i out of %i]" % (str(case),
                                                  process_nb,
                                                  j + 1,
                                                  len(cases))
        print(msg)
        t0 = time.time()
        try:
            atomic_func(case, *other_args)
        except:
            msg = "Something went wrong while running %s" % atomic_func.__name__
            print(msg)
        t1 = time.time()

        msg = "%s took %.4f minutes" % (str(case), (t1 - t0) / 60)
        print(msg)


def __sample_atomic_func(case, p1, p2, p3="Z"):
    r"""Sample 'atomic' procedure that actually does something with a case
    
    Parameters
    ----------
    case : tuple
    p1 : whatever, specific to this function
    p2 : whatever, specific to this function
    p3 : whatever, specific to this function"""
    l = []

    # here the function can handle a case with any number of params,
    # which may not always be so
    for param in case:
        l.append(param)
    l.append(p1)
    l.append(p2)
    l.append(p3)
    print(''.join(l))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s :: %(levelname)6s :: %(module)20s '
                               ':: %(lineno)3d :: %(message)s')
    l1 = ['a', 'b', 'c', 'd']
    l2 = ['1', '2', '3', '4']
    l3 = ['+', '-', '*', '/']

    parallel_run(iter_func=__sample_iter_func,
                 atomic_func=__sample_atomic_func,
                 iter_args=[l1, l2, l3],
                 args=['lorem', "ipsum", "dolor"])
