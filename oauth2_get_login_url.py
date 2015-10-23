import os
from rauth import OAuth2Service

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

print( login_url )
