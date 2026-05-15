import os

import tweepy

client = tweepy.Client(
    consumer_key=os.environ["TWTR_API_KEY"],
    consumer_secret=os.environ["TWTR_API_KEY_SECRET"],
    access_token=os.environ["TWTR_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWTR_ACCESS_TOKEN_SECRET"],
)
# Post "test"
response = client.create_tweet(text="test")
print(response)
