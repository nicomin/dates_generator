from abc import ABC, abstractmethod

from entities.time_period import TimePeriod


class IMissingDatesApplication(ABC):

    @abstractmethod
    def get_initial_and_missing_dates(self) -> TimePeriod:
        pass
