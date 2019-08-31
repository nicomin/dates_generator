from datetime import datetime
from unittest import TestCase

from test.factories.time_period_dummy_factory import TimePeriodDummyFactory


class TestTimePeriod(TestCase):

    def setUp(self):
        self.time_period = TimePeriodDummyFactory().create()

    def test_output_dates_when_value_is_not_a_list_then_raise_type_error(self):
        try:
            self.time_period.output_dates = 5
        except TypeError:
            self.tearDown()
        except Exception:
            self.fail()
        else:
            self.fail()

    def test_output_dates_setter_when_value_dates_has_a_value_that_already_exists_in_input_dates_then_remove_it_before_assign_value(self):
        self.time_period.output_dates = [datetime(1970, 1, 1), datetime(1997, 12, 1), datetime(1969, 3, 1)]

        self.assertEqual(1, len(self.time_period.output_dates))
        self.assertEqual(12, self.time_period.output_dates[0].month)
        self.assertEqual(1997, self.time_period.output_dates[0].year)

        self.time_period.output_dates = [datetime(1970, 1, 1)]
        self.assertEqual(0, len(self.time_period.output_dates))
