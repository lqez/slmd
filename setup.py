#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

setup(
    name='mdls',
    version='0.1.0',
    packages=find_packages(),
    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/mdls',
    description='Markdown list sorter',
    test_suite='mdls.test',
)
