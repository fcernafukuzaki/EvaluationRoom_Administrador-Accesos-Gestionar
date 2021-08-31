from configs.flask_config import db
from object.usuario import Usuario


class UsuariosService():

    def get_usuarios(self):
        result = None
        try:
            usuarios = db.session.query(Usuario)

            if usuarios.count():
                result, code, message = usuarios, 200, 'Se encontró usuarios.'
            code, message = 404, 'No existen usuarios.'
        except Exception as e:
            code, message = 503, f'Hubo un error al obtener datos de usuarios en base de datos {e}'
        finally:
            print(message)
            return result, code, message
    
    def get_usuario(self, uid):
        result = None
        try:
            usuario = db.session.query(Usuario).filter(Usuario.idusuario==uid)
            
            if usuario.count():
                result, code, message = usuario.one(), 200, 'Se encontró usuario.'
            code, message = 404, 'No existe usuario.'
        except Exception as e:
            code, message = 503, f'Hubo un error al obtener datos de usuario {uid} en base de datos {e}'
        finally:
            print(message)
            return result, code, message
    
    def add_usuario(self, uid, nombre, email, activo, perfiles):
        result = None
        try:
            new_usuario = Usuario(uid, nombre, email, activo)
            db.session.add(new_usuario)
            db.session.commit()
            db.session.refresh(new_usuario)
            result = new_usuario.idusuario
            code, message = 200, 'Se registró usuario en base de datos.'
        except Exception as e:
            code, message = 503, f'Hubo un error al registrar usuario en base de datos {e}'
        finally:
            print(message)
            return result, code, message
    
    def update_usuario(self, uid, nombre, email, activo, perfiles):
        result = None
        try:
            update_usuario = Usuario.query.get((uid))
            update_usuario.nombre = nombre
            update_usuario.email = email
            update_usuario.activo = activo
            db.session.commit()
            result, code, message = uid, 200, 'Se actualizó usuario en base de datos.'
        except Exception as e:
            code, message = 503, f'Hubo un error al actualizar usuario en base de datos {e}'
        finally:
            print(message)
            return result, code, message