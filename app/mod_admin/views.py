from flask_admin.contrib.mongoengine import ModelView


class DCView(ModelView):
    column_filters = ['name']


class HDDView(ModelView):
    column_filters = ['serial']
