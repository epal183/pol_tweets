# NLP
# Team Project

import tweepy
import csv
import sys

# Twitter API credentials
consumer_api_key = "GTxJrg4AY2J83vgpOTgFKnoHD"
consumer_api_secret = "quGsfOW9FdNsFrMVtQvlPz0RrB5Nx69beXO7Y36muH508LMaOJ"
access_token = "1018939370458566656-n4nQ7qJ3ifQJ4AMuQo72Wd0bhofKZI"
access_token_secret = "340gQMx5ZSz4e5vlDjBeyDyyc3uHUAkLquIblmOqTp0bp"

# reference: https://gist.github.com/yanofsky/5436496
def get_all_tweets(screen_name):
	"""
	Searches tweets by the twitter account user id (screen name)
	and returns a list of up to 3240 most recent tweets (Status object).
	
	Note:
		Without a Premium Twitter API, Twitter only allows access
		to a user's most recent 3240 tweets.

	Args:
		screen_name (str): twitter account user id
	
	Returns:
		output_tweets (list): list of tuples containing tweet info.
	"""
	# initialize tweepy
	auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	print(f'\nRetrieving tweets by Twitter Account (user id): {screen_name}\n')
	# retrieve most recent tweets by user_id (200 is the maximum allowed count)
	retrieved_tweets = api.user_timeline(screen_name = screen_name, count=200, tweet_mode='extended')
	all_tweets = retrieved_tweets
	try:
		# save the last tweet_id retrieved for further retrieval
		oldest_tweet_id = retrieved_tweets[-1].id - 1
	except:
		print(f"Twitter Account (user id): '{screen_name}' does not have any tweets.")
		return None

	# keep fetching tweets (200 each time) until all tweets are retrieved
	while len(retrieved_tweets) > 0:
		print(f'Retrieved up to tweet id number: {oldest_tweet_id}')
		print(f'{len(all_tweets)} tweets downloaded so far.\n')
		# max_id parameter prevents duplicate tweets
		retrieved_tweets = api.user_timeline(
			screen_name = screen_name,
			count=200,
			max_id=oldest_tweet_id,
			tweet_mode='extended')
		try:
			# save the last tweet_id retrieved for further retrieval
			oldest_tweet_id = retrieved_tweets[-1].id - 1	
			all_tweets.extend(retrieved_tweets)
		except:
			print(f"Retrieved all tweets by Twitter Account (user id): '{screen_name}'.\n")
			
	# save tweet id, tweet created time, tweet full text to output list.
	output_tweets = []
	for tweet in all_tweets:
		output_tweets.append((tweet.id_str, tweet.created_at, tweet.full_text.encode('utf-8')))
	return output_tweets

def write_csv_file(screen_name, list_of_tweets):
	"""
	Writes tweet data into csv file.
	"""	
	print(f'Writing to csv file: {screen_name}_tweets.csv')
	with open(f'{screen_name}_tweets.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		headers = ("tweet_id", "created_at", "full_text")
		writer.writerow(headers)
		writer.writerows(list_of_tweets)


if __name__ == '__main__':
	screen_name = sys.argv[-1]
	list_of_tweets = get_all_tweets(screen_name)
	if list_of_tweets is not None:
		write_csv_file(screen_name, list_of_tweets)