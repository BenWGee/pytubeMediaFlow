# pytubeMediaFlow
Download YouTube videos based on channel, date, URL, playlist etc and move them
to some file location.

# Disclaimer

This script is for educational purposes and does not endorse downloading YouTube
 videos legitimately.

# Purpose

This project aims to assemble an entire media flow based on the pytube library.
The files within contain several functions for the gathering and downloading of
YouTube content.

ytToLocal.py is the script doing the heavy lifting here, searching for videos,
downloading their content.

In the sampleBashFiles folder you will find 4 example scripts, which will
download videos from a channel, file, playlist and url respectively. Simply
change the --url parameter to your chosen url (or the --list parameter if you
  are importing URLs from your own premade list). There are other parameters too
please see --help for explanations on what each parameter is ore see below.

The script by default will generate a couple folders, a logs folder which will
house a record of all files downloaded as well as any errors. Secondly a media
folder will be created. Inside this there will be an audio and video folder.
Files that have been downloaded with the --audioOnly set to 'y' will show up in
the audio folder, while other files will be sent to the video folder.

# Parameters

usage: ytToLocal [-h] -g {url,channel,playlist,file} [-u URL] [-l LIST] [-r RELEASEDATE] [-d DELIMITER] [-f FORMAT]
                 [-a {y,n}]

options:
  -h, --help            show this help message and exit
  -g {url,channel,playlist,file}, --get {url,channel,playlist,file}
                        String(get): Get list of videos by . (default: None)
  -u URL, --url URL     String(url): Link to required video/channel/playlist . (default: None)
  -l LIST, --list LIST  String(list): Path/name of text file list with delimited urls. (default: None)
  -r RELEASEDATE, --releaseDate RELEASEDATE
                        String(releaseDate): Look for videos after this date.(YYYY/MM/DD) (default: None)
  -d DELIMITER, --delimiter DELIMITER
                        String(delimiter): Character used to delimit video urls in file. (default: )
  -f FORMAT, --format FORMAT
                        String(format): File format of saved content (mp3/4 recomended). (default: mp3)
  -a {y,n}, --audioOnly {y,n}
                        String(audioOnly): toggle for audio only version of video. (default: y)

## Notes on parameters

If -g is set to url, channel, or playlist then you should supply a -u value

If -g is set to file a value for -l and -d should be set

If -g is set to channel it is reconnected you set a value for -r or else it will
attempt to download all videos since 1970 for that channel (ie all videos). This
would at best take a long time and at worst raise some potential red flags with
YouTube.

# TODO

[X] Add processesing of command line arguments
[X] Multiple options for how to gather URLs eg: Channel name, date, from file
* Cronjob to automate gathering
[X] Check if video is already downloaded before downloading
* Put downloaded files into different folder based on something eg: time, channel name
* Have naming convention for naming files eg: SomeGuys Lets Play Part 1, ensure all parts stay in order some how
* Script to move files from download folder tosome end location
