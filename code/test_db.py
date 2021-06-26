import unittest
import sqlite3
#from DateTime import date
import datetime
from video import Video


class TestDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       pass

    @classmethod
    def tearDownClass(cls):
       pass

    def setUp(self):
        self.conn = sqlite3.connect("database/test.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
        self.c = self.conn.cursor()
        
        cmd = """CREATE TABLE IF NOT EXISTS Video 
            (video_id integer PRIMARY KEY NOT NULL, episode_number integer, title TEXT, state TEXT, publication_date DATE, notes TEXT)"""
        sqlite_insert_with_param = """INSERT INTO 'Video'
                          ('video_id', 'episode_number', 'title', 'state', 'publication_date', 'notes') 
                          VALUES (?, ?, ?, ?, ?, ?);"""
        sqlite_upsert_with_param = """INSERT INTO 'Video'
                          ('video_id', 'episode_number', 'title', 'state', 'publication_date', 'notes')               
                            VALUES (?, ?, ?, ?, ?, ?)
                            ON CONFLICT(video_id) DO NOTHING;"""
        #INSERT INTO vocabulary(word) VALUES('jovial')
        #ON CONFLICT(word) DO UPDATE SET count=count+1;
        self.vid_1 = Video(2, "test video", "working on",  datetime.date(2014,4,28), "goes on")
        data_tuple = (self.vid_1.video_id_, self.vid_1.episode_number_, self.vid_1.title_, self.vid_1.state_, self.vid_1.publication_date_, self.vid_1.notes_)
        self.c.execute(cmd)
        self.c.execute(sqlite_upsert_with_param, data_tuple)
        self.conn.commit()
        


    def tearDown(self):
         self.conn.close()
    
    def test_vid_1(self):
        sqlite_select_query = """SELECT * from Video where video_id = 1"""
        self.c.execute(sqlite_select_query)
        record = self.c.fetchone()
        #print(record)
        self.assertEqual(record[0], self.vid_1.video_id_)
        self.assertEqual(record[1], self.vid_1.episode_number_)
        self.assertEqual(record[2], self.vid_1.title_)
        self.assertEqual(record[3], self.vid_1.state_)
        self.assertEqual(record[4], self.vid_1.publication_date_)
        self.assertEqual(record[5], self.vid_1.notes_)

if __name__ == "__main__":
    unittest.main()
    