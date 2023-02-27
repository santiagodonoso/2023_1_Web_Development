from bottle import get, template

@get("/tweet")
def _():
  return template("tweet")