import datetime
import sqlite3

from model import Model

class ModelDB(Model):
    def __init__(self):
        self.conn_ = sqlite3.connect("database/test.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.c_ = self.conn_.cursor()
        self.videos_all_information_ = """SELECT * from Video"""
        self.all_keywords_for_vid_ = """SELECT kw.name
                                    FROM Video v, VidKeyWord vkw, KeyWord kw
                                    WHERE v.video_id = vkw.video_id AND kw.keyword_id = vkw.keyword_id AND v.video_id = ?"""

    def get_videos_information(self):
        #get all objects from DB/desirialize objects
        self.c_.execute(self.videos_all_information_)
        self.record_videos_ = self.c_.fetchall()
       # print(self.record_videos_)

    def get_all_keywords_for_a_vid(self, video_id):
        self.c_.execute(self.all_keywords_for_vid_, (video_id,))
        return self.c_.fetchall()
        #print(self.all_keywords_for_vid)

    def get_videos_with_keywords(self):
        self.get_videos_information()
        videos_with_keywords = []
        for v in self.record_videos_:
            v_list = list(v)
            vid = v[0]
            keywords = self.get_all_keywords_for_a_vid(vid)
            keywords = list(map(lambda tuple : tuple[0], keywords))
            v_list.extend(keywords)
            videos_with_keywords.append(v_list)
        return videos_with_keywords
    
    def __del__(self):
        self.conn_.close()

if __name__ == "__main__":
    m = ModelDB()
   # m.get_videos_information()
   # m.get_all_keywords_for_a_vid(1)
    print(m.get_videos_with_keywords())