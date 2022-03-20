import pytube as pyt
from datetime import date, datetime
import sys, os, logging, datetime, time, argparse
from logging.handlers import RotatingFileHandler

# Path to project
path = ""#os.getenv('')
#Create name
name = "ytToLocal" #Project Name
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
def fileFormat():
    return
#===============================================================================

#===============================================================================
def checkVideoExists(url,path,ext):
    yt = pyt.YouTube(url)
    vidName = path + str(yt.title) + ext
    if os.path.exists(vidName):
        return True
    else:
        return False
#===============================================================================

#===============================================================================
def downloadVideo(url,path,audioOnlyMode = True, ext = "mp3"):
    yt = pyt.YouTube(url)
    t = yt.streams.filter(only_audio = audioOnlyMode)
    try:
        t[0].download(path)
        logger.info("Video " + str(yt.title) + ext + " succesfully download")
    except:
        logger.info("Video " + str(yt.title) + ext + " failed to download")
#===============================================================================

#===============================================================================
def videosByChannel(url, vidDate = datetime.datetime(1970,1,1)):
    links = []
    channel = pyt.Channel(url)
    for vid in channel.video_urls[:3]:
        yt = pyt.YouTube(vid)
        print(str(yt.title))
        if yt.publish_date >= vidDate:
            links.append(vid)
    return links
#===============================================================================

#===============================================================================
def videosByPlaylist(url):
    playlist = pyt.Playlist(url)
    links = [videoURL for videoURL in playlist.video_urls]
    return links
#===============================================================================

# MAIN
if __name__ == "__main__":

    #GET COMMAND INPUT
    opts = argparse.ArgumentParser(prog=name, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    opts.add_argument(
        "-g", "--get",
        required=True,
        default=None,
        type=str,
        choices=['url', 'channel', 'playlist', 'file'],
        help="String(get): Get list of videos by ."
    )

    opts.add_argument(
        "-u", "--url",
        required=False,
        default=None,
        type=str,
        help="String(url): Link to required video/channel/playlist ."
    )

    opts.add_argument(
        "-l", "--list",
        required=False,
        default=None,
        type=str,
        help="String(list): Path/name of text file list with delimited urls."
    )

    opts.add_argument(
        "-r", "--releaseDate",
        required=False,
        default=None,
        type=str,
        help="String(releaseDate): Look for videos after this date.(YYYY/MM/DD)"
    )

    opts.add_argument(
        "-d", "--delimiter",
        required=False,
        default="\n",
        type=str,
        help="String(delimiter): Character used to delimit video urls in file."
    )

    opts.add_argument(
        "-f", "--format",
        required=False,
        default="mp3",
        type=str,
        help="String(format): File format of saved content (mp3/4 recomended)."
    )

    opts.add_argument(
        "-a", "--audioOnly",
        required=False,
        default="y",
        choices = ["y","n"],
        type=str,
        help="String(audioOnly): toggle for audio only version of video."
    )



    # BUILD ARGS ARRAY
    args = opts.parse_args()
    valid = True

    if args.get == "file":
        logger.info("Gathering videos from " + str(args.file))
        urlList = readFile(args.file, args.delimiter)
    elif args.get == "url":
        logger.info("Gathering videos from " + str(args.get))
        urlList = [args.url]
    elif args.get == "channel":
        logger.info("Gathering videos from " + str(args.get))
        urlList = videosByChannel(args.url, datetime.datetime.strptime(args.releaseDate, '%Y/%m/%d'))
    elif args.get == "playlist":
        logger.info("Gathering videos from " + str(args.get))
        urlList = videosByPlaylist(args.url)
    else:
        valid = False
        logger.info("Invalid get option selected.")

    if valid:
        saveLoc = "media"
        audioOnlyMode = True
        if args.audioOnly == "y":
            saveLoc += "/audio"
        else:
            saveLoc += "/video"

        for link in urlList:
            if not checkVideoExists(link,saveLoc,args.format):
                downloadVideo(link,saveLoc,audioOnlyMode)
        logger.info("Review downloaded files at " + saveLoc)

    else:
        logger.info("Unable to download files.")

    logger.info(os.path.basename(__file__) + " finished")
