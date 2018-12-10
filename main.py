import os
import pandas as pd
import tweepy
from collections import defaultdict

FILENAME = 'tweets.csv'


def count_word(row, word):
    if word in row['text'].lower():
        return 1
    return 0


def env(key):
    return os.environ[key]

auth = tweepy.OAuthHandler(env('TWITTER_CONSUMER_KEY'), env('TWITTER_CONSUMER_SECRET'))
auth.set_access_token(env('TWITTER_ACCESS_TOKEN'), env('TWITTER_ACCESS_TOKEN_SECRET'))

api = tweepy.API(auth)

data = defaultdict(list)

for tweet in tweepy.Cursor(api.user_timeline, screen_name='@rerb', count=3200, tweet_mode='extended').items():
    data['id'].append(tweet.id)
    data['created_at'].append(tweet.created_at)
    data['text'].append(tweet.full_text)
    data['retweet_count'].append(tweet.retweet_count)
    data['favorite_count'].append(tweet.favorite_count)

df = pd.DataFrame.from_dict(data).set_index('id', drop=False)

df['tweet_mentionne_excuse'] = df.apply(lambda row: count_word(row, 'excuse'), axis=1)
df['tweet_mentionne_regulation'] = df.apply(lambda row: count_word(row, 'régulation'), axis=1)
df['tweet_mentionne_bon_courage'] = df.apply(lambda row: count_word(row, 'bon courage'), axis=1)

csv = pd.read_csv(FILENAME, parse_dates=['created_at']).set_index('id', drop=False)

csv = csv.append(df)
csv.drop_duplicates(
    subset=['id'],
    keep='last',
    inplace=True
)
csv.sort_values(by='created_at', inplace=True)

csv.to_csv(FILENAME, index=False)
