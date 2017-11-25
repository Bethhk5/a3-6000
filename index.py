import tweepy, time, csv

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "D03T2ecjTxDSTbBiteLy1T66N"
consumer_secret = "pOZf8FOnb8m22q3hMaTqM3ql2FEd8fD6uyZT90BmnJoqE15cHp"
access_key = "915585146245525504-TmCSh9nD12LuwVpn1R0U2aVGRUycbEe"
access_secret = "FpH7gYP5U5iPuPeboueNNqnOlXDDROrKiGoJwLqBDi5Pq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# this function collects a twitter profile request and returns a Twitter object
def get_profile(CitronResearch):
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"
    return user_profile

def get_tweets(screen_name):
    try:
        tweets = api.user_timeline(screen_name = screen_name,count = 200)
    except:
        tweets = "broken"
    return tweets

# uses the function to query a Twitter user. Try s = get_profile("cd_conrad")
profiles = ["CitronResearch"]

with open ('tweets.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for profile in profiles:
        t = get_tweets(profile)
        for tweet in t:
            if "FTC" in tweet.text:#change shopify to
                print(tweet.text)
                writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
