import PyPDF2
import sys
import os

# with open("dummy.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise((90))
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("tilt.pdf", "wb") as new_file:
#         writer.write(new_file)

# Create PDF merger script
# use sys and argv,
# also import os cuz it could be handy

# inputs = sys.argv[1:]


# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write("super.pdf")


# pdf_combiner(inputs)

# watermark all pages of a specified file

from pathlib import Path
from typing import Union, Literal, List
from PyPDF2 import PdfWriter, PdfReader


def stamp(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(stamp_pdf)
    image_page = reader.pages[0]

    writer = PdfWriter()

    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox
        content_page.merge_page(image_page)
        content_page.mediabox = mediabox
        writer.add_page(content_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)


stamp("super.pdf", "wtr.pdf", "super2.pdf")
