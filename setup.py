#!/usr/bin/env python
# -*- coding: latin-1 -*-
import codecs
import os

from setuptools import setup, find_packages

from pylodemd import __version__


def open_local(paths, mode='r', encoding='utf8'):
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        *paths
    )
    return codecs.open(path, mode, encoding)


with open_local(['README.rst'], encoding='utf-8') as readme:
    long_description = readme.read()

with open_local(['requirements.txt']) as req:
    install_requires = req.read().split("\n")

setup(
    name='pyLODEmd',
    packages=find_packages(),
    package_dir={'pylodemd': 'pylodemd', 'img': 'img'},
    package_data={
        'pylodemd': ['templates/*.html', 'templates/*/*.html', 'templates/*.md', 'templates/*/*.md', 'style/*.css'],
        'img': ['pyLODE-250.png']
    },
    version=__version__,
    use_scm_version={'write_to': 'pylodemd/_version.py'},
    description='An OWL ontology Markdown documentation tool forked from pyLODE v2.13.3 (https://github.com/RDFLib/pyLODE/releases/tag/2.13.3).',
    author='Ashley Caselli',
    author_email='ashley.caselli@unige.ch',
    url='https://github.com/ashleycaselli/pyLODE.md',
    license='LICENSE',
    keywords=['Semantic Web', 'OWL', 'ontology', 'template', 'Jinja2', 'documentation'],
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'pylodemd = pylodemd.cli:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/ashleycaselli/pyLODE.md/issues',
        'Source': 'https://github.com/ashleycaselli/pyLODE.md',
    },
    install_requires=install_requires,
    long_description_content_type="text/x-rst"
)
