from video import app
from flask import redirect,render_template,url_for
from .forms import DownloadForm
import youtube_dl
@app.route("/", methods=['GET','POST'])
def home():
    data = []
    form = DownloadForm()
    if form.validate_on_submit():
        a = form.link.data;
        data.append(a)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320', }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([a])
    return render_template('home.html', form = form,data = data)