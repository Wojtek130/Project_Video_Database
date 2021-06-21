from row import Row

class Video(Row):
    current_video_id_ = 1
    def __init__(self, episode_number = 0, title = "", state = "recorded", publication_date = "today", notes  = "", key_words = []):
        self.video_id_ = self.current_video_id_
        self.video_id_inc()
        self.episode_number_ = episode_number
        self.title_ = title
        self.state_ = state
        self.publication_date_ = publication_date
        self.notes_ = notes
        #create/get from database all keyword obcjects and add their key_word_ids to self.key_word_ids_list
        self.key_word_ids_list = []

    @classmethod #maybe it should be a static method (pro)
    def video_id_inc(self):
        self.current_video_id_ += 1
        return

class KeyWord:
    current_key_word_id_ = 1
    def __init__(self, name):
        self.keyword_id_ = self.current_key_word_id_
        self.key_word_id_inc()
        self.name_ = name

    @staticmethod #maybe it should be a class method (pro)
    def key_word_id_inc(self):
        self.current_key_word_id_ += 1
        return

if __name__ == "__main__":
    v1 = Video()
    print(v1.video_id_)
    v2 = Video()
    print(v2.video_id_)