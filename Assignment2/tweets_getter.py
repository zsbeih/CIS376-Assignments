# Name: Zain Sbeih
# Date: 2/16/2025
from flask import Flask, jsonify
import json

app = Flask(__name__)

# Open the json file containing the tweets and their information
with open('favs.json', 'r') as file:
    tweets = json.load(file)

# Function to get all tweets(time, id, and text) from the json file
@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    tweets_data = []

    # Loop through all tweets and get the necessary information from each tweet saved as a dictionary and appended to a list
    for tweet in tweets:
        tweets_data.append({
            'created_time': tweet['created_at'],
            'id': tweet['id'],
            'text': tweet['text']
        })

    return jsonify(tweets_data)

# Function to get all external link from the json file
@app.route('/links', methods=['GET'])
def get_all_links():
    all_links = []

    # Loop through all tweets and then through all urls and get any external links in the tweet and save it as a dictionary and append it to a list
    for tweet in tweets:
        urls = tweet['entities']['urls'] 
        for url in urls:
            all_links.append({tweet['id']: url['url']})

    return jsonify(all_links)

# Function to get all details, specifically when it was created, the text, and the username of the tweeter about a given tweet(tweet ID)
@app.route('/tweets/<tweet_id>', methods=['GET'])
def get_tweet_details(tweet_id):

    # Loop through all tweets and if a tweet that matches the given id is found, return the details about the tweet
    for tweet in tweets:
        if str(tweet['id']) == tweet_id:
            tweet_details = {
                'created_at': tweet['created_at'],
                'text': tweet['text'],
                'user_screen_name': tweet['user']['screen_name']
            }
            
            return jsonify(tweet_details)

    return jsonify("Error: tweet not found") # If no tweet is found with the given id, return an error

# Function to get a user's profile(location, description, follower count, and friend count) from the json file given a user's screen name
@app.route('/users/<screen_name>', methods=['GET'])
def get_user_profile(screen_name):

    # Loop through all tweets and if a user with the given user screen name is found, return the details about the user
    for tweet in tweets:
        if tweet['user']['screen_name'] == screen_name:
            user_info = {
                'location': tweet['user']['location'],
                'description': tweet['user']['description'],
                'follower_count': tweet['user']['followers_count'],
                'friend_count': tweet['user']['friends_count']
            }
            return jsonify(user_info)
        
    return jsonify("Error: user not found") # If no user is found with the given user screen name, return an error
