from bottle import post, response
import x

@post("/test")
def _():
	try:
		db = x.db()
		db.commit()
		return {"info":"ok"}
	except Exception as e:
		print(e)
		if "db" in locals(): db.rollback()
		try: # Controlled exception, usually comming from the x file
			response.status = e.args[0]
			return {"info":e.args[1]}
		except: # Something unknown went wrong
			if "users.user_email" in str(e):
				response.status = 400
				return {"info":"user_email already exists"}
			if "users.user_phone" in str(e):
				response.status = 400
				return {"info":"user_phone already exists"}
			# unknown scenario
			response.status = 500
			return {"info":str(e)}
	finally:
		if "db" in locals(): db.close()