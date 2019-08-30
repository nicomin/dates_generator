from abc import ABC, abstractmethod


class IDataGenerator(ABC):

    @abstractmethod
    def get(self):
        pass