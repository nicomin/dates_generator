import requests
from requests import RequestException

from infra.infrastructure_exception import InfrastructureException
from infra.interfaces.i_previred_api import IPreviredApi


class PreviredApi(IPreviredApi):

    def __init__(self):
        self.url = 'http://127.0.0.1:8080/periodos/api'

    def get_periodo(self):
        try:
            headers = {'Accept': 'application/json'}
            response = requests.get(self.url, headers=headers)
        except RequestException as e:
            raise InfrastructureException(InfrastructureException.ErrorType.REQUEST_ERROR) from e
        if not response.status_code == 200:
            raise InfrastructureException(InfrastructureException.ErrorType.FAILED)
        return response.json()
