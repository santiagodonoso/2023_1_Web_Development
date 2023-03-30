from bottle import post, request, response
import random


@post("/api-get-latest-tweets")
def _():	
	# TODO: Get latest tweets from the db
	# tweets = db.execute("SELECT * FROM tweets ????????")
	return str(     int(random.randint(0, 999))     )
	# return "x"

