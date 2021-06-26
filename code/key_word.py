from row import Row

class KeyWord(Row):
    current_key_word_id_ = 1
    already_created_keywords = []
    def __init__(self, name):
        self.keyword_id_ = self.current_key_word_id_
        self.key_word_id_inc()
        self.name_ = name
        self.already_created_keywords.append(self.name_)

    def data_tuple(self):
        return (self.keyword_id_, self.name_)

    @classmethod #maybe it should be a class method (pro)
    def key_word_id_inc(self):
        self.current_key_word_id_ += 1
        return


if __name__ == "__main__":
    kw1 = KeyWord("bread")
    print(kw1.keyword_id_)
    kw2 = KeyWord("butter")
    print(kw2.keyword_id_)