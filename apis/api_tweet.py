from bottle import post, request, response
import x

@post("/tweet")
def _():
  try: # SUCCESS
    x.validate_tweet()
    return "ok"
  except Exception as ex: # SOMETHING IS WRONG
    response.status = 400
    return str(ex)
  finally: # This will always take place
    pass

