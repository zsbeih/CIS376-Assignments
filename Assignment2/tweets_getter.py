from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('favs.json', 'r') as file:
    tweets = json.load(file)

@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    tweets_data = []
    for tweet in tweets:
        tweets_data.append({
            'created_time': tweet['created_at'],
            'id': tweet['id'],
            'text': tweet['text']
        })

    return jsonify(tweets_data)

@app.route('/links', methods=['GET'])
def get_all_links():
    all_links = []
    for tweet in tweets:
        urls = tweet['entities']['urls']

        for url in urls:
            all_links.append({tweet['id']: url['url']})

    return jsonify(all_links)

@app.route('/tweets/<tweet_id>', methods=['GET'])
def get_tweet_details(tweet_id):

    for tweet in tweets:
        if str(tweet['id']) == tweet_id:
            tweet_details = {
                'created_at': tweet['created_at'],
                'text': tweet['text'],
                'user_screen_name': tweet['user']['screen_name']
            }
            
            return jsonify(tweet_details)

    return jsonify("Error: tweet not found")

@app.route('/users/<screen_name>', methods=['GET'])
def get_user_profile(screen_name):

    for tweet in tweets:
        if tweet['user']['screen_name'] == screen_name:
            user_info = {
                'location': tweet['user']['location'],
                'description': tweet['user']['description'],
                'follower_count': tweet['user']['followers_count'],
                'friend_count': tweet['user']['friends_count']
            }
            return jsonify(user_info)
        
    return jsonify("Error: user not found")
