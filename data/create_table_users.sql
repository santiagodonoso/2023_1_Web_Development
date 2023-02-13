DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id                TEXT,
  username          TEXT,
  name              TEXT,
  last_name         TEXT,
  total_followers   TEXT,
  total_following   TEXT,
  total_tweets      TEXT,
  avatar            TEXT,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;

INSERT INTO users VALUES("51602a9f7d82472b90ed1091248f6cb1","elonmusk","Elon", "Musk", "128900000", "177", "22700","51602a9f7d82472b90ed1091248f6cb1.jpg");
INSERT INTO users VALUES("6268331d012247539998d7664bd05cc1","shakira","Shakira", "", "53700000", "235", "7999", "6268331d012247539998d7664bd05cc1.jpg");
INSERT INTO users VALUES("a22da1effb3d4f03a0f77f9aa8320203","Rihanna","Rihanna", "", "107000000", "980", "10600", "a22da1effb3d4f03a0f77f9aa8320203.jpg");



