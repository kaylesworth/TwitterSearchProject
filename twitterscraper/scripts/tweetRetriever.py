from twython import Twython
import time

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#Uses Twython and Twitter API to grab tweets with the entered word from index
#Adds username, date, and tweet into a list and returns a list containing all
def tweetRetriever(word):
	results = twitter.search(q="#"+word, count='1500', lang='en')
	tweets = []
	for r in results['statuses']:
		t = r['created_at']
		date = t[3:10] + " " +  t[25:]
		temp = {'username':r['user']['screen_name'], 'date':date , 'tweet':r['text'], 'picture_url':r['user']['profile_image_url_https'], 'name':r['user']['name'], 'id':r['id']}
		tweets.append(temp)
	return tweets

