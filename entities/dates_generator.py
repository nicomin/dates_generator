class DatesGenerator:
    def __init__(self, id, begin_date, end_date, input_dates):
        self.id = id
        self.begin_date = begin_date
        self.end_date = end_date
        self.input_dates = input_dates
        self.output_dates = []