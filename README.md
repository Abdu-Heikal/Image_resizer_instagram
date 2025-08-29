# Image_resizer_instagram

This repository provides a small Python utility that helps prepare images for
Instagram's 5:4 aspect ratio. A file dialog is used to select one or more
images, each of which is placed on a white canvas so that the final result has
the correct ratio without cropping. The processed files are written to an
``edited`` subdirectory with an ``_edited`` suffix added to the original name.

## Usage

```bash
python image_resizer.py
```

After running the script, choose the images you want to process from the pop-up
window. Each resized copy will appear in an ``edited`` folder next to the
originals with ``_edited`` appended before the file extension.
