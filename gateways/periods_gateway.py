from utils.date_utils import DateUtils
from entities.time_period import TimePeriod
from gateways.repository_exception import GatewayException
from infra.infrastructure_exception import InfrastructureException
from infra.interfaces.i_previred_api import IPreviredApi
from gateways.interfaces.i_previred_gateway import IPeriodsGateway


class PeriodsGateway(IPeriodsGateway):
    def __init__(self, previred_api: IPreviredApi):
        self.previred_api = previred_api
        self.date_utils = DateUtils()

    def get(self):
        try:
            result = self.previred_api.get_periodo()
            input_dates = []
            for date_str in result['fechas']:
                input_dates.append(self.date_utils.get_date_from_date_str(date_str))
        except InfrastructureException as e:
            raise GatewayException() from e
        return TimePeriod(
            result['id'],
            result['fechaCreacion'],
            result['fechaFin'],
            input_dates
        )


