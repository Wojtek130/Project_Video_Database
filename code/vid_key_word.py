from row import Row

class VidKeyWord(Row):
    current_vid_key_word_id_ = 1
    create_table_ = """CREATE TABLE IF NOT EXISTS VidKeyWord 
                    (vid_keyword_id integer PRIMARY KEY NOT NULL, video_id integer NOT NULL,  keyword_id integer NOT NULL,
                    FOREIGN KEY(video_id) REFERENCES Video(video_id),
                    FOREIGN KEY(keyword_id) REFERENCES KeyWord(keyword_id))"""
    insert_replace_ = """INSERT OR REPLACE INTO 'VidKeyWord'
                    ('vid_keyword_id', 'video_id','keyword_id')                 
                    VALUES (?, ?, ?)"""
    upsert_ = """INSERT INTO 'VidKeyWord'
            ('vid_keyword_id', 'video_id','keyword_id')               
            VALUES (?, ?, ?)
            ON CONFLICT(video_id) DO NOTHING;"""
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