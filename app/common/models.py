from app import db


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
    used = db.FloatField(max_length=40)
    server = db.ReferenceField(Server, reverse_delete_rule=3)
    status = db.StringField(max_length=40)
