import sqlite3

db = sqlite3.connect("twitter.db")

db.executescript(
  """
  BEGIN;
  DROP TABLE IF EXISTS users;
  CREATE TABLE users(
    id            TEXT,
    name          TEXT,
    email         TEXT,
    PRIMARY KEY(id)
  ) WITHOUT ROWID;
  COMMIT;
  """
)

db.execute("INSERT INTO users(id,name,email) VALUES('1','a','aa')")
db.commit()








