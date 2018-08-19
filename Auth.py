from requests_oauthlib import OAuth2Session
import Config

wunderlist = OAuth2Session()
wunderlist.headers['X-Client-ID'] = Config.CLIENT_ID
wunderlist.headers['X-Access-Token'] = Config.ACCESS_TOKEN
wunderlist.headers['Content-Type'] = 'application/json'
