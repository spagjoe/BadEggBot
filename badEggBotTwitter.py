import tweepy, random, time, badEggAPI

class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		username = status.user.screen_name 
		status_id = status.id
		replyTweet(username, status_id)



def replyTweet(username, status_id):
	rdm = random.randint(0, 2)
	if rdm == 0:
		api.update_status('@' + username +' You\'re a bad egg.'.format(username), in_reply_to_status_id=status_id)
	else:
		api.update_status('@' + username +' You\'re a good egg.'.format(username), in_reply_to_status_id=status_id)


api = badEggAPI.connectAPI()


myStreamListener = MyStreamListener(api)
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track = ["@BadEggBot"])
