# YouTube Downloader

This mini project, is all about making my life a bit easier.

given a list of songs (title/artist) in a file, using yoytube DATA API, for search the best result.\
with this result - fetching the videoID, and download it with youtube-dl package.\
after downloading the file "ffmpeg" will convert the file to mp3 (and remove the original file).

### requirements:
- youtube_dl (python package
- ffmpeg (formatting from video to audio)
- python 3.6 >=
- youtube data API key

### run:
it can be run with 2 (optional) arguments: src_songs_list, dst_folder when:\
src_songs_list: the songs list file (e.g top_100_hits.txt)
dst_folder: distention folder for the mp3 files

**when running without arguments - you will need to enter those args manually**

    python3 dlFromList src_songs_list dst_folder
or
  
    python3 dlFromList
    
