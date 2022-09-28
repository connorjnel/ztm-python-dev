# Python Scripting

Allows you to run tasks easily using python, image processing, checking password

## Image Processing

- Image gets processed, compresses it, adds filter, crops image, creates a few different sizes
- Pillow - Image processing library

## Developer Fundamentals

- Pick the right library - check for ones with lots of git stars, forks. Check for security issues

## PIL / Pillow

- `pip install Pillow` - install pillow
- `from PIL import Image` - initial import
- `Image.open("path")` - Load image
- `img.filter(ImageFilter.BLUR)` - Add filter, remember to import ImageFilter
- `img.save("name", "format")` = Save image
- With filters save as PNG instead of JPEG
- `Image.show()` - Opens image, mainly for debugging
