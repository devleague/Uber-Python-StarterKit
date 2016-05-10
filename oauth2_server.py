import os
import requests
from rauth import OAuth2Service
from flask import Flask, request, redirect
app = Flask(__name__)
uber_api_url = 'https://sandbox-api.uber.com/v1'

@app.route('/oauth/login')
def login():

  uber_api = OAuth2Service(
    client_id=os.environ['UBER_CLIENT_ID'],
    client_secret=os.environ['UBER_CLIENT_SECRET'],
    name='StarterKit', # put your app name here
    authorize_url='https://login.uber.com/oauth/authorize',
    access_token_url='https://login.uber.com/oauth/token',
    base_url='https://sandbox-api.uber.com/v1/',
  )

  parameters = {
    'response_type': 'code',
    'redirect_uri': 'http://localhost:8080/oauth/cb', # your callback url for oauth2 step 2
    'scope': 'profile',
  }

  # Redirect user here to authorize your application
  login_url = uber_api.get_authorize_url(**parameters)
  return redirect(login_url)

@app.route('/oauth/cb')
def cb():

  parameters = {
    'redirect_uri': 'http://localhost:8080/oauth/cb',
    'code': request.args.get('code'),
    'grant_type': 'authorization_code',
  }

  response = requests.post(
    'https://login.uber.com/oauth/token',
    auth=(
      os.environ['UBER_CLIENT_ID'],
      os.environ['UBER_CLIENT_SECRET'],
    ),
    data=parameters,
  )

  # This access_token is what we'll use to make requests in the following steps
  access_token = response.json().get('access_token')
  return access_token

@app.route('/profile')
def profile():

  access_token = request.args.get('access_token')

  response = requests.get(
    uber_api_url + '/me',
    headers={
        'Authorization': 'Bearer %s' % access_token
    }
  )

  data = response.text
  return data

if __name__ == "__main__":
  app.run( host=os.getenv('HOST', '0.0.0.0'), port=int( os.getenv('PORT',8080) ), debug=True )
