from row import Row

class Video(Row):
    current_video_id_ = 1
    create_table =  """CREATE TABLE IF NOT EXISTS KeyWord 
            (keyword_id integer PRIMARY KEY NOT NULL, name TEXT)"""
    def __init__(self, episode_number = 0, title = "", state = "recorded", publication_date = "today", notes  = ""):
        self.video_id_ = self.current_video_id_
        self.video_id_inc()
        self.episode_number_ = episode_number
        self.title_ = title
        self.state_ = state
        self.publication_date_ = publication_date
        self.notes_ = notes
        #create/get from database all keyword obcjects and add their key_word_ids to self.key_word_ids_list
        #self.key_word_ids_list = []

    def data_tuple(self):
        return (self.video_id_, self.episode_number_, self.title_, self.state_, self.publication_date_, self.notes_,)

    @classmethod #maybe it should be a static method (pro)
    def video_id_inc(self):
        self.current_video_id_ += 1
        return



if __name__ == "__main__":
    v1 = Video()
    #print(v1.video_id_)
    v2 = Video()
   # print(v2.video_id_)

