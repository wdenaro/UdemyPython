# https://pypdf2.readthedocs.io/en/3.0.0/user/migration-1-to-2.html#imports-and-modules
"""
Pass the script filenames of pdf files to combine them into a super.pdf
> python3 pdf.py dummy.pdf twopage.pdf
"""

import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):

    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)
