import json
import random

with open('black_cards.json') as f:
	black_cards = json.load(f)

with open('white_cards.json') as boop:
	white_cards = json.load(boop)

# Works to choose a string from the black cards json
print(black_cards["blackCards"][random.randrange(67)]["text"])

# Works to choose a string from the white cards json
print(random.choice(white_cards["whiteCards"]))