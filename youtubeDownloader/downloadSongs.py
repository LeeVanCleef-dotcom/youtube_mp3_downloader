from __future__ import unicode_literals
import urllib.request
import urllib.parse
import re
import youtube_dl


def load_songs(file_path):
    with open(file_path, encoding='utf-8') as file:
        data = file.readlines()
    return data


def download_songs(url_list):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for url in url_list:
            ydl.download([url])


def get_urls(song_list):
    urls = [get_song_url(song) for song in song_list]

    return urls


def get_song_url(song_name):
    query_string = urllib.parse.urlencode({"search_query": song_name})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    video_id = re.search(r'/watch\?v=(.{11})', html_content.read().decode())
    url = "http://www.youtube.com/watch?v=" + video_id.group(1)

    return url


if __name__ == '__main__':
    # filePath: path of songs containing .txt file
    filePath = r''

    songs = load_songs(filePath)
    songs = list(map(lambda song: song.replace('\n', ''), songs))

    song_urls = get_urls(songs)

    download_songs(song_urls)
