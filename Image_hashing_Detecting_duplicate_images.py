#detects duplicate images with different resolutions as well (so 'rb' in with open
# method will be different. so we need another library called imagehash)

import imagehash
import os
from PIL import Image #reading the image contents

directory = 'files/detect_duplicate_images'
hashsize = 8

imagehash_dict ={}

#make filepath, read filepaths using Image.open() ,hash the content
#then
for file in os.listdir(directory):
    filepath = os.path.join(directory, file)

    #read contents of image
    with Image.open(filepath) as img:
        image_hash = imagehash.average_hash(img, 8)

        image_hash = str(image_hash)

        if image_hash in imagehash_dict:
            print(f"Duplicate detected : {filepath}")
            print(f"Original file : {imagehash_dict[image_hash]}\n")

        else:
            imagehash_dict[image_hash] = filepath

