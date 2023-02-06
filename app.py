from bottle import get, run, template, static_file

##############################
@get("/thumbnails/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./thumbnails")

##############################
@get("/thumbnails/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./thumbnails")

##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

##############################
@get("/")
def render_index():
  return template("index", title="Twitter")

##############################
# syn. localhost
run(host="127.0.0.1", port=3000, reloader=True, debug=True) # 65535
