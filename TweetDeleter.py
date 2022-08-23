import tweepy
from zipfile import ZipFile
import os
import json
import time
import sys

def pre_clean():
    # Create JSON from archive.zip tweet history
    if not os.path.exists('tweet.json'):
        with ZipFile('archive.zip', 'r') as z:
            with open('tweet.json', 'wb') as f:
                f.write(z.read('data/tweet.js')[25:])
    # Create JSON from archive.zip like history
    if not os.path.exists('like.json'):
        with ZipFile('archive.zip', 'r') as z:
            with open('like.json', 'wb') as f:
                f.write(z.read('data/like.js')[24:])

def post_clean(tweets, number):
    # Take in tweets/likes and removed them from their JSON files
    tweets = tweets[number:]
    with open('tweet.json', 'w') as outfile:
        outfile.write(json.dumps(tweets , sort_keys=False, indent=2))

def loadTweets():
    # Load Tweets and return as a JSON object
    with open('./tweet.json', errors="ignore") as f:
        tweets = json.load(f)
    
    return tweets

def loadLikes():
    # Load Likes and return as a JSON object
    with open('./like.json', errors="ignore") as f:
        likes = json.load(f)
    
    return likes

def printTweet(tweet):
    print("Tweet: "+ tweet['tweet']['full_text'])
    print(tweet['tweet']['retweet_count'] + ' Retweets || ' + tweet['tweet']['favorite_count'] + " Likes || Date: " + tweet['tweet']['created_at'])
    print('______________________________________________________________ \n')

def printLike(tweet):
    print("Tweet: "+ tweet['like']['fullText'])
    print('______________________________________________________________ \n')

def auth():
    # Auth with Twitter API using Tweepy and OAuth2
    # Using this client, we auth as an user instead of an app
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

def deleteLikes(tweets, number_to_delete, oauth):
    # Go through Likes JSON, and unlike tweets by their IDS
    # User rate limit is 50 requests per 15-minutes windows
    # Once we hit that limit we sleep for 15 mins
    count = 0
    for tweet in tweets:

        printLike(tweet)
        print("Currently on count {}".format(count))

        code = oauth.unlike(tweet['like']['tweetId'])
        
        if(code.data['liked'] == False):
            print("This Tweet has been unliked!")

        count = count + 1
        if(count > number_to_delete):
            break
        elif(count % 49 == 0):
            time.sleep(900)

def deleteTweets(tweets, number_to_delete, oauth):
    # Go through Tweets JSON, and unlike tweets by their IDS
    # User rate limit is 50 requests per 15-minutes windows
    # Once we hit that limit we sleep for 15 mins
    count = 0
    for tweet in tweets:

        printTweet(tweet)
        print("Currently on count {}".format(count))
        
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
    # Tweets to Delete
    #tweets = loadTweets()
    #deleteTweets(tweets, number_to_delete, oauth)
    #post_clean(tweets, number_to_delete)
    # Likes to Unlike
    likes = loadLikes()
    deleteLikes(likes, number_to_delete, oauth)
    post_clean(likes, number_to_delete)

if __name__ == '__main__':
    main()