import tkinter as tk
from tkinter import *
from pubsub import pub
from modelDB import ModelDB
from view import View

class Controller:
    def __init__(self, main_window):
        self.main_window_ = main_window
        self.view_ = View(self.main_window_)
        self.model_ = ModelDB()
        self.view_.set_up()
        pub.subscribe(self.get_videos_information, "but_1_show_videos_clicked")
        pub.subscribe(self.render_videos_information, "videos_information_ready")
        pub.subscribe(self.get_keywords_information, "but_2_show_keywords_clicked")
        pub.subscribe(self.render_keywords_information, "keywords_information_ready")
        pub.subscribe(self.add_video, "but_6_submit_add_clicked")
        pub.subscribe(self.edit_requested, "edit_requested")
        pub.subscribe(self.delete_requested, "delete_requested")
        pub.subscribe(self.get_all_keywords_for_vid, "get_all_keywords_for_vid")
        pub.subscribe(self.all_keywords_for_vid_ready, "all_keywords_for_vid_ready")

    def get_videos_information(self, data):
        self.model_.get_videos_information(data)

    def render_videos_information(self, data):
        self.view_.insert_videos_data(data)

    def get_keywords_information(self, data):
        self.model_.get_keywords_information(data)

    def render_keywords_information(self, data):
        self.view_.insert_keywords_data(data)

    def add_video(self, data):
        self.model_.add_video(data)

    def edit_requested(self, data):
        self.model_.edit_requested(data)

    def delete_requested(self, data):
        self.model_.delete_requested(data)

    def get_all_keywords_for_vid(self, vid):
        self.model_.get_all_keywords_for_vid(vid)

    def all_keywords_for_vid_ready(self, data):
        self.view_.all_keywords_for_vid_ready(data)

if __name__ == "__main__":
    main_window = Tk()
    WIDTH = 800
    HEIGHT = 800
    main_window.geometry("%sx%s" % (WIDTH, HEIGHT))
    #mainwin.resizable(0, 0)
    main_window.title("Video Database")

    game_app = Controller(main_window)

    main_window.mainloop()