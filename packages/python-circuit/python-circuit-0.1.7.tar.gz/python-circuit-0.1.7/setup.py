#!/usr/bin/env python
from setuptools import setup

with open('README.md') as f:
    long_description = f.read().strip()

setup(name='python-circuit',
      version='0.1.7',
      description='Simple implementation of the Circuit Breaker pattern',
      long_description=long_description,
      author='Edgeware',
      author_email='info@edgeware.tv',
      url='https://github.com/edgeware/python-circuit',
      packages=['circuit'],
      test_suite='circuit.test',
      tests_require=[
          'mockito == 0.5.2',
          'Twisted >= 10.2'
      ])
