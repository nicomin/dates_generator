from datetime import datetime

from entities.time_period import TimePeriod


class TimePeriodDummyFactory:

    def create(self):
        return TimePeriod(1, "1969-03-01", "1970-01-01",
                          [datetime(1969, 3, 1), datetime(1969, 5, 1), datetime(1969, 9, 1), datetime(1970, 1, 1)])
