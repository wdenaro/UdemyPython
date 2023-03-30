# https://pypdf2.readthedocs.io/en/3.0.0/user/migration-1-to-2.html#imports-and-modules
"""
Will watermark all pages of PDF
"""

import PyPDF2

template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
out_file = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    out_file.add_page(page)

    with open('watermarked_output.pdf', 'wb') as file:
        out_file.write(file)
