# TwitterDeleter
 Completely clean your Twitter Account! This scripts cleans out all old Tweets and Likes provided from a user's archived Twitter data.

 ## How It's Made:
 **Tech Used:** Python, [Tweepy (Python library for accessing the Twitter API)](https://docs.tweepy.org/), [Twitter API](https://developer.twitter.com/en/docs)

## How It Works:
With a Twitter Developer Account, a Twitter App created, and your downloaded tweet archive you can use that information to delete and unlike Tweets everything in your account and start fresh. 
Using Tweepy, we will authenticate with Twitter with OAuth2 as a user instead of an App by passing our keys and bearer token. Then we create two JSON files contain all the information about your Tweets and all the Tweets you've liked. We load those JSON files and go through all that data to delete/unlike those tweets, leaving your an Twitter account like new!

## How to Get Started:
### Apply for a Twitter Developer account

1. [Create a Twitter Developer account](https://developer.twitter.com/en/apply):
    1. **User profile**: Use your current Twitter @username.
    1. **Account details**: Select *I am requesting access for my own personal use*,
      set your 'Account name' to your @username, and select your 'Primary country
      of operation.
    1. **Use case details**: select 'Other', and explain in at least 300 words that
      you want to create an app to semi-automatically clean up your own tweets.
    1. **Terms of service**: Read and accept the terms.
    1. **Email verification**: Confirm your email address.
1. Now wait for your Twitter Developer account to be reviewed and approved.

### Create a Twitter app

1. [Create a new Twitter app](https://developer.twitter.com/en/apps/create) (not
  available as long as your Twitter Developer account is pending review).
1. Set 'Access permissions' of your app to *Read and write*.

### Configure your environment

1. Open your Twitter Developer's [apps](https://developer.twitter.com/en/apps).
1. Click the 'Details' button next to your newly created app.
1. Click the 'Keys and tokens' tab, and find your keys, bearer token, secret keys and access tokens.
1. Copy and paste your keys into the appropriate place, like so

```python
"consumer_key" : "abcdefgh12345"
```

### Get your tweet archive

1. Open the [Your Twitter data page](https://twitter.com/settings/your_twitter_data)
1. Scroll to the 'Download your Twitter data' section at the bottom of the page
1. Re-enter your password
1. Click 'Request data', and wait for the email to arrive
1. Follow the link in the email to download your Tweet data
1. Unpack the archive

### Running the script

1. Open the terminal in the Project's directory
1. Run the python script using the following command which the amount of Tweets you want to go through, which run every 15 minutes
```python
$ py TweetDeleter.py 100
```
1. If you don't want to delete tweets or unlike tweets, comment those lines out under def main()
```python
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
```