import datetime
import sqlite3
from pubsub import pub
from model import Model

class ModelDB(Model):
    def __init__(self):
        self.conn_ = sqlite3.connect("database/test.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.c_ = self.conn_.cursor()
        self.videos_all_information_ = """SELECT * from Video"""
        self.all_keywords_for_vid_ = """SELECT kw.name
                                    FROM Video v, VidKeyWord vkw, KeyWord kw
                                    WHERE v.video_id = vkw.video_id AND kw.keyword_id = vkw.keyword_id AND v.video_id = ?"""

    def get_videos_information_from_db(self):
        #get all objects from DB/desirialize objects
        self.c_.execute(self.videos_all_information_)
        self.record_videos_ = self.c_.fetchall()
       # print(self.record_videos_)

    def get_all_keywords_for_a_vid(self, video_id):
        self.c_.execute(self.all_keywords_for_vid_, (video_id,))
        return self.c_.fetchall()
        #print(self.all_keywords_for_vid)

    def videos_data_array(self, sorting_option):
        self.get_videos_information_from_db()
        videos_with_keywords = []
        for v in self.record_videos_:
            v_list = list(v)
            vid = v[0]
            keywords = self.get_all_keywords_for_a_vid(vid)
            keywords = list(map(lambda tuple : tuple[0], keywords))
            v_list.append(keywords)
            videos_with_keywords.append(v_list)
        ["Video ID", "Episode No.", "Title", "State","Publication date"]
        if sorting_option == "Episode No.":
            videos_with_keywords.sort(key=lambda x:x[1])
        elif sorting_option == "Title":
            videos_with_keywords.sort(key=lambda x:x[2])
        elif sorting_option == "State":
            videos_with_keywords.sort(key=lambda x:x[3])
        elif sorting_option == "Publication date":
            videos_with_keywords.sort(key=lambda x:x[4])
        else:
            pass

        return videos_with_keywords

    def get_videos_information(self, sorting_option = "Video ID"):
        pub.sendMessage("videos_information_ready", data = self.videos_data_array(sorting_option))
    
    def __del__(self):
        self.conn_.close()

if __name__ == "__main__":
    m = ModelDB()
   # m.get_videos_information()
   # m.get_all_keywords_for_a_vid(1)
    print(m.videos_data_array())