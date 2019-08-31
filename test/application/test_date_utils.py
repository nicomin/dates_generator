from datetime import datetime
from unittest import TestCase

from utils.date_utils import DateUtils


class TestDateUtils(TestCase):

    def setUp(self):
        self.utils = DateUtils()

    def test_get_date_from_date_str_when_date_str_then_return_datetime_obj(self):
        date_str = '1970-02-01'
        result = self.utils.get_date_from_date_str(date_str)
        self.assertEqual(1, result.day)
        self.assertEqual(2, result.month)
        self.assertEqual(1970, result.year)

    def test_sum_one_month_to_date_when_date_then_return_that_date_one_month_on_future(self):
        input_date = datetime(1970, 1, 1)
        result = self.utils.sum_one_month_to_date(input_date)

        self.assertEqual(1, result.day)
        self.assertEqual(2, result.month)
        self.assertEqual(1970, result.year)
