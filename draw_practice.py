# python version in pipenv shell is 3.6.5

from PIL import Image, ImageDraw, ImageFont

lolpic = Image.open('sailormoon.jpg')

draw = ImageDraw.Draw(lolpic)

font = ImageFont.truetype('Verdana.ttf', size=10)
 
# starting position of the message
 
(x, y) = (10, 10)
message = "BOOP"
# color = 'rgb(255, 255, 255)' # white color
color = 'rgb(0, 0, 0)' # black color

 
# draw the message on the background
 
draw.text((x, y), message, fill=color, font=font)
 
# save the edited image
 
lolpic.save('newboop.jpg')