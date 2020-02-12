import json
import random

with open('black_cards.json') as f:
  black_cards = json.load(f)

# Works to choose a string from the black cards json
# 67 is the number of black card questions, should un-hardcode the number lol
question = (black_cards["blackCards"][random.randrange(67)]["text"])
