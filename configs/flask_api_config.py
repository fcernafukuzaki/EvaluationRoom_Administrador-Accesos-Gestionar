from .flask_config import api
from controller.usuarios_controller import *
from controller.perfiles_controller import *

api.add_resource(UsuariosController, 
    '/usuarios/',
    '/usuarios/<int:uid>')

api.add_resource(PerfilesController, 
    '/perfiles/',
    '/perfiles/<int:uid>')