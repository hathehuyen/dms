from flask_admin.contrib.mongoengine import ModelView


class DCView(ModelView):
    column_filters = ['name']


class RackView(ModelView):
    column_filters = ['name']


class ServerView(ModelView):
    column_filters = ['mac']


class HDDView(ModelView):
    column_filters = ['serial']
