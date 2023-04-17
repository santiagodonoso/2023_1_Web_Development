DROP TABLE IF EXISTS phones;
CREATE TABLE phones(
	user_fk		INTEGER,
	phone_number	TEXT,
	PRIMARY KEY(user_fk, phone_number),
	FOREIGN KEY(user_fk) REFERENCES users(user_id) ON DELETE CASCADE
);

