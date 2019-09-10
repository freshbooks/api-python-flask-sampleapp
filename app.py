import requests
from flask import Flask, request
import json

app = Flask(__name__)

session = requests.Session()

@app.route("/OauthSession")
def OauthSession():
    session.headers.clear()
    auth_code = request.args.get('code')
    auth_data = { "grant_type": "authorization_code",
    "client_secret": "",
    "code": auth_code,
    "client_id": "",
    "redirect_uri": ""}
    auth_request = session.post("https://api.freshbooks.com/auth/oauth/token", json = auth_data)
    access_token_dict = json.loads(auth_request.text)
    session.headers.update({"Authorization":"Bearer "+ access_token_dict["access_token"]})
    return access_token_dict

@app.route("/Aboutme")
def Aboutme():
    identity_request = session.get("https://api.freshbooks.com/auth/api/v1/users/me")
    identity_dict = json.loads(identity_request.text)
    print(identity_dict)
    return identity_dict

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
