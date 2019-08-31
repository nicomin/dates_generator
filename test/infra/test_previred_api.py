from unittest import TestCase
from unittest.mock import patch

from infra.interfaces.previred_api import PreviredApi


class TestPreviredApi(TestCase):

    def setUp(self):
        self.api = PreviredApi()

    @patch('infra.previred_api.requests')
    def test_previred_api_when_request_exception_then_raise_infrastructure_exception(self, request_mock):
        request_mock.get.side_effect = Request
