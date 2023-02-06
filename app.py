from bottle import get, run

##############################
@get("/")
def render_index():
  return "hix"

##############################
# syn. localhost
run(host="127.0.0.1", port=3000, reloader=True, debug=True) # 65535
