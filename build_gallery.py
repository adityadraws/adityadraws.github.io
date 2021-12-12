from os      import listdir
from os.path import isfile, join
from shutil  import copyfile

import os
import json

DIRFILE = open('directories.json')
DIRS = json.load(DIRFILE)
DIRFILE.close()

POST_CONTENT = '''---
title: {}
image: {}
thumbnail: {}
caption: {}
---
'''
ROOT = DIRS['root']
THUMB_ROOT = DIRS['thumbs']
FULL_ROOT = DIRS['fulls']
POST_ROOT = DIRS['post']

# TODO: Change ROOT to newest path of instagram data-download
dated_folders = os.walk(ROOT)

dry_run = False

im = r'C:\Users\gayat\Desktop\Instagram data backups\adityadraws_20211212\media\posts\202106\200509058_3047549632142829_5999638296946235673_n_18135034312168803.jpg'

def resize(image):
    from PIL import Image, ImageOps
    from math import ceil
    img = Image.open(image)
    print(img.width, img.height)

    # If it is not 4:3, make it 4:3 ratio first by adding borders
    # then resize to 1200:750

    w = img.width
    h = img.height
    new_h = h
    new_w = w
    if w > h:
        new_h = 3/4 * w
    if w <= h:
        new_w = 4/3 * h

    horizontal_border = new_w - w
    vertical_border = new_h - h

    up = ceil(vertical_border/2)
    down = ceil(vertical_border/2)
    left = ceil(horizontal_border/2)
    right = ceil(horizontal_border/2)
    print(left, up, right, down)
    #new_img = ImageOps.expand(img, (up, right, down, left), fill = 'black')
    new_img = ImageOps.expand(img, (left, up, right, down), fill = 'black')
    size = (1200, 800)
    new_img.save(image)


for folder in dated_folders:
    path_to_folder = folder[0]

    if path_to_folder == ROOT:
        continue

    '''
    Enter into this folder.
    Copy every image and move it to blog's thumbnail + full
    Create a new md post for this and add the path + title
    Title can be date and post number
    YYYMM#<PostNo>
    '''

    images = [f for f in listdir(path_to_folder) if isfile(join(path_to_folder, f)) and (f.endswith('.jpg') or f.endswith('png') or f.endswith('jpeg'))]
    post_num = 1
    for image_filename in images:
        # time_of_posting  = 'YYYYMM'
        time_of_posting    = path_to_folder.split('\\')[-1]

        # 'YYYYMM Art#X'
        output_image_title = time_of_posting + ' Art#' + str(post_num)
        output_filename    = time_of_posting + '_' + str(post_num)

        destination_thumbnail = THUMB_ROOT + '\\' + output_filename + '.jpg'
        destination_full      = FULL_ROOT + '\\' + output_filename + '.jpg'
        source_image          = path_to_folder + '\\' + image_filename
        resize(source_image)

        print('Copying', source_image, 'to', destination_thumbnail)
        print('Copying', source_image, 'to', destination_full)
        if not dry_run:
            copyfile(source_image, destination_thumbnail)
            copyfile(source_image, destination_full)

        new_post_filepath = POST_ROOT + '\\' + output_filename + '.md'

        print('Creating file:', new_post_filepath)
        new_post = None
        if not dry_run:
            new_post = open(new_post_filepath, 'w')

        content_image_path = 'assets/images/fulls/' + output_filename + '.jpg'
        content_thumbnail_path = 'assets/images/thumbs/' + output_filename + '.jpg'
        content = POST_CONTENT.format(output_image_title, content_image_path, content_thumbnail_path, '')
        new_post.write(content)
        
        if not dry_run:
            new_post.close()
            
        print('Generating with content:')
        print(content)
        post_num += 1


print('Success!')
