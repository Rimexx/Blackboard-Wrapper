import requests
import json

with open('config.json', 'r') as f:
    config = json.load(f)

print(config["domain"])

domain = "https://" + config["domain"] + "/"

s = requests.session()

login_data = {
"user_id": config["username"],
"password": config["password"],
}

response = s.post(domain + "webapps/login/", login_data)

print(response.content)