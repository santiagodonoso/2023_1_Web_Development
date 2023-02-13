DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
  id              TEXT,
  user_fk         TEXT,
  created_at      TEXT,
  message         TEXT,
  image           TEXT,
  updated_at      TEXT,
  total_retweets  TEXT,
  total_likes     TEXT,
  total_views     TEXT,
  total_replies   TEXT,
  PRIMARY KEY(id)
) WITHOUT ROWID;

INSERT INTO tweets VALUES(
  "75544dcd995745ba83557143458a672c", 
  "51602a9f7d82472b90ed1091248f6cb1",
  "1676283561",
  "My first tweet",
  "",
  "0",
  "0",
  "0",
  "0",
  "0"
  );

