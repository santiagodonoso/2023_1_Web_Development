from bottle import get, run, template, static_file

# This data will come from the database
# For now, we just hard codedthe data
# 0 False 1 True
tweets = [
  { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":0, "image_name":"2.jpg", "fullname":"Joe Biden", "username":"joebiden","message":"I am THE president","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":0, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":0, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
]






##############################
@get("/images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./images")

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
  return template("index", title="Twitter", tweets=tweets)

##############################
# syn. localhost
run(host="127.0.0.1", port=3000, reloader=True, debug=True) # 65535
