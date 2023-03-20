DROP TABLE IF EXISTS users;
CREATE TABLE users(
	user_id 					TEXT UNIQUE,
	user_email 					TEXT UNIQUE,  
	user_phone					TEXT UNIQUE,          
	user_created_at 			TEXT,
	user_api_key 				TEXT UNIQUE,
	user_password 				TEXT,
	user_password_reset_key		TEXT,
	user_verification_key 		TEXT,
	user_verified_at			TEXT,
	user_last_sent_sms_at		TEXT,
	PRIMARY KEY(user_id)
) WITHOUT ROWID;

-- ##############################

DROP TABLE IF EXISTS smses;
CREATE TABLE smses(
	sms_id			TEXT UNIQUE,
	sms_message		TEXT,
	sms_to_phone	TEXT,
	sms_created_at	TEXT,
	sms_sent_at		TEXT, -- 0 if not sent, else epoch
	sms_user_id		TEXT,
	PRIMARY KEY(sms_id)
) WITHOUT ROWID;