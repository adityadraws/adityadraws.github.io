# adityadraws.github.io
Art gallery

## SOP for adding content

### To add a new image/video:
1. Duplicate an existing image/video, for eg.

For an image:
```
<div class="artwork-item" style="grid-column: span 3; grid-row: span 3;" onclick="openModal('image','assets/images/rei_firebreath.PNG')">
	<img src="assets/images/rei_firebreath_thumb.jpg" loading="lazy">
</div>
```

2. Set the grid size by modifying the `grid-column` and `grid-row` sizes.

3. Set the onclick image/video parameter in the onclick function call.

4. Use a compressed thumbnail for optimizing page load time.

You can compress thumbnails using Magick - an open source image editing CLI

```
magick.exe kai.PNG -resize 90% kai_thumb.jpg
```

Magick: https://imagemagick.org/script/download.php
Magick CLI wiki: https://imagemagick.org/script/magick.php