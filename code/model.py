from abc import ABC, abstractmethod

class Model(ABC):
    #should be abstract class, then ModelDB and maybe ModelSerializable subclasses will be created
    @abstractmethod
    def load_table(self):
        #get all objects from DB/desirialize objects
        pass