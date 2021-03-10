#!/usr/bin/env python

# from distutils.core import setup
# from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup

setup(
    packages=['rosdoc_lite'],
    package_dir={'': 'src'},
    scripts=['scripts/rosdoc_lite'],
    package_data={'rosdoc_lite': ['templates/*']}
)

# setup(**d)
