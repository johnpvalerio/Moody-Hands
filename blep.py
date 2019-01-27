from bs4 import BeautifulSoup
import requests
Playlists = {'Mood0':'https://www.youtube.com/playlist?list=PLiU3RtKBcY8KvVxCrsNel4Rl8VCjCAWQS', 'Mood4':'https://www.youtube.com/watch?v=HMnrl0tmd3k&list=PLiU3RtKBcY8JHo-acuAvhKZmQIfknGGpR'} 
selected_playlist = list()
#random_ytlink
class YoutubeLink:
    def __init__(self,t,l):
        self.title = t
        self.link = l
    def __str__(self):
        return 'Title: ' + self.title + '\nLink: '+ self.link

def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            #print(link.string.strip())
            #print(domain + href + '\n') 
            selected_playlist.append(YoutubeLink(link.string.strip(),(domain+href)))
getPlaylistLinks(Playlists['Mood0'])

print(str(selected_playlist[1]))