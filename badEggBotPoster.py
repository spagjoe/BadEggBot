import tweepy, random, time, badEggAPI

def makeRdmPost():
	c = 0
	rdm = 0
	content = ""
	templates = open("badEggTemplates.txt")
	for line in templates:
		c += 1
	rdm = random.randint(0, c-1)
	templates = open("badEggTemplates.txt")
	content = templates.readlines()[rdm]
	c = 0

	nouns = open("badEggNouns.txt")
	for line in nouns:
		c += 1
	while(content.find("(noun)") >= 0):
		nouns = open("badEggNouns.txt")
		rdm = random.randint(0, c-1)
		print(rdm)
		newNoun = nouns.readlines()[rdm]
		content = content.replace("(noun)", newNoun, 1)
	c = 0

	verbs = open("badEggVerbs.txt")
	for line in verbs:
		c += 1
	while(content.find("(verb)") >= 0):
		verbs = open("badEggVerbs.txt")
		rdm = random.randint(0, c-1)
		print(rdm)
		newVerb = verbs.readlines()[rdm]
		content = content.replace("(verb)", newVerb, 1)

	content = content.replace("\n", '')
	api.update_status(content)

api = badEggAPI.connectAPI()

while(True):
	makeRdmPost()
	time.sleep(3600)