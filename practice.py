# python version in pipenv shell is 3.6.5

from PIL import Image, ImageDraw, ImageFont
import random
import pprint
import json

with open('white_cards.json') as f:
  cards = json.load(f)

print(cards)