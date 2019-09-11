import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
from flask import Flask, request
import json

app = Flask(__name__)

BASE_URL = "https://api.freshbooks.com"

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@app.route("/TestAuthentication")
def oauth_session():
    auth_code = request.args.get('code')
    auth_data = { 
        "grant_type": "authorization_code",
        "client_secret": os.getenv('CLIENT_SECRET'),
        "code": auth_code,
        "client_id": os.getenv('CLIENT_ID'),
        "redirect_uri": os.getenv('REDIRECT_URL')
    }
    auth_request = requests.post(BASE_URL + "/auth/oauth/token", json = auth_data)
    access_token_dict = json.loads(auth_request.text)
    headers = {"Authorization":"Bearer " + access_token_dict["access_token"]}
    identity_request = requests.get(BASE_URL + "/auth/api/v1/users/me", headers=headers)
    identity_dict = json.loads(identity_request.text)
    profile_dict = identity_dict["response"]["profile"]
    response = "You have successfully logged in for " + profile_dict["first_name"] + " " + profile_dict["last_name"]
    return response

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
