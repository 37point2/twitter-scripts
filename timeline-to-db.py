from pymongo import Connection
import tweepy
import json
from time import sleep

#add OAuth keys
CONSUMER_KEY =
CONSUMER_SECRET =
ACCESS_TOKEN =
ACCESS_TOKEN_SECRET =

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

connection = Connection('localhost', 27017)
#define the db name and collection however you'd like
db = connection.Twitter
raw = db.raw

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
        try:
            json_data = json.loads(data)
            if not json_data.has_key("friends"):
                raw.insert(json_data)
                print json_data["user"]["screen_name"] + " " + json_data["text"] + "\n"
        except:
            pass

def get_stream():
    listener = StreamListener()
    streamer = tweepy.Stream(auth=auth, listener=listener)
    streamer.userstream()

def main():
    while True:
        try:
            get_stream()
        except:
            sleep(300)
            continue

if __name__ == '__main__':
    main()
