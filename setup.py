#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='pynessusrpc',
    author='Nadeem Douba',
    version='0.2',
    author_email='ndouba@gmail.com',
    description='Python Nessus RPC client.',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    install_requires=[],
    dependency_links=[]
)


