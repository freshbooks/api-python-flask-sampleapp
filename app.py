import os
from os import path
from dotenv import load_dotenv
from flask import Flask, request
import requests

app = Flask(__name__)


BASE_URL = "https://api.freshbooks.com"

dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


@app.route("/TestAuthentication")
def test_authentication():
    auth_code = request.args.get('code')
    auth_data = {
        "grant_type": "authorization_code",
        "client_secret": os.getenv('CLIENT_SECRET'),
        "code": auth_code,
        "client_id": os.getenv('CLIENT_ID'),
        "redirect_uri": os.getenv('REDIRECT_URL')
    }

    auth_request = requests.post(BASE_URL + "/auth/oauth/token", json=auth_data)
    access_token_dict = auth_request.json()

    headers = {"Authorization": "Bearer " + access_token_dict["access_token"]}
    identity_request = requests.get(BASE_URL + "/auth/api/v1/users/me", headers=headers)
    identity_dict = identity_request.json()
    profile_dict = identity_dict["response"]["profile"]

    response = "You have successfully logged in for {} {}".format(
        profile_dict["first_name"], profile_dict["last_name"])
    return response


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
