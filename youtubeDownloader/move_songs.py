import os
import shutil
import re
import sys


def remove_gibberish(filename):
    pattern = re.compile(r'''(
    (-\S.*)
    (\.mp3)
    )''', re.VERBOSE)

    match_obj = pattern.search(filename)

    if match_obj:
        to_replace = match_obj.group(2)
        replace_with = ''
        filename = filename.replace(to_replace, replace_with)

    return filename


def move_mp3s(source, destination):
    os.chdir(source)
    current_directory_content = os.listdir()

    for file in current_directory_content:
        if file.endswith('.mp3'):
            old_file = file
            file = remove_gibberish(file)

            src = os.path.join(source, old_file)
            dst = os.path.join(destination, file)

            print('moving %s to %s' % (src, dst))
            shutil.move(src, dst)


if __name__ == '__main__':
    # sourcePath: path to the directory where your songs are downloaded (by default it is project's root directory)
    sourcePath = sys.argv[1]
    # destinationPath: path to where you want your songs to be moved after gibberish is removed from their name
    destinationPath = sys.argv[2]

    move_mp3s(sourcePath, destinationPath)
