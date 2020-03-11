import json
import random
import tweepy
import secrets
import os

# twitter auth stuff
auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)
api = tweepy.API(auth)

with open('black_cards.json') as f:
  black_cards = json.load(f)

# finds the total number of questions in the black cards json
total_questions = len(black_cards["blackCards"])

# Works to choose a string from the black cards json
question = (black_cards["blackCards"][random.randrange(total_questions)]["text"])

# successfully tweets a question!
# api.update_status(question)

# upload media to twitter?
media_object = api.media_upload("/Users/carlislefujiyoshi/Documents/bottybots/casm/subtitled/new2.jpg")
api.update_status(question, media_ids=[media_object.media_id])