from bottle import get, run, template, static_file, response, request
import sqlite3

# This data will come from the database
# For now, we just hard coded the data
# 0 False 1 True
tweets = [
  { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":0, "image_name":"2.jpg", "fullname":"Joe Biden", "username":"joebiden","message":"I am THE president","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":0, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":0, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
]

# list = array
# dictionary is {}. Think of it as JSON
trends = [
  {"title":"One", "total_hash":1},
  {"title":"Two", "total_hash":2},
  {"title":"Three", "total_hash":3},
  {"title":"Four", "total_hash":4},
  {"title":"Five", "total_hash":5},
  {"title":"Six", "total_hash":6},
  {"title":"Seven", "total_hash":7},
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
  return template("index", title="Twitter", tweets=tweets,
  trends=trends)

##############################
@get("/about")
def _():
  return template("about-us")  

##############################
@get("/contact")
def _():
  return template("contact-us")  

##############################
# APIs do not return HTML... there are exceptions
# API returns most likely JSON
# Rule 1 - To test the API you use thunderclient or Postman
@get("/api-get-name")
def _():
  try: # Best case scenario

    id = request.query.get("id")
    name = request.query.get("name")
    lastname = request.query.get("lastname")

    if id != "1": raise Exception("the id is wrong")
    if name != "a": raise Exception("the name is wrong")
    if lastname != "b": raise Exception("the lastname is wrong")

    # Connect/Open to the database
    db = sqlite3.connect("twitter.db")
    users = db.execute("SELECT * FROM users").fetchall()
    print(users) # this is for the terminal
    # Get name from the database

    # Send the name to the client
    # return users
    return {"id":id, "name": name, "lastname":lastname}
  except Exception as ex: # Something went wrong
    print(dir(ex))
    # Send a 400 to the client
    response.status = 400
    return {"error": str(ex)}
  finally: # It must be done 
    # Close the database
    if "db" in locals(): db.close()
    print("I am here")
  

##############################
# syn. localhost
run(host="127.0.0.1", port=3000, reloader=True, debug=True, server="paste") # 65535
