import tkinter as tk
from tkinter import *
from pubsub import pub
from model import Model
from view import View

class Controller:
    def __init__(self, main_window):
        self.main_window_ = main_window
        self.view_ = View(self.main_window_)
        self.model_ = Model()
        self.view_.set_up()
        pub.subscribe(self.load_table_button_pressed, "load_table")

    def load_table_button_pressed(self):
        #print ('controller receive message - OpenFile_Button_Pressed')
        self.model_.load_table()


if __name__ == "__main__":
    main_window = Tk()
    WIDTH = 800
    HEIGHT = 800
    main_window.geometry("%sx%s" % (WIDTH, HEIGHT))
    #mainwin.resizable(0, 0)
    main_window.title("Video Database Controller")

    game_app = Controller(main_window)

    main_window.mainloop()