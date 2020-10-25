#!/usr/bin/env python
# coding: utf-8


import tweepy
import csv
import pandas as pd

consumer_key = '#####################'
consumer_secret = '##################################################'
access_token = '##############################################'
access_token_secret = '#############################################'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('14-10-2020.csv', 'a') #
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#covid19",
                           lang="en",
                           since="2020-10-14", until = "2020-10-15").items(2600):
    print (tweet.created_at)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.retweet_count,
                        tweet.id_str.encode('utf-8'),tweet.user.name.encode('utf-8'),tweet.user.id_str.encode('utf-8')])

