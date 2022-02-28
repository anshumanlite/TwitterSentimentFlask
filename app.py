from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = '3hFs89kzifJGnpCSmNbahZ8sg'
consumer_secret = 'sLnbChEhqj7LtGssXRBcmccCImZ4BpMkug7DONkcRqJvsYGRj9'

access_token = '1450437905424416776-cQQ1LB7S5k5kqLspGOCmzRBY2sr5YC'
access_token_secret = '9quRIk9YiIrQfHf5e1RPBO4jLhmWPdtCnGVlV2jjDmipn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()