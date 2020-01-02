# YouTube Downloader

This mini project, is all about making my life bit easier.

given a list of songs (youtube URL) on a txt file, this code will download 
the song as video format (mp4 I think), and then by using ffmpeg - convert to mp3.

### srequirements:
- youtube_dl (python package)
- ffmpeg (formatting from video to audio)
- python 3.6 >=

##### files:
* dlFormList.py - gets an argument: songs.txt - saves the mp3 files in Songs folder
* renaming.py - gets an argument: dist folder, remove irrelevant stuff from title (e.g youtube id, parenthesis, "official video")

    The dist folder rgument is for saving the file in another folder.


