from abc import ABC, abstractmethod

class Row(ABC):
    pass

    @abstractmethod
    def data_tuple(self):
        return

    @property
    def create_table_(self):
        raise NotImplementedError

    @property
    def insert_replace_(self):
        raise NotImplementedError
    
    @property
    def upsert_(self):
        raise NotImplementedError