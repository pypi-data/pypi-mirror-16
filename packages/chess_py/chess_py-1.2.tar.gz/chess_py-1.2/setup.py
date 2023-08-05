#!/usr/bin/env python

from setuptools import setup

setup(name='chess_py',
      version='1.2',
      description='Python chess client',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
      ],
      author='Aubhro Sengupta',
      author_email='aubhrosengupta@gmail.com',
      url='https://github.com/LordDarkula/chess_py',
      license='MIT',
      packages=['chess_py', 'chess_py.core', 'chess_py.core.algebraic', 'chess_py.game', 'chess_py.pieces',
                'chess_py.players'],
      )
