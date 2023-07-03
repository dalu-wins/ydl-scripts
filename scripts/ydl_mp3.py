import yt_dlp as downloader
from datetime import date

url = [input("Enter url:\t")]
options = {
    'outtmpl': '../downloads/audio/{directory}/%(title)s.%(ext)s'.format(directory=date.today()),  # custom download path
    'format': 'bestaudio/best',
    'addmetadata': True,
    'ignoreerrors': True,       # skip to next song if error occurs
    'continuedl': True,         # continue download if cancelled before
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',    # only audio
        'preferredcodec': 'mp3',        # as .mp3
        'preferredquality': '192',      # best quality preferred
    }, {
        'key': 'FFmpegMetadata',  # needed for metadata saving
    }],
}

with downloader.YoutubeDL(options) as ydl:
    ydl.download(url)

