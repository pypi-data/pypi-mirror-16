#!/usr/bin/env python

from setuptools import setup
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='noodles',
    version='0.2.1',
    long_description=long_description,
    description='Workflow Engine',
    author='Johan Hidding',
    author_email='j.hidding@esciencecenter.nl',
    url='https://github.com/NLeSC/noodles',
    packages=[
        'noodles', 'noodles.serial', 'noodles.run', 'noodles.run.xenon',
        'noodles.display',
        'noodles.interface', 'noodles.workflow', 'noodles.files',
        'noodles.prov'],

    classifiers=[
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Distributed Computing'],

    install_requires=[],
    extras_require={
        'prov': ['tinydb'],
        'xenon': ['pyxenon'],
        'test': ['nose', 'coverage', 'pyflakes', 'pep8', 'docker-py']
    },
)
