import glob
import os.path

from PIL import Image, ImageDraw


def process(png: str):
    img = Image.open(png)
    img = img.convert("RGBA")

    ImageDraw.floodfill(img, xy=(0, 0), value=(0, 0, 0, 0), thresh=726)

    img.save(os.path.join("images", os.path.basename(png)))


if __name__ == "__main__":
    for png in glob.glob("raw/*.png"):
        process(png)
