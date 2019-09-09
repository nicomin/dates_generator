from abc import ABC, abstractmethod

from entities.time_period import TimePeriod


class IDatesApplication(ABC):

    @abstractmethod
    def get_initial_and_missing_dates(self) -> TimePeriod:
        pass
