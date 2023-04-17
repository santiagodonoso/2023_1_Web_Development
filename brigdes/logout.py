from bottle import get
@get("/logout")
def _():
	# delete_cookies
	# redirect status 303
	# location