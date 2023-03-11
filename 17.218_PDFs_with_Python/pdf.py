# https://pypdf2.readthedocs.io/en/3.0.0/user/migration-1-to-2.html#imports-and-modules

import PyPDF2

with open('dummy.pdf', 'rb') as file:

    # print(file)

    reader = PyPDF2.PdfReader(file)

    # Returns total number of pages
    # print(len(reader.pages))

    # Returns useful page object data
    # print(reader.pages[0])

    # Rotate the PDF and write a new file
    page = reader.pages[0]
    #print(page.rotate(180))

    page.rotate(180)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)

    with open('upsidedown.pdf', 'wb') as new_file:
        writer.write(new_file)
