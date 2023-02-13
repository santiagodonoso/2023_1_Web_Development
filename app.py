from bottle import get, run

##############################
@get("/<username>")
def _(username):
  return username

##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)

