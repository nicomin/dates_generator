from abc import ABC, abstractmethod


class IPreviredApi(ABC):

    @abstractmethod
    def get_periodo(self):
        pass
