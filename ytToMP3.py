import pytube as pyt
from datetime import date, datetime

def downloadVideo(url,path,audioOnlyMode = True, ext = "mp3"):
    yt = pyt.YouTube(url)
    t = yt.streams.filter(only_audio = audioOnlyMode)
    print("Video is Downloading as " + str(yt.title) + ext)
    try:
        t[0].download(path)
        print("Video " + str(yt.title) + ext + " succesfully download")
    except:
        print("Video " + str(yt.title) + ext + " failed to download")

def videosByChannel(channelName, vidDate = datetime(1970,1,1)):
    links = []
    channel = pyt.Channel("https://www.youtube.com/c/" + channelName)
    for vid in channel.video_urls[:3]:
        yt = pyt.YouTube(vid)
        if yt.publish_date >= vidDate:
            links.append(vid)
    return links

# def videoByURLList():
#     return

playlist = pyt.Playlist("")
urls = [videoURL for videoURL in playlist.video_urls]


path = "media"
audioOnlyMode = True
if audioOnlyMode:
    path += "/audio"
else:
    path += "/video"

for link in urls:
    print(link)
    downloadVideo(link,path,audioOnlyMode)

print("Done")