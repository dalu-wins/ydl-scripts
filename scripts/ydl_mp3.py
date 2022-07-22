import youtube_dl
from datetime import date

global url
global options


def add_url():
    global url
    url.append(input("Enter url:\t"))


def set_options():
    global options
    options = {
        'outtmpl': './downloads/audio/{directory}/%(title)s.%(ext)s'.format(directory=date.today()),  # custom download path
        'format': 'bestaudio/best',
        'addmetadata': True,
        'ignoreerrors': True,  # skip to next song if error occurs
        'continuedl': True,  # continue download if cancelled before
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # only audio
            'preferredcodec': 'mp3',  # as .mp3
            'preferredquality': '192',  # best quality preferred
        }, {
            'key': 'FFmpegMetadata',  # needed for metadata saving
        }],
    }


def start_download():
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download(url)


if __name__ == '__main__':
    add_url()
    set_options()
    start_download()
