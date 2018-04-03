#!/usr/bin/env python
# coding: utf-8**

"""setuptools based setup module for corelib"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
import codecs
from os import path

import corelib

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name=corelib.__name__,
    version=corelib.__version__,
    description=corelib.__description__,
    long_description=long_description,
    url=corelib.__url__,
    download_url=corelib.__download_url__,
    author=corelib.__author__,
    author_email=corelib.__author_email__,
    license=corelib.__license__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='',
    packages=['corelib',
              'corelib.core',
              'corelib.geometry',
              'corelib.testing',
              'corelib.units'],
    install_requires=['numpy', 'scipy', 'matplotlib', 'jinja2', 'psutil'],
    extras_require={
        'dev': [],
        'test': ['pytest', 'coverage'],
    },
    package_data={},
    data_files=[],
    entry_points={}
    )
