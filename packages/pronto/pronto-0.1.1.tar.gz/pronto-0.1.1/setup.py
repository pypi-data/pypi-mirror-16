#!/usr/bin/env python
# released under the GNU General Public License version 3.0 (GPLv3)

from setuptools import setup, find_packages
import pronto

## SETUPTOOLS VERSION
setup(
    name='pronto',
    version=pronto.__version__,
    
    packages=find_packages(),
    
    py_modules=['pronto'],
    
    author= pronto.__author__,
    author_email= 'martin.larralde@ens-cachan.fr',

    description="Python frontend to ontologies - a library to parse, create, browse and export ontologies.",
    long_description=open('README.md').read(),
    
    install_requires=open('requirements.txt').read().splitlines(),
    extras_require = {
        'doc':  ['Sphinx', 'sphinx-rtd-theme']
    },

    include_package_data=True,

    url='http://github.com/althonos/pronto',

    classifiers=[
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Operating System :: OS Independent",
    ],

    license="GPLv3",

    keywords = ['Bio-Informatics', 'Ontology', 'OBO', 'Owl', 'convert', 'parse'],

)

