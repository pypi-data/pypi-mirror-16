# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup, find_packages
import unittest

import optimove

setup(
    name='optimove',
    version=optimove.__version__,
    packages=find_packages(),
    author='Nicolas RAMY',
    author_email='nicolas.ramy@darkelda.com',
    license='MIT',
    description='',
    long_description=open('README.md').read(),
    include_package_data=True,
    test_suite='tests',
    url='http://github.com/nicolas-ramy/optimove',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7'
    ],
)
