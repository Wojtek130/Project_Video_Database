from pubsub import pub

class Model:
    #should be abstract class, then ModelDB and maybe ModelSerializable subclasses will be created
    def load_table(self):
        #get all objects from DB/desirialize objects
        print("getting table from DB")