#SeanDehghani
#HW6


import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "33093650-lMlbx8bcuRLVkj5pMEiq8DBJowq2k3M8gDm7JdHKX"
access_token_secret_ = "ZsFfmHcZBMVSmS1r8lB5F1YVhbIKRNRmWiwECN8ars"
consumer_key = "5sk7dKsZGWfSycMZhRN8F93SW"
consumer_secret = "CIKf9lN29zhnw6U6dc0GWtiWaaBYSwmBrcgHpUtCdqabRoAqql"

class StdOutListener(StreamListener):

    def on_data(self,data):
        print(data)
        return True

    def on_error(self, status):
        print(status) 

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret_)
twitterStream = Stream(auth, StdOutListener()) 
twitterStream.filter(track=["python", "javascript", "ruby"])
