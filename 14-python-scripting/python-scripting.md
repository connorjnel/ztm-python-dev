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
- Set email body and structure using EmailMessage object, then do smtp connection with host and port as well as credentials
- Can use email templates when doing emails
- `from string import Template` - Substitute variables inside text, ie string interpolation in emails, handy
- `from pathlib import Path` - Basic IO module, kinda like OS
- `Template(Path("index.html").read_text())` - import file as text with pathlib and as a template for use with template
- TIP - Start using pathlib instead instead of OS, more friendly
- When using set content and substitute need to set content type to HTML

## Password Checker

- `pip install requests` - import for simple http requests
- Always save passwords hashed
- `import hashlib` - built in py library for hashing, read doc when using, complicated
- Tip - `sys.argv[1:]` - accept multiple arguments
- Tip - `sys.exit()` - exits file once done

### Hash Function

- Function that generates a value of fixed length for each input it gets.
- Used in hash tables, advanced data structure
- The most common hash functions used in digital forensics are Message Digest 5 (MD5), and Secure Hashing Algorithm (SHA) 1 and 2.

## Twitter Bot

- Skipped because api wanted phone number, NFW, copied project code and watched instructions but not tested
- Use tweepy library

## SMS with PY

- Use twilio for SMS, voice etc
- `pip3 install twilio` - twilio library, not standard
- Despise twilio, cant login because I tried to login? WTF
- Again unable to test, watched instructions, think I dislike API's now purely because of Twitter and Twilio being AHOLES
- Twilio has code for dif langauges pre written, just need to grab auth details and plug them in
- Free account is limited but good enough for testing
- Can call the twilio function as a module in another function, ie have a function checking the web for something then send a message using twilio once condition is met, very cool but still, hate twilio and their dumb auth errors
- When you are using library, api for the first time, google it, check documentation, if your stuck stack overflow, test and make it work
