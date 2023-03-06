from bottle import get, run, template

@get("/login")
def _():
    return template("login")



##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)



