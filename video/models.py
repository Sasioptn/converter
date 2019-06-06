from video import db


class Musics(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    link=db.Column(db.String)
    def __repr__(self):
        return f"Music('{self.link}')"
