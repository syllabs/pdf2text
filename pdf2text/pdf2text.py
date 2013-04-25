#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import re
from cStringIO import StringIO

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

class Extractor(object):
    def __init__(self,
            password='',
            encoding='utf-8',
            normalize_spaces=True,
            caching=True,
            detect_vertical=True,
            char_margin=1.0,
            line_margin=0.3,
            word_margin=0.3):
        """PDF Text extractor

        password: password for password protected file
        encoding: expected encoding
        normalize_spaces: convert multiple spaces to a single space
        caching: activate PDFMIner object caching
        detect_vertical: detect vertical text

        For more details about the options, see:
            http://www.unixuser.org/~euske/python/pdfminer/index.html

        """
        self.password = password
        self.encoding = encoding

        self.normalize_spaces = normalize_spaces

        self.caching = caching

        self.laparams = LAParams()
        self.laparams.detect_vertical = detect_vertical
        self.laparams.char_margin = char_margin
        self.laparams.line_margin = line_margin
        self.laparams.word_margin = word_margin


    def __call__(self, stream):
        """Extract text from input stream"""
        # Prepare pdf extraction
        outfp = StringIO()
        rsrcmgr = PDFResourceManager(caching=self.caching)
        device = TextConverter(
                rsrcmgr,
                outfp,
                codec=self.encoding,
                laparams=self.laparams,
        )

        # Extract text
        process_pdf(
                rsrcmgr,
                device,
                stream,
                set(), # pagenos
                maxpages=0,
                password=self.password,
                caching=self.caching,
                check_extractable=True,
        )

        # Output
        text = outfp.getvalue()
        outfp.close()
        if self.normalize_spaces:
            return re.sub(r'  +', ' ', text)
        else:
            return text

def main():
    import sys

    if len(sys.argv) < 2:
        sys.stderr.write(' usage: pdf2text.py <pdffiles...>\n')
        exit(1)

    extract = Extractor()
    for fname in sys.argv[1:]:
        with open(fname, 'rb') as stream:
            print extract(stream)

if __name__ == '__main__':
    main()

