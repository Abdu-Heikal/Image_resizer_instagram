"""Resize images to 5:4 aspect ratio with white padding.

This script opens a file dialog to allow users to select one or more image
files. Each image is placed on a white background to match a 5:4 (width:height)
ratio without cropping the original content. The processed images are saved in
the same directory as the source files with an ``_edited`` suffix.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from PIL import Image
from tkinter import Tk, filedialog

RATIO = 5 / 4  # Desired aspect ratio (width / height)


def resize_with_padding(img: Image.Image, ratio: float = RATIO) -> Image.Image:
    """Return a copy of *img* centered on a white canvas with the given ratio.

    The original image is not scaled. Instead, a new canvas with a white
    background is created so that the resulting image has the requested aspect
    ratio. The original image is then pasted in the center of this canvas.
    """
    w, h = img.size
    if w / h > ratio:
        new_w = w
        new_h = int(round(w / ratio))
    else:
        new_h = h
        new_w = int(round(h * ratio))
    background = Image.new("RGB", (new_w, new_h), "white")
    offset = ((new_w - w) // 2, (new_h - h) // 2)
    background.paste(img, offset)
    return background


def process_images(paths: Iterable[Path]) -> None:
    """Process each image in *paths* and save a resized copy.

    The output file is saved in the same directory with ``_edited`` appended to
    the base name.
    """
    for path in paths:
        try:
            with Image.open(path) as img:
                edited = resize_with_padding(img)
                out_path = path.with_name(path.stem + "_edited" + path.suffix)
                edited.save(out_path)
                print(f"Saved {out_path}")
        except Exception as exc:  # pragma: no cover - best effort logging
            print(f"Failed to process {path}: {exc}")


def main() -> None:
    """Prompt the user for images and process them."""
    root = Tk()
    root.withdraw()  # Hide the main window
    file_types = [
        ("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),
        ("All files", "*.*"),
    ]
    selected = filedialog.askopenfilenames(title="Select images", filetypes=file_types)
    root.destroy()
    if not selected:
        print("No files selected.")
        return
    process_images(Path(p) for p in selected)


if __name__ == "__main__":
    main()
