import json
import random

with open('black_cards.json') as f:
  black_cards = json.load(f)

# finds the total number of questions in the black cards json
total_questions = len(black_cards["blackCards"])

# Works to choose a string from the black cards json
question = (black_cards["blackCards"][random.randrange(total_questions)]["text"])