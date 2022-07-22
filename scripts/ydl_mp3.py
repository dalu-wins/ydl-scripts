import sys

import youtube_dl
from datetime import date

urls = ['https://music.youtube.com/playlist?list=PLB5axqo_BYe1P2z9uBZIkTdqrDXpcvrdW']
options = {
    'outtmpl': './downloads/audio/{directory}/%(title)s.%(ext)s'.format(directory=date.today()),
    'format': 'bestaudio/best',
    'addmetadata': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    },
    {
        'key': 'FFmpegMetadata',
    }],
}
with youtube_dl.YoutubeDL(options) as ydl:
    try:
        ydl.download(urls)
    except KeyboardInterrupt:
        sys.exit()