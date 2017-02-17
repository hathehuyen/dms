from flask_admin.contrib.mongoengine import ModelView


class DCView(ModelView):
    column_filters = ['name']


class RackView(ModelView):
    column_filters = ['name']
    form_ajax_refs = {
        'dc': {
            'fields': ['name']
        }
    }


class ServerView(ModelView):
    column_filters = ['mac']
    form_ajax_refs = {
        'rack': {
            'fields': ['name']
        }
    }


class HDDView(ModelView):
    column_filters = ['serial']
    form_ajax_refs = {
        'server': {
            'fields': ['mac']
        }
    }
