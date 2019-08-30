from abc import ABC, abstractmethod


class IMissingDatesApplication(ABC):

    @abstractmethod
    def get_initial_and_missing_dates(self):
        pass
