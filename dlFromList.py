from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv
import requests
import webbrowser
import settings
import errno

# globals:

url_search = 'https://www.googleapis.com/youtube/v3/search'
url_watch = 'https://www.youtube.com/watch?v='
cur_dir = os.getcwd()


def get_url_id(title):
    global url_search
    params = {
        'part': 'snippet',
        'q': title,
        'key': settings.KEY,
        'maxResults': 1,
        'type': 'video'
    }
    res = requests.get(url_search, params=params)
    url_id = res.json()['items'][0]['id']['videoId']
    try:
        title = res.json()['items'][0]['snippet']['title']
        if 'official' not in title.lower():
            print('not official ' + title)
    except:
        print('no title')
    return url_id


def main():
    song_list, folder = input_validation()

    # youtube-dl options download
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with open(song_list, 'r') as f:  # open songs list file
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for song_title in f:
                song_title = song_title.strip()
                song_url = get_url_id(song_title)
                ydl.download([song_url])


def input_validation():
    if len(argv) == 3:
        songs_list = argv[1]
        folder = argv[2]
    elif len(argv) < 2:
        # raise IndexError('please enter file name')
        songs_list = input('please chose a song list (with extension)')
        folder = input('please specify an output folder for downloading')
    else:
        raise IndexError('this scripts get 0 or 2 arguments!')

    if not os.path.isfile(songs_list):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), songs_list)

    if not os.path.isdir(folder):
        os.mkdir(folder)

    return songs_list, folder


if __name__ == '__main__':
    main()
