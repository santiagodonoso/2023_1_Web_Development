from bottle import post

@post("/tweet")
def _():
  return "ok"



