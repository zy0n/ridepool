# Copy this file into secrets.py and set keys, secrets and scopes.

# Details of your community
community = {
	'name': 'Tanglewood Forest',
	'address': 'Austin, TX',
	'lat': 30.184655,
	'lng': -97.833937
}

# This is a session secret key used by webapp2 framework.
# Get 'a random and long string' from here:
# http://clsc.net/tools/random-string-generator.php
# or execute this from a python shell: import os; os.urandom(64)
SESSION_KEY = 'c2xbj60d10l9gd76ts7pfm12wj8q432f'

# Google APIs
GOOGLE_APP_ID = '628022227548-q17j4kp7r914eomjmnqkcogd8nirceva.apps.googleusercontent.com'
GOOGLE_APP_SECRET = 'RLdzy35nWbvcOD1elzYKmXWS'

# Facebook auth apis
FACEBOOK_APP_ID = null
FACEBOOK_APP_SECRET = null

# https://dev.twitter.com/apps
TWITTER_CONSUMER_KEY = null
TWITTER_CONSUMER_SECRET = null


# config that summarizes the above
# do not modify the following
AUTH_CONFIG = {
  # OAuth 2.0 providers
  'google'      : (GOOGLE_APP_ID, GOOGLE_APP_SECRET,
                  'https://www.googleapis.com/auth/userinfo.profile'),

  'facebook'    : (FACEBOOK_APP_ID, FACEBOOK_APP_SECRET,
                  'user_about_me'),

  # OAuth 1.0 providers don't have scopes
  'twitter'     : (TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)

  # OpenID doesn't need any key/secret
}
