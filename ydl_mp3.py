import youtube_dl
from datetime import date

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'
options = {
    'outtmpl': './downloads/audio/{directory}/%(title)s-%(artist)s.%(ext)s'.format(directory=date.today()),
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])
