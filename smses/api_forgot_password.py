from bottle import post, response
import x
import uuid
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##############################
@post("/api-forgot-password")
def _():
	try:
		user_email = x.validate_user_email()
		user_password_reset_key = str(uuid.uuid4()).replace("-","")
		db = x.db()
		rows_affected = db.execute(f"""
			UPDATE users 
			SET user_password_reset_key = ?
			WHERE user_email = ?
		""", (user_password_reset_key, user_email)).rowcount
		if not rows_affected: raise Exception(400, "user not found")
		db.commit()	

		message = MIMEMultipart("alternative")
		message["Subject"] = "smses password reset"
		message["From"] = x.EMAIL_FROM
		message["To"] = user_email

		# Create the plain-text and HTML version of your message
		text = f"""\
		Hi,
		To reset your password, send a POST request to:
		https://YOUR_USERNAME.eu.pythonanywhere.com/api-reset-password
		and use the user_password_reset_key: {user_password_reset_key}
		"""
		html = f"""\
		<html>
		<body>
			Hi,
			To reset your password, send a POST request to:
			https://YOUR_USERNAME.eu.pythonanywhere.com/api-reset-password
			and use the user_password_reset_key: {user_password_reset_key}
		</body>
		</html>
		"""

		# Turn these into plain/html MIMEText objects
		part1 = MIMEText(text, "plain")
		part2 = MIMEText(html, "html")

		# Add HTML/plain-text parts to MIMEMultipart message
		# The email client will try to render the last part first
		message.attach(part1)
		message.attach(part2)

		# Create secure connection with server and send email
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(x.EMAIL_FROM, x.EMAIL_SECRET)
			server.sendmail(
				x.EMAIL_FROM, user_email, message.as_string()
			)
			
		return {
			"info" : "Check your email to reset your password"
		}
	except Exception as e:
		print(e)
		if "db" in locals(): db.rollback()
		try: # Controlled exception, usually comming from the x file
			response.status = e.args[0]
			return {"info":e.args[1]}
		except: # Something unknown went wrong		
			# unknown scenario
			response.status = 500
			return {"info":str(e)}
	finally:
		if "db" in locals(): db.close()
