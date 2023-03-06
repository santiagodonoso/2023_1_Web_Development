from bottle import post, response

@post("/login")
def _():
    # Redirection
    # status code
    # the redirected page
    # response.status = 300
    # response.set_header("Location", "/login")
    user = {
        "user_name":"santiagodonoso",
        "user_first_name":"Santiago",
        "user_last_name":"Donoso"
    }
    response.set_cookie("user", user, secret="my-secret")
    response.status = 303
    response.set_header("Location", "/admin")
    return

