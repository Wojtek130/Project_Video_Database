from row import Row

class KeyWord(Row):
    #current_key_word_id_ = 1
    def __init__(self, video_id, keyword_id):
        self.video_id_ = video_id
        self.keyword_id_ = keyword_id

    def data_tuple(self):
        return (self.video_id_, self.keyword_id_)