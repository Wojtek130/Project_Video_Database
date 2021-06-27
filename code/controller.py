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
        pub.subscribe(self.get_videos_information, "but_1_show_videos_pressed")
        pub.subscribe(self.render_videos_information, "videos_information_ready")
        

    def get_videos_information(self):
        self.model_.get_videos_information()

    def render_videos_information(self, data):
        self.view_.insert_videos_data(data)


if __name__ == "__main__":
    main_window = Tk()
    WIDTH = 800
    HEIGHT = 800
    main_window.geometry("%sx%s" % (WIDTH, HEIGHT))
    #mainwin.resizable(0, 0)
    main_window.title("Video Database Controller")

    game_app = Controller(main_window)

    main_window.mainloop()