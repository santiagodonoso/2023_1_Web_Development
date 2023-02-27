from bottle import post, request
import x

@post("/tweet")
def _():
  try: # SUCCESS
    x.validate_tweet()
    return "ok"
  except Exception as ex: # SOMETHING IS WRONG
    return str(ex)
  finally: # This will always take place
    pass

