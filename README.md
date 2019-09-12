# api-python-flask-sampleapp

This Flask application demostrates how developers can use the **FreshBooks API** to let users login to their application through **OAuth2** then access and modify the users' information using the endpoints provided to them.

## Setting up you developer account

- Create a new FreshBooks account by signing up on the [signup page](https://my.freshbooks.com/#/signup).
- Visit the [developer page](https://my.freshbooks.com/#/developer) and create a new app.
> Make sure that your redirect uri ends with **/TestAuthentication**, since this will be the endpoint used to verify that you have successfully set up your application on FresbBooks [developer page](https://my.freshbooks.com/#/developer). For example,
```
https://localhost:5000/TestAuthentication
```
- Once you have created the application, keep the [developer page](https://my.freshbooks.com/#/developer) open as you will need it for the next step.

## Running the Flask app

- Make sure you have [Python3](https://www.python.org/downloads/) installed on your computer.
- Clone this repo into your computer.
- Create a new **.env** file in the root folder of the project. The .env file should at least contain the following variables
```
CLIENT_SECRET='<YOUR-CLIENT-SECRET>'
CLIENT_ID='<YOUR-CLIENT-ID>'
REDIRECT_URL='<YOUR-REDIRECT-URI>'
```
The values for these variables are available on the [developer page](https://my.freshbooks.com/#/developer)
- Install all the dependencies for this project as mentioned on the **requirements.txt**.
```
pip install -r requirements.txt
```
- Run the app using the Flask command.
```
flask run --cert=adhoc
```
- Click on the **Authorizaton URL** for you application available on the [developer page](https://my.freshbooks.com/#/developer)
- Login to the FreshBooks application using the following credentials
```
Email:
Password:
```
If you have correctly set up you application on **FreshBooks** and entered your credentials on the **.env** file you should get the following output.
```
You have successfully logged in for First Last
```

If you can see the above output, congrats you can now start building your application using the **Freshbooks API**. If you do not see the message, you will have to go over the instructions again.

Hope you have a fun hackathon experience.

**Cheers!**