# python version in pipenv shell is 3.6.5

from PIL import Image, ImageDraw, ImageFont
import random
import pprint
import json

# load white cards json
with open('white_cards.json') as boop:
  white_cards = json.load(boop)

# randomly choose white card
answer = (random.choice(white_cards["whiteCards"]))
print(answer)

# bring in image and get dimensions
lolpic = Image.open('sailormoon.jpg')
height = lolpic.size[1]
width = lolpic.size[0]

# number checks
# print(lolpic.size)
# print("height: " + str(height))
# print("width: " + str(width))

draw = ImageDraw.Draw(lolpic)
font = ImageFont.truetype('Verdana.ttf', size=36)
 
# starting position of the message
# x is starting position from the left
# y is starting position from the top
x = 30
y = height-50
# color = 'rgb(255, 255, 255)' # white color
color = 'rgb(0, 0, 0)' # black color

# draw the message on the background
draw.text((x, y), answer, fill=color, font=font)
 
# save the edited image
lolpic.save('newboop.jpg')