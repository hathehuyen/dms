from admin_blueprint import AdminBlueprint
from app.common.models import DC, Rack, Server, HDD
from views import DCView, RackView, ServerView, HDDView


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_admin = AdminBlueprint('admin', __name__)

mod_admin.add_view(DCView(DC))
mod_admin.add_view(RackView(Rack))
mod_admin.add_view(ServerView(Server))
mod_admin.add_view(HDDView(HDD))

# Set the route and accepted methods
# @mod_admin.route('aa', methods=['GET', 'POST'])
# def index():
#     return 'Admin page'

# app = AdminBlueprint('admin', __name__, url_prefix='/admin', static_folder='static', static_url_path='/static/admin')
# mod_admin = AdminBlueprint('admin', __name__)
# app.add_view(ModelView(MyModel, db.session))
