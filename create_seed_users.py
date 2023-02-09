import sqlite3

db = sqlite3.connect("twitter.db")

db.executescript(
  """
  BEGIN;
  DROP TABLE IF EXISTS users;
  COMMIT;
  """
)









