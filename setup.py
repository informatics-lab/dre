#!/usr/bin/env python

from distutils.core import setup

setup(name='dre',
      version='0.1',
      install_requires=[
          "datapoint"
      ],
      description='Decision Recommendation Engine',
      long_description='''
Decision Recommendation Engine
''',
      author='Rachel Prudden',
      author_email='rachel.prudden@informaticslab.co.uk',
      maintainer='Rachel Prudden',
      maintainer_email='rachel.prudden@informaticslab.co.uk',
      url='https://github.com/met-office-lab/dre',
      license='TBC',
      packages=['dre'],
      classifiers=[
          'Programming Language :: Python :: 2.7',
      ]
     )