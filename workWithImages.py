#!/usr/bin/env python3
import os, sys
from PIL import image

size = (128, 128)

for file in os.listdir():
  fixed = os.path.splitext(file) [0]
  try:
  	with Image.open(file).convert('RGB') as im:
  		im.thumbnail(size)
  		im.rotate(270).save("/opt/icons/" + fixed, "JPEG")
  except OSError:
  	pass
