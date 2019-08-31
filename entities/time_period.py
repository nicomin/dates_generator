class TimePeriod:
    def __init__(self, id, begin_date, end_date, input_dates):
        self.id = id
        self.begin_date = begin_date
        self.end_date = end_date
        self.input_dates = input_dates
        self._output_dates = []

    @property
    def output_dates(self):
        return self._output_dates

    @output_dates.setter
    def output_dates(self, value: list):
        if not isinstance(value, list):
            raise TypeError()
        for input_date in self.input_dates:
            if input_date in value:
                value.remove(input_date)
        self._output_dates = value
