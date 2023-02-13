from bottle import get, template, run, view
import sqlite3

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
    db = sqlite3.connect("twitter.db")
    db.row_factory = dict_factory
    user = db.execute("SELECT * FROM users WHERE username=?",(username,)).fetchall()[0]
    print(user) # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
    return template("profile", user=user)
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()


##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)

