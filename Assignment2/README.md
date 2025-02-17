1. Make sure `favs.json` and `tweets_getter.py` are in the root directory
2. Ensure python version 3.12.9 is installed
3. Install requirements containing the flask version:

    pip install -r requirements.txt
                or
    pip install flask

4. Run the program:

    flask --app tweets_getter run 

View the contents for each of the functions through the following links: 
    http://127.0.0.1:5000/tweets
    http://127.0.0.1:5000/links
    http://127.0.0.1:5000/tweets/<tweet_id>
    http://127.0.0.1:5000/users/<screen_name>