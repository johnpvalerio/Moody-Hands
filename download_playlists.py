from subprocess import call
Playlists = {'Mood0':'https://www.youtube.com/playlist?list=PLiU3RtKBcY8KvVxCrsNel4Rl8VCjCAWQS', 
'Mood4':'https://www.youtube.com/watch?v=HMnrl0tmd3k&list=PLiU3RtKBcY8JHo-acuAvhKZmQIfknGGpR'} 

for playlist in Playlists.keys():
    command = "youtube-dl -x --audio-format wav -o %(playlist)s/%(playlist_index)s-%(title)s.%(ext)s "+Playlists[playlist]
    call(command.split(), shell=False)

