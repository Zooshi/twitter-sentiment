import tweepy
from textblob import TextBlob
from accountdata import Accessdata

Access = Accessdata()

app_key = Access.app_key
app_secret = Access.app_secret

access_token =Access.access_token
access_secret = Access.access_secret

auth = tweepy.OAuthHandler(app_key,app_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

results = api.search('Trump')

for result in results:
    print(result.text)
    thetext = TextBlob(result.text)
    print(thetext.sentiment)
