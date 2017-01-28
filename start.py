# Attempting to make a python app
# Connect to Twitter first

import tweepy

consumer_key = "vA5CAkZHk6m7SqsNiOfvA7z9H",
consumer_secret = "5cToCIIjtxR0KYatvLvRJD9Thg0KTlLcB1jO48b2mrtFIc3BsT",
access_token = "377650054-sP0r6om0WvtOWKxLz3XI7ZLybrUZRVkZ4GGwC3gG",
access_token_secret = "nNkkoywIXl0xRprxRDFAvnL8zIIlOJcH5wSAVfQqHzwFL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)