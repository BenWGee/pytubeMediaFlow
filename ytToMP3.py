import pytube as pyt
from datetime import date, datetime
import sys, os, logging, datetime, time, argseparse
from logging.handlers import RotatingFileHandler

# Path to project
path = os.getenv('')
#Create name
name = "" #Project Name
#Create version
version = "0.0.0"
#Set Log dir location
log_dir = path + "logs/" #Path to logs file
#Create PID
pid = "pid="+str(os.getpid())+";"
#LOGGING
## Create Logger
logger = logging.getLogger(name)
##Set Default Logging Level
logger.setLevel(logging.DEBUG)
## Create Console Handler
ch = logging.StreamHandler()
## Set ch log level
ch.setLevel(logging.DEBUG)
## Create a rotating local log file handler
#fh = logging.handlers.RotatingFileHandler(name+".log", mode='a', maxBytes=4096, backupCount=0, encoding=None, delay=False, errors=None)
fh = logging.handlers.RotatingFileHandler(log_dir+name+".log", mode='a', maxBytes=4096, backupCount=0, encoding=None, delay=False)
## Set fh log level
fh.setLevel(logging.DEBUG)
## Logging format options
stdFormat = logging.Formatter('[%(asctime)s] '+pid+' level="%(levelname)s"; name="%(name)s"; message="%(message)s";', datefmt='%Y-%m-%dT%H:%M:%S')
debugFormat = logging.Formatter('[%(asctime)s] '+pid+' level="%(levelname)s"; name="%(name)s"; function="%(funcName)s"; line="%(lineno)d"; message="%(message)s";', datefmt='%Y-%m-%dT%H:%M:%S')
## Add formatting to handlers
ch.setFormatter(debugFormat)
fh.setFormatter(debugFormat)
##Add log handlers
logger.addHandler(ch)
logger.addHandler(fh)

# End of Logging boilerplate

logger.info(os.path.basename(__file__) + " stated")

#===============================================================================
def downloadVideo(url,path,audioOnlyMode = True, ext = "mp3"):
    yt = pyt.YouTube(url)
    t = yt.streams.filter(only_audio = audioOnlyMode)
    print("Video is Downloading as " + str(yt.title) + ext)
    try:
        t[0].download(path)
        print("Video " + str(yt.title) + ext + " succesfully download")
    except:
        print("Video " + str(yt.title) + ext + " failed to download")
#===============================================================================

#===============================================================================
def videosByChannel(channelName, vidDate = datetime(1970,1,1)):
    links = []
    channel = pyt.Channel("https://www.youtube.com/c/" + channelName)
    for vid in channel.video_urls[:3]:
        yt = pyt.YouTube(vid)
        if yt.publish_date >= vidDate:
            links.append(vid)
    return links
#===============================================================================

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
# MAIN
if __name__ == "__main__":

    #GET COMMAND INPUT
    opts = argparse.ArgumentParser(prog=name, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    opts.add_argument(
        "-g", "--get",
        required=True,
        default=None,
        type=str,
        choices=['url', 'channel', 'playlist', 'file']
        help="String(get): Get list of videos by ."
    )

    opts.add_argument(
        "-u", "--url",
        required=False,
        default=None,
        type=str,
        help="String(get): Link to required video/channel/playlist ."
    )

    # BUILD ARGS ARRAY
    args = opts.parse_args()

    if args.report == "SomeValue":
		#doThis
    else:
		#doThat
        logger.info("INVALID REPORT TYPE REQUESTED")
