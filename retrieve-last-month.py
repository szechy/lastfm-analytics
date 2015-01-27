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

# retrieve last month's songs
n = 2
duration = input('How many days to go back to search your Last.fm data? ')
last_n = n
print "Thanks!"
duration = duration*24*60*60	# as in, 31 days

# Next function only works 'properly' (returning Unix time) on Unix machines
# Sorry, Windows
current = time.time()
goal = current - duration;

tracks = user.get_recent_tracks(n)
tracks = user.get_recent_tracks(202)

while True:
	# two options to retrieve time
	# we'll use the timestamp method, but strptime() method works
	date = time.strptime(tracks[-1].playback_date, "%d %b %Y, %H:%M")
	last_time = float(tracks[-1].timestamp)
	print last_time
	print goal
	print n
	print date.tm_mon
	print date.tm_mday
	# We haven't gone far enough back
	if(last_time > goal):
		last_n = n
		n *= 2;
		tracks = user.get_recent_tracks(n)
	# We've gone back far enough
	else: 
		# need to go through tracks to find the last one before goal
		while last_n != n:
			if tracks[last_n].timestamp > goal:
				last_n += 1
			else:
				break

print last_n
