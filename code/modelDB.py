from model import Model

class ModelDB(Model):
    def __init__(self):
        self.db_ = db

    def load_table(self):
        #get all objects from DB/desirialize objects
        print("getting table from DB")