from bottle import get, template, run, view

##############################
@get("/<username>")
# @view("profile")
def _(username):
  return template("profile")

##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)

