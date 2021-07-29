from abc import ABC, abstractmethod

class Model(ABC):
    #should be abstract class, then ModelDB and maybe ModelSerializable subclasses will be created
    @abstractmethod
    def get_videos_information(self):
        pass

    @abstractmethod
    def get_keywords_information(self):
        pass

    @abstractmethod
    def add_video(self):
        pass

    @abstractmethod
    def edit_requested(self):
        pass

    @abstractmethod
    def delete_requested(self):
        pass