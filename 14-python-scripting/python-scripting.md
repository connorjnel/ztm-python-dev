# Python Scripting

Allows you to run tasks easily using python, image processing, checking password

## Developer Fundamentals

- Pick the right library - check for ones with lots of git stars, forks. Check for security issues

## PIL / Pillow - Image Processing

- `pip install Pillow` - install pillow
- `from PIL import Image` - initial import
- `Image.open("path")` - Load image
- `img.filter(ImageFilter.BLUR)` - Add filter, remember to import ImageFilter
- `img.save("name", "format")` = Save image
- With filters save as PNG instead of JPEG
- `Image.show()` - Opens image, mainly for debugging
- `img.rotate(90)` - rotate image
- `img.resize((300,300))` - resize image, has to be tuple
- `img.crop(crop-tuple)` - crop image, has seperate box model for crop as a tuple, can input the crop box directly as a tuple ie `img.crop((5,5,5,5))`
- `img.thumbnail((400,400))` - Creates thumbnail with size specified, doesnt return new image so dont save to var
- os library from py very useful, basically powerful IO
- opencv - deals with computer vision, can analyze images

## PyPDF2 - PDF processing

- `pip install PyPDF2==1.26` - Version used for course
- `import PyPDF2` - standard import
- `PyPDF2.PdfFileReader(file)` - read pdf file
- When using `with open` on pdf files add `"rb"` as mode so it opens it in binary mode
- `writer = PyPDF2.PdfFileWriter()` - create a pdf writer
- Tip - `inputs = sys.argv[1:]` - grab all sys arguments as a list
- `merger.append(pdf)` - very simple way to combine pdfs
- clean syntax for open file `template = PyPDF2.PdfFileReader(open("super.pdf", "rb"))`
- `getNumPages` - method to get page count, useful for looping
- `merge_page` - use for watermarking in a loop

## Email Module - Email processing

- `import email` - standard library import, no install
- `import smtplib` - smtp library, create smtp server
- Dont save passwords in the clear on repos
