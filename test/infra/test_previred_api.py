import json
from unittest import TestCase
from unittest.mock import patch

from requests import RequestException

from infra.infrastructure_exception import InfrastructureException
from infra.mock_response import MockResponse
from infra.previred_api import PreviredApi


class TestPreviredApi(TestCase):

    def setUp(self):
        self.api = PreviredApi()

    @patch('infra.previred_api.requests')
    def test_previred_api_when_request_exception_then_raise_infrastructure_exception(self, request_mock):
        request_mock.get.side_effect = RequestException
        self.assertRaises(InfrastructureException, lambda: self.api.get_periodo())

    @patch('infra.previred_api.requests')
    def test_previred_api_when_response_status_code_is_not_200_then_raise_infrastructure_exception(self, request_mock):
        request_mock.get.return_value = MockResponse(text='', status_code=409)
        self.assertRaises(InfrastructureException, lambda: self.api.get_periodo())

    @patch('infra.previred_api.requests')
    def test_previred_api_when_response_is_succesful_then_return_it_as_json_dict(self, request_mock):
        mock_response = {'something': 'special'}
        request_mock.get.return_value = MockResponse(text=json.dumps(mock_response), status_code=200)
        response = self.api.get_periodo()
        self.assertEqual(mock_response, response)
