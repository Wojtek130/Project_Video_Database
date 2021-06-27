from row import Row

class Video(Row):
    current_video_id_ = 1
    create_table_ =  """CREATE TABLE IF NOT EXISTS Video 
                    (video_id integer PRIMARY KEY NOT NULL, 
                    episode_number integer, title TEXT, state TEXT, 
                    publication_date DATE, notes TEXT)"""
    insert_replace_ = """INSERT OR REPLACE INTO 'Video'
                    ('video_id', 'episode_number', 'title', 'state', 'publication_date', 'notes')               
                    VALUES (?, ?, ?, ?, ?, ?)"""
    upsert_ = """INSERT INTO 'Video'
            ('video_id', 'episode_number', 'title', 'state', 'publication_date', 'notes')               
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(video_id) DO UPDATE SET video_id = video_id;"""
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

    def __str__(self):
        return "Video({0}, {1}, {2}, {3}, {4}, {5})".format(self.video_id_, self.episode_number_, self.title_, self.state_, self.publication_date_, self.notes_)



if __name__ == "__main__":
    v1 = Video()
    #print(v1.video_id_)
    v2 = Video()
   # print(v2.video_id_)

