import tweepy
from zipfile import ZipFile
import os
import json
import time
import sys

def pre_clean():
    if not os.path.exists('tweet.json'):
        with ZipFile('archive.zip', 'r') as z:
            with open('tweet.json', 'wb') as f:
                f.write(z.read('data/tweet.js')[25:])

def post_clean(tweets, number):
    tweets = tweets[number:]
    with open('tweet.json', 'w') as outfile:
        outfile.write(json.dumps(tweets , sort_keys=False, indent=2))

def loadTweets():
    with open('./tweet.json', errors="ignore") as f:
        tweets = json.load(f)
    
    return tweets

def printTweet(tweet):
    print("Tweet: "+ tweet['tweet']['full_text'])
    print(tweet['tweet']['retweet_count'] + ' Retweets || ' + tweet['tweet']['favorite_count'] + " Likes || Date: " + tweet['tweet']['created_at'])
    print('______________________________________________________________ \n')

def auth():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    bearer_token = ""

    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key, 
        consumer_secret=consumer_secret,
        access_token=access_token, 
        access_token_secret=access_token_secret
    )

    return client

def deleteTweets(tweets, number_to_delete, oauth):

    count = 0
    for tweet in tweets:

        printTweet(tweet)

        code = oauth.delete_tweet(id=tweet['tweet']['id'])

        print("Has this been deleted: {}".format(code.data['deleted']))

        count = count + 1
        if(count > number_to_delete):
            break
        elif(count % 49 == 0):
            time.sleep(900)

def main():
    pre_clean()
    number_to_delete = int(sys.argv[1])
    oauth = auth()
    tweets = loadTweets()
    deleteTweets(tweets, number_to_delete, oauth)
    post_clean(tweets, number_to_delete)

if __name__ == '__main__':
    main()