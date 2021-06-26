from abc import ABC, abstractmethod

class Row(ABC):
    pass

    @abstractmethod
    def data_tuple(self):
        return