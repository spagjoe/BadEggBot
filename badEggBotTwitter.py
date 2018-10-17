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

#keys:
consumer_key = "IedrWL2cqTAX8nh4AKlaqiKCf"
consumer_secret = "LDQwDBqtgbytkwFYIRg9ksqtJjdg6z4ADckOku5tLix1XicJhG"
access_token = "990326452968198144-f4dNZwLGtcAD6rjsTPkTIOI9nNjLPHj"
access_token_secret = "Mzqcfpeaf7EDU2xl526ic6FpgNlJOb5MhFvWOXjWMOTyt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener(api)
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track = ["@BadEggBot"])