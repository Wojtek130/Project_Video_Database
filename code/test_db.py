import datetime
import os
import sqlite3
import unittest

from video import Video
from key_word import KeyWord
from vid_key_word import VidKeyWord

class TestDB(unittest.TestCase):

    def setUp(self):
       pass

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        os.remove("database/test.db")

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect("database/test.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cls.c = cls.conn.cursor()

        cls.c.execute(Video.create_table_)
        cls.vid_1 = Video(2, "test_video", "working on",  datetime.date(2014,4,28), "goes onaa")        
        cls.c.execute(Video.insert_replace_, cls.vid_1.data_tuple())
        cls.conn.commit()

        cls.vid_2 = Video(3, "Spain", "ready",  datetime.date(2018,5,29), "waiting for")        
        cls.c.execute(Video.insert_replace_, cls.vid_2.data_tuple())
        cls.conn.commit()

        cls.kw_1 = KeyWord("sea")
        cls.kw_2 = KeyWord("ocean")
        cls.kw_3 = KeyWord("fish")
        cls.c.execute(KeyWord.create_table_)
        cls.c.execute(KeyWord.insert_replace_, cls.kw_1.data_tuple())
        cls.c.execute(KeyWord.insert_replace_, cls.kw_2.data_tuple())
        cls.c.execute(KeyWord.insert_replace_, cls.kw_3.data_tuple())
        cls.conn.commit()

        cls.c.execute(VidKeyWord.create_table_)
        cls.conn.commit()

        cls.vkw_1 = VidKeyWord(1, 2)
        cls.c.execute(VidKeyWord.insert_replace_, cls.vkw_1.data_tuple())
        cls.conn.commit()

        cls.vkw_2 = VidKeyWord(1, 3)
        cls.c.execute(VidKeyWord.insert_replace_, cls.vkw_2.data_tuple())
        cls.conn.commit()

        cls.vkw_3 = VidKeyWord(2, 1)
        cls.c.execute(VidKeyWord.insert_replace_, cls.vkw_3.data_tuple())
        cls.conn.commit()
       
        cls.vkw_4 = VidKeyWord(2, 2)
        cls.c.execute(VidKeyWord.insert_replace_, cls.vkw_4.data_tuple())
        cls.conn.commit()

        sqlite_select_query = """SELECT * from Video where video_id = 1"""
        cls.c.execute(sqlite_select_query)
        cls.record = cls.c.fetchone()

        query_kw1 = """SELECT * from KeyWord where keyword_id = 1"""
        cls.c.execute(query_kw1)
        cls.record_kw_1 = cls.c.fetchone()
        
        query_kw2 = """SELECT * from KeyWord where keyword_id = 2"""
        cls.c.execute(query_kw2)
        cls.record_kw_2 = cls.c.fetchone()

        query_vkw1 = """SELECT * from VidKeyWord where keyword_id = 2"""
        cls.c.execute(query_vkw1)
        cls.record_vkw_1 = cls.c.fetchone()

        query_all_keywords_vid_1 = """SELECT kw.name
                                    FROM Video v, VidKeyWord vkw, KeyWord kw
                                    WHERE v.video_id = vkw.video_id AND kw.keyword_id = vkw.keyword_id AND v.video_id = 1"""

        cls.c.execute(query_all_keywords_vid_1)
        cls.keywords_vid_1 = cls.c.fetchall()

    def tearDown(self):
         pass

    def test_vid(self):
        print('test_vid')
        self.assertEqual(self.record[0], self.vid_1.video_id_)

    def test_episode_no(self):
        print('test_episode_no')
        self.assertEqual(self.record[1], self.vid_1.episode_number_)
    
    def test_title(self):
        print('test_episode_no')
        self.assertEqual(self.record[2], self.vid_1.title_)

    def test_state(self):
        print('test_state')
        self.assertEqual(self.record[3], self.vid_1.state_)

    def test_pub_date(self):
        print('test_pub_date')
        self.assertEqual(self.record[4], self.vid_1.publication_date_)

    def test_notes(self):
        print('test_notes')
        self.assertEqual(self.record[5], self.vid_1.notes_)

    def test_kw1_id(self):
        print('test_id_kw_1')
        self.assertEqual(self.record_kw_1[0], self.kw_1.keyword_id_)

    def test_kw1_name(self):
        print('test_name_kw_1')
        self.assertEqual(self.record_kw_1[1], self.kw_1.name_)

    def test_kw2_id(self):
        print('test_id_kw_2')
        self.assertEqual(self.record_kw_2[0], self.kw_2.keyword_id_)

    def test_kw1_name(self):
        print('test_name_kw_2')
        self.assertEqual(self.record_kw_2[1], self.kw_2.name_)

    def test_vkw1_vkwid(self):
        print('test_vkwid_vkw_1')
        self.assertEqual(self.record_vkw_1[0], self.vkw_1.vid_key_word_id_)

    def test_vkw1_vid(self):
        print('test_vid_vkw_1')
        self.assertEqual(self.record_vkw_1[1], self.vkw_1.video_id_)

    def test_vkw1_kwid(self):
        print('test_kwid_vkw_1')
        self.assertEqual(self.record_vkw_1[2], self.vkw_1.keyword_id_)

    def test_vid1_keywords(self):
        print('test_keywords_vid_1')
        self.assertEqual(set(map(lambda tuple : tuple[0],self.keywords_vid_1)), set(["ocean","fish"]))

    
if __name__ == "__main__":
    unittest.main()
    