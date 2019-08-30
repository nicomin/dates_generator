class MissingDatesValidator:
    def __init__(self, *args):
        self.required_fields = args

    def required_fields_validation(self, input_data: dict) -> bool:
        return all([key in input_data.keys() for key in self.required_fields])

    def none_and_empty_fields_validation(self, input_data: dict) -> bool:
        return all([input_data[key] for key in self.required_fields])

    def validate(self, input_data: dict) -> bool:
        return self.required_fields_validation(input_data) and self.none_and_empty_fields_validation(input_data)