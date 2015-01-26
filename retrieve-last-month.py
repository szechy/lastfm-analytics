import pylast

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
password = pylast.md5(keys.readline())

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)
user = network.get_user(username)

# retrieve last month's songs
#songs = user.get_recent_tracks();
n = 1

while True:
	tracks = user.get_recent_tracks(n)
	print tracks[0].playback_date
	print type(tracks[0].playback_date)