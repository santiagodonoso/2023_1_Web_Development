from bottle import post, response
import x
import uuid
import time
import bcrypt
import random

##############################
@post("/api-sign-up")
def _():
	try:

		user_email = x.validate_user_email()
		user_phone = x.validate_user_phone()
		user_password = x.validate_user_password()
		x.validate_user_confirm_password()
		# Adding the salt to password
		salt = bcrypt.gensalt()
		user_id = str(uuid.uuid4()).replace("-","")
		user_api_key = str(uuid.uuid4()).replace("-","")
		user_verification_key = random.randint(1000, 9999)
		user = {
            "user_id" : user_id,
            "user_email" : user_email,   
			"user_phone" : user_phone,         
            "user_created_at" : int(time.time()),
            "user_api_key" : user_api_key,
            "user_password": bcrypt.hashpw(user_password.encode('utf-8'), salt),
			"user_password_reset_key" : "",
			"user_verification_key" : user_verification_key,
			"user_verified_at" : 0,
			"user_last_sent_sms_at" : 0,
        }
		"""
		def get_values_from_dictionary(dictionary):
			values = ""
			for key in dictionary:
				values += f":{key},"
			return values.rstrip(",")			
		"""
		values = x.get_values_from_dictionary(user)
		db = x.db()
		db.execute(f"INSERT INTO users VALUES({values})", user)
		
		sms = {
			"sms_id" : str(uuid.uuid4()).replace("-",""),
			"sms_message" : f"Welcome to SMSES. Your verification key is: {user_verification_key}",
			"sms_to_phone" : user_phone,
			"sms_created_at" :  int(time.time()),
			"sms_sent_at" : 0,
			"sms_user_id" : "admin"
		}	
		values = x.get_values_from_dictionary(sms)
		db.execute(f"INSERT INTO smses VALUES({values})", sms)

		db.commit()		
		return {
			"info" : "User created. You must verify your account: api-verify-account", 
			"user_id" : user_id,
			"user_api_key" : user_api_key
		}
	except Exception as e:
		print(e)
		if "db" in locals(): db.rollback()
		try: # Controlled exception, usually comming from the x file
			response.status = e.args[0]
			return {"info":e.args[1]}
		except: # Something unknown went wrong
			if "user_email" in str(e): 
				response.status = 400 
				return {"info":"user_email already exists"}
			if "user_phone" in str(e): 
				response.status = 400 
				return {"info":"user_phone already exists"}				
			# unknown scenario
			response.status = 500
			return {"info":str(e)}
	finally:
		if "db" in locals(): db.close()
