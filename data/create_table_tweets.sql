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
