import unittest
import sqlite3
#import sys
#sys.path.insert(1, '/.../application/app/folder')
#sys.path.append("..")
import os
from . import *


class TestDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       pass

    @classmethod
    def tearDownClass(cls):
       pass

    def setUp(self):
        self.conn = sqlite3.connect("database/test.db")
        c = self.conn.cursor()
       # vid_1 = Video()
      #  cmd = "CREATE TABLE video (trend TEXT, trend_id1 TEXT, trend_id2 TEXT, trend_id3 TEXT, datetime TEXT)"
      #  c.execute(cmd)
     #   self.conn.commit()

    def tearDown(self):
         self.conn.close()
    
    def test_example(self):
        self.assertEqual(1 + 2, 3)

if __name__ == "__main__":
    #print(os.getcwd())
    unittest.main()
    