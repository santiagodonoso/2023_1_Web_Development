from bottle import get, run, view

##############################
@get("/<username>")
@view("profile")
def _(username):
  return 

##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)

