from bottle import post, response
import time 

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
    # 1678060800


    cookie_expiration_date = int(time.time()) + 7200
    response.set_cookie("user", user, secret="my-secret", httponly=True)
    response.status = 303
    response.set_header("Location", "/profile")
    return

