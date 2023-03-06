from bottle import get, request, response, run, template

@get("/login")
def _():
    return template("login")

##############################
@get("/profile")
def _():

    response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)

    user = request.get_cookie("user", secret="my-secret")
    # if not user:
    # if user is None:
    #     response.status=303
    #     response.set_header("Location", "/login")
    #     return
    return template("profile", user=user)

##############################
@get("/logout")
def _():
    response.set_cookie("user", "", expires=0)
    response.status = 303
    response.set_header("Location", "/login")
    return


##############################
import bridges.login

##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)



