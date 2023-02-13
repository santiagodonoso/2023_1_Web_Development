DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id                TEXT,
  username          TEXT,
  name              TEXT,
  last_name         TEXT,
  total_followers   TEXT,
  total_following   TEXT,
  total_tweets      TEXT,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;

INSERT INTO users VALUES("1","elonmusk","Elon", "Musk", "128900000", "177", "22700");



