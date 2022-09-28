# Python Scripting

Allows you to run tasks easily using python, image processing, checking password

## Developer Fundamentals

- Pick the right library - check for ones with lots of git stars, forks. Check for security issues

## Image Processing

- Image gets processed, compresses it, adds filter, crops image, creates a few different sizes
- Pillow - Image processing library

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
