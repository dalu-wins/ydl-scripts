import youtube_dl
from datetime import date

url = [input("Enter url:\t")]
options = {
        'outtmpl': '../downloads/video/{directory}/%(title)s.%(ext)s'.format(directory=date.today()),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
        'addmetadata': True,
        'ignoreerrors': True,
        'continuedl': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }, {
            'key': 'FFmpegMetadata',
        }],
    }

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(url)