import datetime
import sqlite3
import unittest


from video import Video
from key_word import KeyWord


class TestDB(unittest.TestCase):

   
    def setUp(self):
       pass

    @classmethod
    def tearDownClass(cls):
       pass

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect("database/test.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
        cls.c = cls.conn.cursor()
        
        cmd = """CREATE TABLE IF NOT EXISTS Video 
            (video_id integer PRIMARY KEY NOT NULL, episode_number integer, title TEXT, state TEXT, publication_date DATE, notes TEXT)"""
        #sqlite_insert_with_param = """INSERT INTO 'Video'
                          #('video_id', 'episode_number', 'title', 'state', 'publication_date', 'notes') 
                          #VALUES (?, ?, ?, ?, ?, ?);"""
        sqlite_upsert_with_param = """INSERT INTO 'Video'
                            ('video_id', 'episode_number', 'title', 'state', 'publication_date', 'notes')               
                            VALUES (?, ?, ?, ?, ?, ?)
                            ON CONFLICT(video_id) DO UPDATE SET video_id = video_id;"""
        video_insert_replace = """INSERT OR REPLACE INTO 'Video'
                            ('video_id', 'episode_number', 'title', 'state', 'publication_date', 'notes')               
                            VALUES (?, ?, ?, ?, ?, ?)"""
        #INSERT INTO vocabulary(word) VALUES('jovial')
        #ON CONFLICT(word) DO UPDATE SET count=count+1;
        cls.vid_1 = Video(2, "test video", "working on",  datetime.date(2014,4,28), "goes onaa")
        data_tuple = (cls.vid_1.video_id_, cls.vid_1.episode_number_, cls.vid_1.title_, cls.vid_1.state_, cls.vid_1.publication_date_, cls.vid_1.notes_)
        
        
        cls.c.execute(cmd)
        cls.c.execute(video_insert_replace, data_tuple)
        cls.conn.commit()



        create_keyword_table = """CREATE TABLE IF NOT EXISTS KeyWord 
            (keyword_id integer PRIMARY KEY NOT NULL, name TEXT)"""

        upsert_keyword = """INSERT INTO 'KeyWord'
                    ('keyword_id', 'name')               
                    VALUES (?, ?)
                    ON CONFLICT(keyword_id) DO NOTHING;"""

        keyword_insert_replace = """INSERT OR REPLACE INTO 'KeyWord'
            ('keyword_id', 'name')               
            VALUES (?, ?)"""
        cls.kw_1 = KeyWord("sea")
        cls.kw_2 = KeyWord("ocean")
        cls.c.execute(create_keyword_table)
        cls.c.execute(keyword_insert_replace, cls.kw_1.data_tuple())
        cls.c.execute(keyword_insert_replace, cls.kw_2.data_tuple())
        cls.conn.commit()

        ### 
        create_vid_keyword_table = """CREATE TABLE IF NOT EXISTS VidKeyWord 
            (keyword_id integer NOT NULL,  keyword_id integer NOT NULL),
             FOREIGN KEY(video_id) REFERENCES Video(video_id),
             FOREIGN KEY(keyword_id) REFERENCES KeyWord(keyword_id),"""

        upsert_vid_keyword = """INSERT INTO 'VidKeyWord'
                    ('video_od','keyword_id')               
                    VALUES (?, ?)
                    ON CONFLICT(video_id) DO NOTHING;"""

        keyword_insert_replace = """INSERT OR REPLACE INTO 'VidKeyWord'
             ('video_id','keyword_id')               
            VALUES (?, ?)"""
        ###

        sqlite_select_query = """SELECT * from Video where video_id == 1"""
        cls.c.execute(sqlite_select_query)
        cls.record = cls.c.fetchone()

        query_kw1 = """SELECT * from KeyWord where keyword_id = 1"""
        cls.c.execute(query_kw1)
        cls.record_kw_1 = cls.c.fetchone()
        
        query_kw2 = """SELECT * from KeyWord where keyword_id = 2"""
        cls.c.execute(query_kw2)
        cls.record_kw_2 = cls.c.fetchone()

    def tearDown(self):
         self.conn.close()
    


    #
    # def test_kw_1(self):
    #    print("Test 2")
   #     self.assertEqual(1, 1)
     #   print("heheh")
        #query = """SELECT * from KeyWord where name = 'ocean'"""
        #self.c.execute(query)
       # record = self.c.fetchone()
      #  print(record)
      #  self.assertEqual(record[0], self.kw_1.key_word_id_)
       # self.assertEqual(record[1], self.kw_1.name_)

    
    #def test_vid_1(self):
       # print("Test 1")
      #  self.assertEqual(self.record[0], self.vid_1.video_id_)
        
       # self.assertEqual(record[2], self.vid_1.title_)
       # self.assertEqual(record[3], self.vid_1.state_)
       # self.assertEqual(record[4], self.vid_1.publication_date_)
       # self.assertEqual(record[5], self.vid_1.notes_)

    #def test_2(self):
     #   self.assertEqual(self.record[1], self.vid_1.episode_number_)
#

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

if __name__ == "__main__":
    unittest.main()
    