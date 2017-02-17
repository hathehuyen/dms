from app import db
from datetime import datetime


class DC(db.Document):
    name = db.StringField(max_length=255)


class Rack(db.Document):
    name = db.StringField(max_length=255)
    dc = db.ReferenceField(DC, reverse_delete_rule=3)


class Server(db.Document):
    name = db.StringField(max_length=255)
    ip = db.StringField(max_length=40)
    mac = db.StringField(max_length=20)
    rack = db.ReferenceField(Rack, reverse_delete_rule=3)


class HDD(db.Document):
    serial = db.StringField(unique=True, max_length=40)
    capacity = db.FloatField()
    used = db.FloatField()
    server = db.ReferenceField(Server, reverse_delete_rule=3)
    status = db.StringField(max_length=255)
    location = db.StringField(max_length=10)
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.utcnow())

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.utcnow()
        self.modified_date = datetime.utcnow()
        return super(HDD, self).save(*args, **kwargs)
