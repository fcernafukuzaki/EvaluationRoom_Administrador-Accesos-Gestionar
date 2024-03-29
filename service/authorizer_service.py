import json
from common.util import invoke_api


class AuthorizerService():

    def validate_recruiter_identify(self, token, email):
        if email and token:
            url = 'https://evaluationroom.herokuapp.com/reclutador_identificador_validar'
            data = {"Authorization": token, "correoelectronico": email}
            encoded_data = json.dumps(data).encode('utf-8')
            response = invoke_api(url, body=encoded_data, method='POST')
            print('Resultado de API: {} {}'.format(response.status, response.data))
            if response.status == 200:
                return True, 'Usuario valido', response.status, json.loads(response.data.decode('utf-8'))['idusuario']
            return False, json.loads(response.data.decode('utf-8'))['mensaje'], response.status, None
        return False, 'Usuario no valido.', 404, None