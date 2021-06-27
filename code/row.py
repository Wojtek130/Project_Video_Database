from abc import ABC, abstractmethod

class Row(ABC):
    pass

    @abstractmethod
    def data_tuple(self):
        return

    @property
    def create_table(self):
        raise NotImplementedError