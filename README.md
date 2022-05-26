# youtube_mp3_downloader
 A YouTube MP3 downloader API

To install the requirements run the following command in the project root directory: 
pip install -r requirements.txt

The "download_songs.py" script is ran with two arguments; a path to the file containing the songs and the type of the file content which describes whether file contains urls to the songs (if you want specific version of the song) or the song names, hence 2 possible values for this argument: songs and urls.
Examples: 
python download_songs.py ./songs.txt urls
python download_songs.py ./songs.txt songs

Since the library downloads the songs to the directory containing the script and all of the downloaded songs have some gibberish at the end of their names, you may want to remove and possibly move those.
The "remove_gibberish.py" script can be run with either zero or one command line argument. If you only wish to only remove the gibberish and leave the songs in the project root folder, run it with no additional arguments. If you also wish to move songs elsewhere pass the argument that represents the path to the directory to which you want to move the songs.
Examples:
python remove_gibberish.py
python remove_gibberish.py ./some/else/path
