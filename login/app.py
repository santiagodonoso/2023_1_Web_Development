from bottle import get, request, run, template

@get("/login")
def _():
    return template("login")

##############################
@get("/admin")
def _():
    user = request.get_cookie("user", secret="my-secret")
    user_name = "MY USER NAME HERE"
    return template("admin", user=user)

##############################
import bridges.login

##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)



