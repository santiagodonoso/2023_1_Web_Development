from bottle import get, template
import x

tweets = [
  {"tweet_id":"1", "tweet_message":"a"},
  {"tweet_id":"2", "tweet_message":"b"},
  {"tweet_id":"3", "tweet_message":"c"}
]

@get("/tweet")
def _():
  return template("tweet", 
                  tweet_min_len=x.TWEET_MIN_LEN, 
                  tweet_max_len=x.TWEET_MAX_LEN, 
                  tweets=tweets)