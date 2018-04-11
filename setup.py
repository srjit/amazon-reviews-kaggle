#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages


__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


install_requires = [
    'tensorflow',
    'pandas',
    'numpy',
    'tqdm',
    'gensim',
]


setup(
      name='amazon-reviews-kaggle',
      version='0.0.1',
      description='LSTM model for sentiment analysis on amazon product reviews',
      author='Sreejith Sreekumar',
      author_email='sreekumar.s@husky.neu.edu',
      url='https://github.com/srjit/amazon-reviews-kaggle',
      license='MIT',
      install_requires=install_requires,
      packages=find_packages()
)

