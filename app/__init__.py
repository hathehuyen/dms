from flask import Flask
from flask_mongoengine import MongoEngine


# Define database
db = MongoEngine()

# Define the WSGI application object
app = Flask(__name__)
app.config.from_object('config')


# Default
@app.route("/", methods=['GET'])
def default():
    return "DMS"

# init database
db.init_app(app)

from app.mod_admin.controllers import mod_admin as admin
from app.mod_api.controllers import mod_api as api

# Register blueprint(s)
app.register_blueprint(admin)
app.register_blueprint(api)
