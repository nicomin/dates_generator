from unittest import TestCase

from resources.validators.missing_dates_validator import MissingDatesValidator


class TestMissingDatesValidator(TestCase):
    def setUp(self):
        self.input_data = {
            'a': 1,
            'b': 2,
            'c': 3
        }
        self.validator = MissingDatesValidator('a', 'b', 'c')

    def test_required_fields_validation_when_some_required_key_is_not_in_data_then_return_false(self):
        self.input_data.pop('c')
        self.assertFalse(self.validator.required_fields_validation(self.input_data))

    def test_required_fields_validation_when_all_required_keys_are_in_data_then_return_true(self):
        self.assertTrue(self.validator.required_fields_validation(self.input_data))

    def test_none_and_empty_fields_validation_when_some_dict_value_is_none(self):
        self.input_data['a'] = None
        self.assertFalse(self.validator.none_and_empty_fields_validation(self.input_data))

    def test_none_and_empty_fields_validation_when_some_dict_value_is_empty_string_then_return_false(self):
        self.input_data['b'] = ''
        self.assertFalse(self.validator.none_and_empty_fields_validation(self.input_data))

    def test_none_and_empty_fields_validation_when_some_dict_value_is_0_then_return_false(self):
        self.input_data['c'] = 0
        self.assertFalse(self.validator.none_and_empty_fields_validation(self.input_data))

    def test_none_and_empty_fields_validation_when_input_values_has_not_none_0_or_empty_strings_between_its_values_then_return_true(self):
        self.assertTrue(self.validator.none_and_empty_fields_validation(self.input_data))
