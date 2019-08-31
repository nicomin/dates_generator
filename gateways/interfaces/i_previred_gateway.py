from abc import abstractmethod, ABC

from entities.time_period import TimePeriod


class IPeriodsGateway(ABC):

    @abstractmethod
    def get(self) -> TimePeriod:
        pass
