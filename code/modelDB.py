import sqlite3
from pubsub import pub

from key_word import KeyWord
from model import Model
from video import Video
from vid_key_word import VidKeyWord

class ModelDB(Model):
    def __init__(self):
        self.conn_ = sqlite3.connect("database/app_db3.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        #self.conn_.execute("PRAGMA foreign_keys = 1")
        self.c_ = self.conn_.cursor()
        self.c_.execute(Video.create_table_)
        self.c_.execute(KeyWord.create_table_)
        self.c_.execute(VidKeyWord.create_table_)
        self.conn_.commit()
        self.set_current_video_id()
        self.set_current_keyword_id()
        self.set_current_vid_keyword_id()
        self.videos_all_information_ = """SELECT * from Video"""
        self.all_keywords_ = """SELECT kw.name from KeyWord kw"""
        self.keyword_id_for_name_ = """SELECT kw.keyword_id from KeyWord kw where kw.name = ?"""
        self.all_keywords_for_vid_ = """SELECT kw.name
                                    FROM Video v, VidKeyWord vkw, KeyWord kw
                                    WHERE v.video_id = vkw.video_id AND kw.keyword_id = vkw.keyword_id AND v.video_id = ?"""
        self.all_titles_for_kwid_ = """SELECT v.title
                            FROM Video v, VidKeyWord vkw, KeyWord kw
                            WHERE v.video_id = vkw.video_id AND kw.keyword_id = vkw.keyword_id AND kw.keyword_id = ?"""
        self.keywords_all_information_ = """SELECT * from KeyWord"""
        

    def get_videos_information_from_db(self):
        self.c_.execute(self.videos_all_information_)
        self.record_videos_ = self.c_.fetchall()

    def get_all_keywords_for_a_vid(self, video_id):
        self.c_.execute(self.all_keywords_for_vid_, (video_id,))
        return self.c_.fetchall()

    def get_all_titles_for_a_kwid(self, keyword_id):
        self.c_.execute(self.all_titles_for_kwid_, (keyword_id,))
        return self.c_.fetchall()

    def videos_data_array(self, sorting_option):
        self.get_videos_information_from_db()
        videos_with_keywords = []
        for v in self.record_videos_:
            v_list = list(v)
            vid = v_list[0]
            keywords = self.get_all_keywords_for_a_vid(vid)
            keywords = list(map(lambda tuple : tuple[0], keywords))
            v_list.append(keywords)
            videos_with_keywords.append(v_list)
        if sorting_option == "Episode No.":
            try:
                videos_with_keywords.sort(key=lambda x:x[1])
            except TypeError:
                print("Values of diffrent type cannot be sorted")
        elif sorting_option == "Title":
            try:
                videos_with_keywords.sort(key=lambda x:x[2])
            except TypeError:
                print("Values of diffrent type cannot be sorted")
        elif sorting_option == "State":
            try:
                videos_with_keywords.sort(key=lambda x:x[3])
            except TypeError:
                print("Values of diffrent type cannot be sorted")
        elif sorting_option == "Publication date":
            try:
                videos_with_keywords.sort(key=lambda x:x[4])
            except TypeError:
                print("Values of diffrent type cannot be sorted")
        else:
            pass
        return videos_with_keywords

    def get_videos_information(self, sorting_option = "Video ID"):
        pub.sendMessage("videos_information_ready", data = self.videos_data_array(sorting_option))

    def get_keywords_information(self, sorting_option = "Keyword ID"):
        pub.sendMessage("keywords_information_ready", data = self.keywords_data_array(sorting_option))

    def keywords_data_array(self, sorting_option):
        self.get_keywords_information_from_db()
        keywords_with_titles = []
        for kw in self.record_keywords_:
            kw_list = list(kw)
            kwid = kw[0]
            titles = self.get_all_titles_for_a_kwid(kwid)
            titles = list(map(lambda tuple : tuple[0], titles))
            kw_list.append(titles)
            keywords_with_titles.append(kw_list)
        if sorting_option == "Keywords ID":
            try:
                keywords_with_titles.sort(key=lambda x:x[0])
            except TypeError:
                print("Values of diffrent type cannot be sorted")
        elif sorting_option == "Name":
            try:
                keywords_with_titles.sort(key=lambda x:x[1])
            except TypeError:
                print("Values of diffrent type cannot be sorted")
        else:
            pass
        return keywords_with_titles

    def get_keywords_information_from_db(self):
        self.c_.execute(self.keywords_all_information_)
        self.record_keywords_ = self.c_.fetchall()
    
    def add_video(self, data):
        video_obj = data[0]
        keywords_list = data[1]
        self.c_.execute(Video.insert_replace_, video_obj.data_tuple())
        self.conn_.commit()
        self.c_.execute(self.all_keywords_)
        all_keywords = self.c_.fetchall()
        all_keywords =  list(map(lambda tuple : tuple[0], all_keywords))
        for kw in keywords_list:
            if kw not in all_keywords:
                new_kw = KeyWord(kw)
                kw_id = new_kw.keyword_id_
                self.c_.execute(KeyWord.insert_replace_, new_kw.data_tuple())
                self.conn_.commit()  
            else:
                self.c_.execute(self.keyword_id_for_name_, (kw,))
                kw_id = self.c_.fetchone()[0]
            new_vkw = VidKeyWord(video_obj.video_id_, kw_id)
            self.c_.execute(VidKeyWord.insert_replace_, new_vkw.data_tuple())
            self.conn_.commit()

    def set_current_video_id(self):
        self.c_.execute("""SELECT COUNT(*) FROM Video """)
        result = self.c_.fetchone()[0]
        if result > 0:
            self.c_.execute("""SELECT MAX(video_id) FROM Video""")
            max_id = self.c_.fetchone()[0]
            Video.set_video_id_(int(max_id) + 1)

    def set_current_keyword_id(self):
        self.c_.execute("""SELECT COUNT(*) FROM KeyWord """)
        result = self.c_.fetchone()[0]
        if result > 0:
            self.c_.execute("""SELECT MAX(keyword_id) FROM KeyWord""")
            max_id = self.c_.fetchone()[0]
            KeyWord.set_keyword_id_(int(max_id) + 1)

    def set_current_vid_keyword_id(self):
        self.c_.execute("""SELECT COUNT(*) FROM VidKeyWord """)
        result = self.c_.fetchone()[0]
        if result > 0:
            self.c_.execute("""SELECT MAX(vid_keyword_id) FROM VidKeyWord""")
            max_id = self.c_.fetchone()[0]
            VidKeyWord.set_vid_key_word_id_(int(max_id) + 1)

    def edit_requested(self, data):
        print("edit model")

    def delete_requested(self, data):
        vid = data[0]
        self.c_.execute("""select kw.keyword_id
                        from Video v, KeyWord kw, VidKeyWord vkw
                        where v.video_id = ? and v.video_id = vkw.video_id and vkw.keyword_id = kw.keyword_id""", (vid,))
        all_kwids_for_vid = self.c_.fetchall()
        all_kwids_for_vid = list(map(lambda tuple : tuple[0], all_kwids_for_vid))
        for kwid in all_kwids_for_vid:
            self.c_.execute("""select v.video_id
                            from Video v, KeyWord kw, VidKeyWord vkw
                            where kw.keyword_id = ? and kw.keyword_id = vkw.keyword_id and vkw.video_id = v.video_id""", (kwid,))
            all_vids_for_kwid = self.c_.fetchall()
            all_vids_for_kwid = list(map(lambda tuple : tuple[0], all_vids_for_kwid))
            if len(all_vids_for_kwid) == 1:
                self.c_.execute("""DELETE FROM Keyword WHERE keyword_id=?""", (kwid,))
        self.c_.execute("""DELETE FROM VidKeyWord WHERE video_id=?""", (vid,))
        self.c_.execute("""DELETE FROM Video WHERE video_id=?""", (vid,))
        self.conn_.commit()

    def get_all_keywords_for_vid(self, vid):
        self.c_.execute("""select kw.name
                        from Video v, KeyWord kw, VidKeyWord vkw
                        where v.video_id = ? and v.video_id = vkw.video_id and vkw.keyword_id = kw.keyword_id""", (vid,))
        all_keywords_for_vid = self.c_.fetchall()
        all_keywords_for_vid = list(map(lambda tuple : tuple[0], all_keywords_for_vid))
        pub.sendMessage("all_keywords_for_vid_ready", data=all_keywords_for_vid)
   
    def __del__(self):
        self.conn_.close()

if __name__ == "__main__":
    m = ModelDB()
   # m.get_videos_information()
   # m.get_all_keywords_for_a_vid(1)