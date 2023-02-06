from bottle import get, run, template, static_file

##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

##############################
@get("/")
def render_index():
  return template("index")

##############################
# syn. localhost
run(host="127.0.0.1", port=3000, reloader=True, debug=True) # 65535
