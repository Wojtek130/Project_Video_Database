from row import Row

class KeyWord(Row):

    current_key_word_id_ = 1
    create_table_ =  """CREATE TABLE IF NOT EXISTS KeyWord 
                    (keyword_id integer PRIMARY KEY NOT NULL, name TEXT)"""
    insert_replace_ = """INSERT OR REPLACE INTO 'KeyWord'
                    ('keyword_id', 'name')               
                    VALUES (?, ?)"""
    upsert_ = """INSERT INTO 'KeyWord'
            ('keyword_id', 'name')               
            VALUES (?, ?)
            ON CONFLICT(keyword_id) DO NOTHING;"""
    already_created_keywords = []
    def __init__(self, name):
        self.keyword_id_ = self.current_key_word_id_
        self.key_word_id_inc()
        self.name_ = name
        self.already_created_keywords.append(self.name_)

    def __str__(self):
        return "KeyWord({0}, {1})".format(self.keyword_id_, self.name_)

    def data_tuple(self):
        return (self.keyword_id_, self.name_)


    @classmethod
    def key_word_id_inc(self):
        self.current_key_word_id_ += 1
    
    @classmethod
    def set_keyword_id_(self, value):
        self.current_key_word_id_ = value


if __name__ == "__main__":
    kw1 = KeyWord("bread")
    kw2 = KeyWord("butter")