#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='model_doctor',
    version='0.0.0',
    description='To monitor the health of the model_doctor performance constantly',
    author='Adel Rahimi',
    packages=find_packages(),
    package_data={'': ['*.png']},
    install_requires=[],
)
