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


def start_download():
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download(url)


if __name__ == '__main__':
    add_url()
    set_options()
    start_download()