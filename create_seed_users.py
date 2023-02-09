import sqlite3
import uuid

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

for x in range(5):
  id = str(uuid.uuid4()) # uuid is type uuid convert it into text
  db.execute("INSERT INTO users(id,name,email) VALUES('1','a','aa')")
  db.commit()








