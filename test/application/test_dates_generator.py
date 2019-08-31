from datetime import datetime
from unittest import TestCase

from application.dates_application_exception import DatesApplicationException
from application.dates_generator import DatesGenerator


class TestDatesGenerator(TestCase):

    def setUp(self):
        self.begin = datetime(1969, 3, 1)
        self.end = datetime(1970, 1, 1)
        self.dates_generator = DatesGenerator(self.begin, self.end)

    def test_generate_when_no_begin_date_then_raise_application_exception(self):
        self.dates_generator.begin_date = None
        self.assertRaises(DatesApplicationException, lambda: self.dates_generator.generate())

    def test_generate_when_no_end_date_then_raise_application_exception(self):
        self.dates_generator.end_date = None
        self.assertRaises(DatesApplicationException, lambda: self.dates_generator.generate())

    def test_generate_when_begin_and_end_are_ok_then_return_datetimes_array_with_all_months_between_parameters_inclusive(self):
        result = self.dates_generator.generate()

        self.assertIsInstance(result, list)
        self.assertEqual(11, len(result))

        self.assertEqual(3, result[0].month)
        self.assertEqual(1969, result[0].year)
        self.assertEqual(1, result[10].month)
        self.assertEqual(1970, result[10].year)

        assert result[1] < result[2] < result[3] < result[4] < result[5] < result[6] < result[7] < result[8] < result[9]

