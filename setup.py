#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

from setuptools import setup
import os

version = '1.0.0'

install_requires = [
    'PDFMiner',
]

entry_points="""
[console_scripts]
pdf2text = pdf2text.pdf2text:main
"""

setup(
        name='pdf2text',
        version=version,
        description="A PDFMiner wrapper to ease the text extraction from pdf files.",
        # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            "Programming Language :: Python",
        ],
        keywords=['pdf', 'pdf2text', 'pdftotext'],
        author='Jimmy Ma',
        author_email='ma@syllabs.com',
        url='https://github.com/syllabs/pdf2text',
        license='MIT/X',
        packages=['pdf2text'],
        install_requires=install_requires,
        entry_points=entry_points,
)
