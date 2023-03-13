from bottle import post, request, response
import x
##############################
@post("/api-sign-up")
def _():
    try:
        user_name = x.validate_user_name()
        return "ok"
    except Exception as e:
        print(e)
        return {"info":str(e)} # cast to string
    finally:
        pass




