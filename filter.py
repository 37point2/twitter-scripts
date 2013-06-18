import tweepy
import json
import sys

api_keys = json.load(open('api.json', 'r'))

CONSUMER_KEY = api_keys['api']['twitter']['CONSUMER_KEY']
CONSUMER_SECRET = api_keys['api']['twitter']['CONSUMER_SECRET']
ACCESS_TOKEN = api_keys['api']['twitter']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = api_keys['api']['twitter']['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

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
                    print json_data["user"]["screen_name"] + " " + json_data["text"] + "\n"
            except:
                pass

def filter_stream(args):
    listener = StreamListener()
    streamer = tweepy.Stream(auth=auth, listener=listener)
    streamer.filter(track=args)

def main(args):
    filter_stream(args)

if __name__ == '__main__':
    main(sys.argv[1:])
