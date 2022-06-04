from apps import db
from datetime import datetime

class Story(db.Model):
    __tablename__ = 'story'

    id = db.Column(db.Integer, primary_key = True)
    s_key = db.Column(db.String(64))
    value = db.Column(db.String(64))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)