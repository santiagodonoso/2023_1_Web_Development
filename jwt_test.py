import jwt
# If the user verifies the JWT show the payload. If not the correct secret, show Sorry...
the_jwt = jwt.encode({"name":"Santiago"}, "the secret", algorithm="HS256")
try:
	# jwt.decode(the_jwt, "the secret", algorithms="HS256")
	print(jwt.decode(the_jwt, "the secret", algorithms="HS256"))
except Exception as e:
	print("Sorry, we cannot verify you")





