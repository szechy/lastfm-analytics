import pylast
import time

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
#password = pylast.md5(keys.readline())
temp_pass = keys.readline()
password = pylast.md5(temp_pass.replace("\n", ""))

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)
user = network.get_user(username)

# retrieve last month's songs
n = 2
time = 31	# as in, 31 days

while True:
tracks = user.get_recent_tracks(n)
	# two options to retrieve time
	# we'll use the timestamp method, but strptime() method works
	# date = time.strptime(tracks[-1].playback_date, "%d %b %Y, %H:%M")
	timestamp = time.gmtime(float(tracks[-1].timestamp))
	print date.tm_year
	print timestamp.tm_year
	print date.tm_mon
	print timestamp.tm_mon
	print date.tm_mday