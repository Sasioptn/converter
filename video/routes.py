from video import app
from flask import render_template
from .forms import DownloadForm
from .models import Musics
from video import db

from.secondary_functions import download_mp3
@app.route("/", methods=['GET','POST'])
def home():
    data = []
    form = DownloadForm()
    if form.validate_on_submit():
        new_link = form.link.data;
        new_music = Musics(link=form.link.data)
        db.session.add(new_music)
        db.session.commit()
        data = Musics.query.all()
        return render_template('home.html', form = form,data = data,new_link = form.link.data)
    return render_template('home.html', form = form,data = data)

@app.route("/download", methods=['GET','POST'])
def download():
    music = Musics.query.all()
    last = music[0]
    result = download_mp3(last.link)
    return "Скачано!!!"

