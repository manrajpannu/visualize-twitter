from twitterscraper import query_tweets
from datetime import timedelta, date
import json



def get_pictures(search_term, limit, days_back=7):
	end_date = date.today()
	begin_date = date.today() - timedelta(days=days_back)

	tweets = query_tweets(search_term, begindate=begin_date, enddate=end_date, limit=limit, poolsize=days_back)

	output = []

	for tweet in tweets:
		for images_url in tweet.img_urls:
			output.append({'image':str(images_url),"tweet": str(tweet.tweet_url)})

	return output
	# with open("temp.py",'w') as f:
	# 	f.write('posts = '+json.dumps(output))