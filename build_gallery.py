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

        destination_thumbnail = THUMB_ROOT + '\\' + output_filename
        destination_full      = FULL_ROOT + '\\' + output_filename
        source_image          = path_to_folder + '\\' + image_filename

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

        if not dry_run:
            new_post.close()
            
        print('Generating with content:')
        print(content)
        post_num += 1


print('Success!')
