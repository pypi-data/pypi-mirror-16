#!/usr/bin/env python3
"""
Ark
===

Ark is a static website generator in Python. It transforms a directory of
text files into a self-contained website that can be viewed locally or
served remotely.

* `Documentation <http://mulholland.xyz/docs/ark/>`_
* `Sample Site <http://ark.mulholland.xyz/phoenix/>`_
* `Github Homepage <https://github.com/dmulholland/ark>`_

"""

import os
import re
import io

from setuptools import setup, find_packages


# MANIFEST.in file content.
manifest = """\
include license.txt readme.md
recursive-include ark/ini *
recursive-include ark/ext *
"""


# Write a temporary MANIFEST.in file alongside the setup.py file.
manpath = os.path.join(os.path.dirname(__file__), 'MANIFEST.in')
with io.open(manpath, 'w', encoding='utf-8') as manfile:
    manfile.write(manifest)


# Load the package's metadata into the meta dict.
metapath = os.path.join(os.path.dirname(__file__), 'ark', 'meta.py')
with io.open(metapath, encoding='utf-8') as metafile:
    regex = r'''^__([a-z]+)__ = ["'](.*)["']'''
    meta = dict(re.findall(regex, metafile.read(), flags=re.MULTILINE))


# Standard setup routine.
setup(
    name = 'ark',
    version = '2.0.1',
    packages =  find_packages(),
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'ark = ark.main:main',
        ],
    },
    install_requires = [
        'markdown >= 2.6.6, < 3.0.0',
        'pygments >= 2.1.3, < 3.0.0',
        'pyyaml >= 3.11, < 4.0',
        'jinja2 >= 2.8, < 3.0',
        'syntex >= 0.13.0, < 0.14.0',
        'ibis >= 1.5.0, < 2.0.0',
        'shortcodes >= 2.1.0, < 3.0.0',
        'libclio >= 2.0.0, < 3.0.0',
    ],
    author = 'Darren Mulholland',
    url='https://github.com/dmulholland/ark',
    license = 'Public Domain',
    description = 'A static website generator.',
    long_description = __doc__,
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: Public Domain',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)


# Delete the temporary MANIFEST.in file.
if os.path.isfile(manpath):
    os.remove(manpath)
