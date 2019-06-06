from .models import Musics
from video import db
import youtube_dl


def download_mp3(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320', }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return "sdelano"


def get_all():
    sounds = Musics.query.all()
    return sounds
