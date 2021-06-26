import unittest
import sqlite3
#from DateTime import date
from datetime import date
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
        c = self.conn.cursor()
        vid_1 = Video()
        cmd = """CREATE TABLE IF NOT EXISTS Video 
            (video_id integer PRIMARY KEY, episode_number integer, title TEXT, state TEXT, publication_date timestamp, notes TEXT)"""
        sqlite_insert_with_param = """INSERT INTO 'Video'
                          ('video_id', 'episode_number', 'title', 'state', 'publication_date', 'notes') 
                          VALUES (?, ?, ?, ?, ?, ?);"""
        sqlite_upsert_with_param = """INSERT INTO 'Video'
                          ('video_id', 'episode_number', 'title', 'state', 'publication_date', 'notes')               
                            VALUES (?, ?, ?, ?, ?, ?)
                            ON CONFLICT(video_id) DO NOTHING;"""
        #INSERT INTO vocabulary(word) VALUES('jovial')
        #ON CONFLICT(word) DO UPDATE SET count=count+1;

        data_tuple = (1, 2, "test video", "working on", date.today(), "goes on")
        c.execute(cmd)
        c.execute(sqlite_upsert_with_param, data_tuple)
        self.conn.commit()
        sqlite_select_query = """SELECT video_id from Video """
        c.execute(sqlite_select_query)
        records = c.fetchall()
        for row in records:
            print(row)


    def tearDown(self):
         self.conn.close()
    
    def test_example(self):
        self.assertEqual(1 + 2, 3)

if __name__ == "__main__":
    unittest.main()
    