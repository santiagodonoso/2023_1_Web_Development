from bottle import post, request, response
import json

##############################
@post("/search")
def _():
	try:
		response.set_header("Content-type", "application/json");
		return json.dumps([{"name":"A"}, {"name":"B"}])
	except Exception as e:
		pass
	finally:
		pass



