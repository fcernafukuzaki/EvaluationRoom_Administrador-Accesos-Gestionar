from configs.flask_config import db
from object.perfil import Perfil


class PerfilesService():

    def get_perfiles(self):
        result = None
        try:
            perfiles = db.session.query(Perfil)

            if perfiles.count():
                result, code, message = perfiles, 200, 'Se encontró perfiles.'
            code, message = 404, 'No existen perfiles.'
        except Exception as e:
            code, message = 503, f'Hubo un error al obtener datos de perfiles en base de datos {e}'
        finally:
            print(message)
            return result, code, message
    
    def get_perfil(self, uid):
        result = None
        try:
            perfil = db.session.query(Perfil).filter(Perfil.idperfil==uid)
            
            if perfil.count():
                result, code, message = perfil.one(), 200, 'Se encontró perfil.'
            code, message = 404, 'No existe perfil.'
        except Exception as e:
            code, message = 503, f'Hubo un error al obtener datos de perfil {uid} en base de datos {e}'
        finally:
            print(message)
            return result, code, message
    
    def add_perfil(self, uid, nombre):
        result = None
        try:
            new_perfil = Perfil(uid, nombre)
            db.session.add(new_perfil)
            db.session.commit()
            db.session.refresh(new_perfil)
            result = new_perfil.idperfil
            code, message = 200, 'Se registró perfil en base de datos.'
        except Exception as e:
            code, message = 503, f'Hubo un error al registrar perfil en base de datos {e}'
        finally:
            print(message)
            return result, code, message
    
    def update_perfil(self, uid, nombre):
        result = None
        try:
            update_perfil = Perfil.query.get((uid))
            update_perfil.nombre = nombre
            db.session.commit()
            result, code, message = uid, 200, 'Se actualizó perfil en base de datos.'
        except Exception as e:
            code, message = 503, f'Hubo un error al actualizar perfil en base de datos {e}'
        finally:
            print(message)
            return result, code, message