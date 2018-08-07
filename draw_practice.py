# python version in pipenv shell is 3.6.5

from PIL import Image, ImageDraw, ImageFont

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
message = "BOOP"
# color = 'rgb(255, 255, 255)' # white color
color = 'rgb(0, 0, 0)' # black color

# draw the message on the background
draw.text((x, y), message, fill=color, font=font)
 
# save the edited image
lolpic.save('newboop.jpg')