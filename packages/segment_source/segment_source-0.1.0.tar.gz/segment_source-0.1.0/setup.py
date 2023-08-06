from setuptools import setup
import os

setup(
    name='segment_source',
    packages=['segment_source'],
    version='0.1.0',
    description='Python source client',
    author='Segment',
    author_email='friends@segment.com',
    url='https://github.com/segmentio/python-source',
    install_requires=[
        'simplejson==3.8.2',
        'grpcio==0.15.0'
    ]
)
