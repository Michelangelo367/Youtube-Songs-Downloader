import os
import sys


def rename_file(original_file_name, dist_folder):
    file_name, file_extension = os.path.splitext(original_file_name)
    # remove id
    file = file_name.split('-')
    title = file[1]
    artist = file[0]

    # removing parenthesis
    bad = "()[]<>"
    for c in bad:
        title = title.replace(c, '')
    # remove irrelevant description
    title = title.replace('Official Music Video', '')
    title = title.replace('Official Video', '')
    title = title.strip()
    artist = artist.strip()

    new_file_name = title + ' - ' + artist + file_extension
    os.rename(original_file_name, os.path.join('../', dist_folder, new_file_name))


if os.path.exists('Songs'):
    # dist folder
    if len(sys.argv) < 2:
        dist = 'Songs'
    else:
        dist = sys.argv[1]
        if not os.path.exists(dist):
            os.mkdir(dist)

    # current folder - 'Songs'
    os.chdir('Songs')
    for fileName in os.listdir(os.getcwd()):
        rename_file(fileName, dist)
