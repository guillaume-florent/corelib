#!/usr/bin/env python
# coding: utf-8

r"""Computer info retrieval example"""

from __future__ import print_function

from corelib.core.computer import physical_memory, processor, number_of_cores, \
    number_of_threads

print("Physical memory : %i bytes" % physical_memory())
print("      Processor : %s" % processor())
print("       Nb cores : %i" % number_of_cores())
print("      Nb threads: %i" % number_of_threads())
