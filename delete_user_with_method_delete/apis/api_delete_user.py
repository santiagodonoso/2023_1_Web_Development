from bottle import delete, request, response

##############################
# @post("/user") id comes in the form
# @get("/user/3")
# @delete("/user") id comes in the form
# @put("/user") id, name, last name, etc. comes in the form

# @post("/user") id,name, last name, etc. comes in the form
# @get("/user/3")
# @delete("/user/3")
# @put("/user/1") name, last name, etc. comes in the form

@delete("/user/<user_id>")
def _(user_id):
	try:
		return f"user deleted: {user_id}"
	except Exception as e:
		pass
	finally:
		pass