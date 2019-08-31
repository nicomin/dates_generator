from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from application.dates_application import DatesApplication
from application.dates_application_exception import DatesApplicationException
from gateways.interfaces.i_previred_gateway import IPeriodsGateway
from gateways.repository_exception import GatewayException
from test.factories.time_period_dummy_factory import TimePeriodDummyFactory


class TestApplicationApplication(TestCase):
    def setUp(self):
        self.gateway = MagicMock(IPeriodsGateway)
        self.app = DatesApplication(self.gateway)
        self.time_period = TimePeriodDummyFactory().create()

    def test_get_initial_and_missing_dates_when_api_exception_then_raise_app_exception(self):
        self.gateway.get.side_effect = GatewayException()

        self.assertRaises(DatesApplicationException, lambda: self.app.get_initial_and_missing_dates())

    def test_get_initial_and_missing_dates_when_api_result_then_calculate_missing_dates_and_return_entity_result(self):
        self.gateway.get_periodos.side_effect.return_value = self.time_period

        result = self.app.get_initial_and_missing_dates()
        self.assertEqual([datetime(1969, 4, 1), datetime(1969, 6, 1), datetime(1969, 7, 1), datetime(1969, 8, 1),
                          datetime(1969, 10, 1), datetime(1969, 11, 1), datetime(1969, 12, 1)], result.output_dates)