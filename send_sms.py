import requests

print("ok")
user_api_key = "YOU KEY"
sms_message = "This is great"
sms_to_phone = "YOUR PHONE"

payload = {	"user_api_key":user_api_key, 
			"sms_message":sms_message, 
			"sms_to_phone":sms_to_phone}

res = requests.post('https://smses.eu.pythonanywhere.com/api-send-sms', data=payload)
print(res)
print(res.text)



