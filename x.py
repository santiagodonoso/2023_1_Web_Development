from bottle import request

TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 5

def validate_tweet():
  error = f"tweet min {TWEET_MIN_LEN} max {TWEET_MAX_LEN} characters"
  if len(request.forms.get("message")) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.get("message")) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.get("message")








