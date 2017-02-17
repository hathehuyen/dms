from flask import Flask
from flask_mongoengine import MongoEngine


# Define database
db = MongoEngine()

# Define the WSGI application object
app = Flask(__name__)
app.config.from_object('config')

# init database
db.init_app(app)

#from app.mod_admin.controllers import mod_admin as admin
# from app.mod_auth.controllers import mod_auth as auth
from app.mod_api.controllers import mod_api as api

# Register blueprint(s)
# app.register_blueprint(auth)
#app.register_blueprint(admin)
app.register_blueprint(api)

# replacing the following code that I had
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
# from common.models import *

# admin = Admin(app, name='microblog', template_mode='adminlte')
# admin.add_view(ModelView(MyModel, db.session))