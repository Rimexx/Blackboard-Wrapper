import requests
import json

with open('config.json', 'r') as f:
    config = json.load(f)

domain = "https://" + config["domain"] + "/"

s = requests.session()

login_data = {
"user_id": config["username"],
"password": config["password"],
}

response = s.post(domain + "webapps/login/", login_data)

response2 = s.get("https://uu.blackboard.com/bbcswebdav/pid-3322793-dt-content-rid-29760478_2/courses/BETA-2019-1-INFOB3SEC-V/huiswerk2.pdf")

print(response2.content)