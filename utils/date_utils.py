from datetime import datetime

from dateutil.relativedelta import relativedelta


class DateUtils:

    def get_date_from_date_str(self, date_str: str, date_format: str = '%Y-%m-%d'):
        return datetime.strptime(date_str, date_format)

    def sum_one_month_to_date(self, date_input: datetime):
        return date_input + relativedelta(months=1)
