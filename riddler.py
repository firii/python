#!/usr/bin/env python3

from PIL import Image, ImageDraw
from math import floor
from sys import argv

width = int(argv[1])

img = Image.new("RGB", (400, 200), (50, 50, 50))

ctx = ImageDraw.Draw(img)

for i in range(0, 136):
	temp = Image.open("parts/op-" + str(i) + ".jpg")
	x = (i % width)*10
	y = floor(i / width)*10
	ctx.bitmap([x, y], temp)
	pass

img.save("solved.png")


