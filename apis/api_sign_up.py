from bottle import post, request, response
import x
##############################
@post("/api-sign-up")
def _():
    try:
        user_name = x.validate_user_name()
        user_id = 1
        user = {
            "user_id" : user_id,
            "user_name" : user_name
        }
        values = ""
        for key in user:
            values = values + f":{key},"
        values = values.rstrip(",")
        print(values)
        # db.execute("INSERT INTO users VALUES(:user_id, :user_name)", user)
        # db.execute(f"INSERT INTO users VALUES({values})", user)

		
        return "ok"
    except Exception as e:
        print(e)
        return {"info":str(e)} # cast to string
    finally:
        if "db" in locals(): db.close()




