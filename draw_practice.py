# python version in pipenv shell is 3.6.5

from PIL import Image, ImageDraw, ImageFont
import random
import pprint
import json
import textwrap

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

draw = ImageDraw.Draw(lolpic)
font = ImageFont.truetype('Verdana.ttf', size=18)
 
# starting position of the message
# x is starting position from the left
# y is starting position from the bottom
# x = 30
# y = height-50
white_fill = 'rgb(255, 255, 255)' # white color
black_fill = 'rgb(0, 0, 0)' # black color
yellow_fill = 'rgb(255, 255, 0)' # yellow color
 
# answer_size = draw.textsize(answer)[0]

# breaking up longer answers into multiple lines
text_block = textwrap.wrap(answer, width=45)

# draw the message on the background
current_height = height-75
pad = 10
for line in text_block:
  w, h = draw.textsize(line, font=font)
  # fake out the black outline behind the yellow text
  draw.text((((width - w)/2)-2, current_height-2), line, fill=black_fill, font=font)
  draw.text((((width - w)/2)-2, current_height+2), line, fill=black_fill, font=font)
  draw.text((((width - w)/2)+2, current_height-2), line, fill=black_fill, font=font)
  draw.text((((width - w)/2)+2, current_height+2), line, fill=black_fill, font=font)
  # draw the yellow text
  draw.text(((width - w)/2, current_height), line, fill=yellow_fill, font=font)
  current_height += (h+pad)
 
# save the edited image
lolpic.save('newboop.jpg')