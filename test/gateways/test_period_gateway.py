from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from infra.infrastructure_exception import InfrastructureException
from infra.interfaces.i_previred_api import IPreviredApi
from gateways.periods_gateway import PeriodsGateway
from gateways.gateway_exception import GatewayException


class TestPreviredGateway(TestCase):

    def setUp(self):
        self.api = MagicMock(IPreviredApi)
        self.gateway = PeriodsGateway(self.api)

    def test_get_when_infrastructure_exception_then_raise_repository_exception(self):
        self.api.get_periodo.side_effect = InfrastructureException()

        self.assertRaises(GatewayException, lambda: self.gateway.get())

    def test_get_when_api_response_is_ok_then_return_time_period_entity_with_data(self):
        self.api.get_periodo.return_value = {
            "id": 6,
            "fechaCreacion": "1969-03-01",
            "fechaFin": "1970-01-01",
            "fechas": [
                "1969-03-01",
                "1969-05-01",
                "1969-09-01",
                "1970-01-01"]
        }
        result = self.gateway.get()

        self.assertEqual(6, result.id)
        self.assertEqual("1969-03-01", result.begin_date)
        self.assertEqual("1970-01-01", result.end_date)
        self.assertEqual([datetime(1969, 3, 1), datetime(1969, 5, 1), datetime(1969, 9, 1),
                          datetime(1970, 1, 1)], result.input_dates)
