from abc import ABC, abstractmethod

class Model(ABC):
    pass
    #should be abstract class, then ModelDB and maybe ModelSerializable subclasses will be created
    @abstractmethod
    def get_videos_information(self):
        pass