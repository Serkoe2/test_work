from apps import db

class Story(db.Model):
    __tablename__ = 'story'

    id = db.Column(db.Integer, primary_key = True)
    s_key = db.Column(db.String(64))
    value = db.Column(db.String(64))