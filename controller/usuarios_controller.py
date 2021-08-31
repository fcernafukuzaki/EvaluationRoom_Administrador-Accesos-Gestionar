from flask import jsonify, request
from flask_restful import Resource
from common.util import field_in_dict, get_response_body, str2bool
from service.authorizer_service import AuthorizerService
from service.usuarios_service import UsuariosService

authorizer_service = AuthorizerService()
usuarios_service = UsuariosService()

class UsuariosController(Resource):

    def get(self, uid=None):
        response_body = None
        try:
            token = request.headers['Authorization']
            email = request.headers['correoElectronico']

            flag, respuesta, codigo, _ = authorizer_service.validate_recruiter_identify(token, email)
            if flag:
                if not uid:
                    result, code, message = usuarios_service.get_usuarios()
                    response_body = {'usuarios':result} if result else None
                else:
                    result, code, message = usuarios_service.get_usuario(uid)
                    response_body = {'usuario':result} if result else None
                user_message = message
            else:
                code, message = 403, 'Operación inválida.'
                user_message = message
        except Exception as e:
            code, message = 503, f'Hubo un error al consultar usuarios {e}'
            user_message = message
        finally:
            if response_body:
                return get_response_body(code=200, message='OK', user_message=message, body=response_body), 200
            return get_response_body(code=code, message=message, user_message=user_message), code
    
    def post(self):
        response_body = None
        try:
            token = request.headers['Authorization']
            email = request.headers['correoElectronico']

            flag, respuesta, codigo, _ = authorizer_service.validate_recruiter_identify(token, email)
            if flag:
                input_json = request.json
                nombre = input_json['nombre'] if field_in_dict(input_json, 'nombre') else None
                correoelectronico = input_json['correoElectronico'] if field_in_dict(input_json, 'correoElectronico') else None
                activo = input_json['activo'] if field_in_dict(input_json, 'activo') else None
                perfiles = input_json['perfiles'] if field_in_dict(input_json, 'perfiles') else None

                result, code, message = usuarios_service.add_usuario(nombre, correoelectronico, activo, perfiles)
                response_body = {'usuario':result} if result else None
                user_message = message
            else:
                code, message = 403, 'Operación inválida.'
                user_message = 'Operación inválida.'
        except Exception as e:
            code, message = 503, f'Hubo un error al guardar usuario {e}'
            user_message = message
        finally:
            if response_body:
                return get_response_body(code=200, message='OK', user_message=message, body=response_body), 200
            return get_response_body(code=code, message=message, user_message=user_message), code
    
    def put(self, uid):
        response_body = None
        try:
            token = request.headers['Authorization']
            email = request.headers['correoElectronico']

            flag, respuesta, codigo, _ = authorizer_service.validate_recruiter_identify(token, email)
            if flag:
                input_json = request.json
                idusuario = input_json['idUsuario'] if field_in_dict(input_json, 'idUsuario') else None
                nombre = input_json['nombre'] if field_in_dict(input_json, 'nombre') else None
                correoelectronico = input_json['correoElectronico'] if field_in_dict(input_json, 'correoElectronico') else None
                activo = input_json['activo'] if field_in_dict(input_json, 'activo') else None
                perfiles = input_json['perfiles'] if field_in_dict(input_json, 'perfiles') else None

                result, code, message = usuarios_service.update_usuario(uid, nombre, correoelectronico, activo, perfiles)
                response_body = {'usuario':result} if result else None
            else:
                code, message = 403, 'Operación inválida.'
            user_message = message
        except Exception as e:
            code, message = 503, f'Hubo un error al actualizar usuario {e}'
            user_message = message
        finally:
            if response_body:
                return get_response_body(code=200, message='OK', user_message=message, body=response_body), 200
            return get_response_body(code=code, message=message, user_message=user_message), code