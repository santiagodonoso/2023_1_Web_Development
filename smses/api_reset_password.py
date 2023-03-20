from bottle import post, request, response
import x
import bcrypt

##############################
@post("/api-reset-password")
def _():
	try:
		user_password_reset_key = request.params.get("user_password_reset_key", "")

		"""
		UUID4_LEN = 32
		UUID4_REGEX = "^[a-f0-9]*$"

		def validate_uuid4(field_name, uuid4):
			error = f"{field_name} invalid"
			uuid4 = uuid4.strip()
			if len(uuid4) != UUID4_LEN : raise Exception(400, error)
			if not re.match(UUID4_REGEX, uuid4): raise Exception(400, error)
			return uuid4		
		"""

		user_password_reset_key = x.validate_uuid4("user-password-reset-key", user_password_reset_key)
		user_password = x.validate_user_password()
		x.validate_user_confirm_password()

		salt = bcrypt.gensalt()
		user_password = bcrypt.hashpw(user_password.encode('utf-8'), salt)

		db = x.db()
		total_changes = db.execute("""
			UPDATE users
			SET user_password = ?, user_password_reset_key = ""
			WHERE user_password_reset_key = ?
			""", (user_password, user_password_reset_key)).rowcount
		db.commit()
		if total_changes != 1: raise Exception(400, "cannot update password. The user_password_reset_key may be invalid")
		return {"info":"password updated"}
	except Exception as e:		
		if "db" in locals(): db.close()
		try: # Controlled exception, usually comming from the x file
			response.status = e.args[0]
			return {"info":e.args[1]}
		except:		
			# unknown scenario
			response.status = 500
			return {"info":str(e)}
	finally:
		if "db" in locals(): db.close()
