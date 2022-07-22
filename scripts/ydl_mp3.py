import youtube_dl
from datetime import date

urls = [input("Enter playlist or video url:\t")]
options = {
    'outtmpl': './downloads/audio/{directory}/%(title)s.%(ext)s'.format(directory=date.today()),
    'format': 'bestaudio/best',
    'addmetadata': True,
    'ignoreerrors': True,
    'continuedl': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }, {
        'key': 'FFmpegMetadata',
    }],
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(urls)
