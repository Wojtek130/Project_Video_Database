import unittest
import sqlite3


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
        cmd = "CREATE TABLE video (trend TEXT, trend_id1 TEXT, trend_id2 TEXT, trend_id3 TEXT, datetime TEXT)"
        c.execute(cmd)
        self.conn.commit()

    def tearDown(self):
         self.conn.close()
    
    def test_example(self):
        self.assertEqual(1 + 2, 3)

if __name__ == "__main__":
    unittest.main()