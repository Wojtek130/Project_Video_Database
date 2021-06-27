from row import Row

class VidKeyWord(Row):
    current_vid_key_word_id_ = 1
    create_table = """CREATE TABLE IF NOT EXISTS Video 
                    (video_id integer PRIMARY KEY NOT NULL, 
                    episode_number integer, title TEXT, state TEXT, 
                    publication_date DATE, notes TEXT)"""
    def __init__(self, video_id, keyword_id):
        self.vid_key_word_id_ = self.current_vid_key_word_id_
        self.vid_key_word_id_inc()
        self.video_id_ = video_id
        self.keyword_id_ = keyword_id

    def __str__(self):
        return "VidKeyWord({0}, {1}, {2})".format(self.vid_key_word_id_,self.video_id_, self.keyword_id_)

    def data_tuple(self):
        return (self.vid_key_word_id_, self.video_id_, self.keyword_id_)

    @classmethod
    def vid_key_word_id_inc(self):
        self.current_vid_key_word_id_ += 1
        return