# JPG to PNG Converter
# First arg (folder-name, new folder)

# from sys first and second arg

# check is destination folder exists, if not create it

# loop through source folder, convert images to png


from PIL import Image
import sys
import os
import re

path = os.path.abspath(sys.argv[1])
dest_dir = os.path.abspath(sys.argv[2])

if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

if os.path.exists(path):
    for filename in os.listdir(path):
        if filename.endswith('.jpg'):
            image = Image.open(os.path.join(path, filename))
            image = image.resize((300, 300))
            pattern = r'(.*)\.'
            data = re.search(pattern, filename)
            image.save(f'{dest_dir}/{data.group(1)}.png',
                       optimize=True, quality=80)
else:
    print(f'Directory {path} does not exists')
