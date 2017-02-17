from flask_admin.contrib.mongoengine import ModelView


class HDDView(ModelView):
    column_filters = ['serial']
