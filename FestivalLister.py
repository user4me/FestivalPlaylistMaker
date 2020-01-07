import pprint
import sys
import math
import spotipy
import spotipy.util as util

SPOTIPY_CLIENT_ID='SPOTIPY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET='SPOTIPY_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI='SPOTIPY_REDIRECT_URI'

errorlog = open('errorlog.txt','w')
lineupfile = open('lineup.txt','r')
lineup = [x.strip('\n') for x in lineupfile.readlines()]

numberofbands = len(lineup)
tracks = []

if len(sys.argv) > 2:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
else:
    print("Usage: %s username playlist_id ..." % (sys.argv[0],))
    sys.exit()
index = 0
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri = SPOTIPY_REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    for x in range(0,len(lineup)):
        results = sp.search(q=str(lineup[x]), limit=3)
        for i, t in enumerate(results['tracks']['items']):
            tracks.append(str(t['id'].strip( 'u' )))
            print("adding ",str(t['id'].strip( 'u' )),t['name'])
    while tracks:
        print "adding song",index
        index = index + 1
        try:
			results = sp.user_playlist_add_tracks(username, playlist_id, tracks[:1], position=None)
        except:
            print "error"
        tracks = tracks[1:]

else:
    print("Can't get token for", username)


print "Playlist Complete!"
