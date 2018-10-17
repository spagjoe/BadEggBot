import tweepy, random

class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		username = status.user.screen_name 
		status_id = status.id
		replyTweet(username, status_id)


	def on_error(self, status):
		if status_code == 420:
			return False

def replyTweet(username, status_id):
	rdm = random.randint(0, 2)
	if rdm == 0:
		api.update_status('@{0} You\'re a bad egg.'.format(username), in_reply_to_status_id=status_id)
	else:
		api.update_status('@{0} You\'re a good egg.'.format(username), in_reply_to_status_id=status_id)

#keys: note that you need unique keys from twitter API
consumer_key = "xxx"
consumer_secret = "xxx"
access_token = "xxx"
access_token_secret = "xxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener(api)
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track = ["@BadEggBot"])
