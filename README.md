
![Banner art depicting Zenitsu](/assets/images/banner.jpg)

Webpage is live at https://adityadraws.github.io

------------------

Hello! You're looking at the source code to generate my art gallery!

#### How this gallery is periodically updated:

build_gallery.py takes full responsibility of this, and proceeds as follows -

- Parses periodic data backups from instagram per the specified dir
- Iterates over subfolders and images
- Resizes each image to 4:3 aspect ratio by encapsulating additional black pixels - this is done to normalize different image resolutions
- Generates full HD versions and thumbnail versions of the image and places them in the assets dir
- Generates the post.md file, adding the image to the gallery
- Repeat for other images

The site has been left un-optimized for mobile intentionally, but feel free to zoom in ✨
