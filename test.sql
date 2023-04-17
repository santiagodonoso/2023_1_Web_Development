DROP TABLE IF EXISTS posts;
CREATE VIRTUAL TABLE posts USING FTS5(post_title, post_body);

INSERT INTO posts VALUES 
('We are trying this database', 'We hope this works'),
('Send a text message', 'We do it via fiotext'),
('Macs are great', 'Windows are great too');
-- find "are" and "message"
SELECT * FROM posts WHERE posts MATCH 'are NOT trying';





