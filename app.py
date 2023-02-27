from bottle import default_app, get, template, run, view
import os
import sqlite3
import pathlib
import uuid


print("#"*30)
print("directory of the script being run")
print(pathlib.Path(__file__).parent.resolve()) # /home/USERNAME/mysite




##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
@get("/")
def _():
  return "Home page"

##############################
@get("/<username>")
# @view("profile")
def _(username):
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
    db.row_factory = dict_factory
    user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE",(username,)).fetchall()[0]
    # Get the user's id
    user_id = user["id"]
    print("#"*30)
    print(f"user id:{user_id}")
    # With that id, look up/get the respectives tweets
    tweets = db.execute("SELECT * FROM tweets WHERE user_fk=?", (user_id,)).fetchall()
    print("#"*30)
    print(tweets)
    print("#"*30)
    # pass the tweets to the view. Template it
    
    print(user) # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
    return template("profile", user=user)
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()

##############################
# VIEWS
import views.tweet

##############################
# APIS
import apis.api_tweet




##############################
##############################
# Run in AWS
try:
  import production
  print("Server running on AWS")
  application = default_app()
# Run in local computer
except Exception as ex:
  print("Server running locally")
  run(host="127.0.0.1", port=80, debug=True, reloader=True) # 1024 - 65535

