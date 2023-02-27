from bottle import get, template
import x

@get("/tweet")
def _():
  return template("tweet", 
                  tweet_min_len=x.TWEET_MIN_LEN, 
                  tweet_max_len=x.TWEET_MAX_LEN)