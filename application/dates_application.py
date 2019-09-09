from injector import inject

from utils.date_utils import DateUtils
from application.dates_application_exception import DatesApplicationException
from application.dates_generator import DatesGenerator
from application.interfaces.i_missing_dates_application import IDatesApplication
from gateways.interfaces.i_previred_gateway import IPeriodsGateway
from gateways.gateway_exception import GatewayException


class DatesApplication(IDatesApplication):
    @inject
    def __init__(self, period_gateway: IPeriodsGateway):
        self.period_gateway = period_gateway
        self.date_utils = DateUtils()

    def get_initial_and_missing_dates(self):
        try:
            time_period = self.period_gateway.get()
            period_dates = self._get_period_dates(time_period.begin_date, time_period.end_date)
            time_period.output_dates = period_dates
        except GatewayException as e:
            raise DatesApplicationException() from e
        else:
            return time_period

    def _get_period_dates(self, begin_date: str, end_date: str):
        generator = DatesGenerator(
            self.date_utils.get_date_from_date_str(begin_date),
            self.date_utils.get_date_from_date_str(end_date)
        )
        return generator.generate()
