import pylast
import time
from datetime import datetime

#	Unique application values
keys = open('lastfm-info', 'r')
#	masking API keys in a local file, sorry everyone
TEMP_API_KEY = keys.readline()
API_KEY = TEMP_API_KEY.replace("\n", "")

TEMP_API_SECRET = keys.readline()
API_SECRET = TEMP_API_SECRET.replace("\n", "")

#	To perform a write operation, need to auth myself
username = "kenavt"
#	I think the fact I have to provide my password is ridiculous
temp_pass = keys.readline()
password = pylast.md5(temp_pass.replace("\n", ""))

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)
user = network.get_user(username)
# Enable caching - important for going past 200 songs
network.enable_caching()

# retrieve last 200 songs

# Next function only works 'properly' (returning Unix time) on Unix machines
# Sorry, Windows
current = time.time()

tracks = user.get_recent_tracks(200)

