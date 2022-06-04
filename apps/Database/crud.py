from apps.Database import models
from apps import db

def add_record(user, value):
    record = models.Story()
    record.s_key = user
    record.value = value
    db.session.add(record)
    db.session.commit()

def get_records(user):
    query = db.session.query(models.Story).filter(models.Story.s_key == user)
    query = query.order_by(models.Story.created_on)
    r = query.all()
    return r