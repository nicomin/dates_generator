from datetime import datetime

from utils.date_utils import DateUtils
from application.dates_application_exception import DatesApplicationException


class DatesGenerator:

    def __init__(self, begin_date: datetime, end_date: datetime):
        self.date_utils = DateUtils()
        self.begin_date = begin_date
        self.end_date = end_date

    def generate(self):
        if not self.begin_date or not self.end_date:
            raise DatesApplicationException(DatesApplicationException.ErrorType.BAD_PARAMETERS)
        current_date = self.begin_date
        period_dates = []
        while current_date <= self.end_date:
            period_dates.append(current_date)
            current_date = self.date_utils.sum_one_month_to_date(current_date)
        return period_dates
