import tkinter as tk
from tkinter import *

class View:

    def __init__(self, main_window):
        self.main_window_ = main_window
        return

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def load_table(self):
        print("loading table")

    def setup_layout(self):
        self.top_frame_.pack(side = TOP)
        self.bottom_frame_.pack (side=BOTTOM)
        self.top_frame_2_.pack(side = TOP)
        #self.b1LoadImg.pack( side=LEFT)
        #self.b2LineDetect.pack(side = RIGHT)
        #self.scale4.pack(side=BOTTOM) #max line gap
        #self.scale3.pack(side=BOTTOM) #min line lenght
        #self.scale2.pack(side=BOTTOM) #threshold
        #self.scale1.pack(side=BOTTOM) # pixel
        #self.panelA.pack()

    def create_widgets(self):
        self.background_label_ = tk.Label(self.main_window_)
        self.top_frame_ = Frame(self.main_window_,borderwidth=2,highlightbackground="black",highlightcolor="red",highlightthickness=1,width=300, height=600)
        self.bottom_frame_ = Frame(self.main_window_,borderwidth=2,highlightbackground="black",highlightcolor="red",highlightthickness=1,width=500, height=600)
        self.top_frame_2_ = Frame(self.top_frame_)
        #button
        self.but_1_show_table_ = tk.Button(self.top_frame_2_, text = "Show table",command = self.load_table)
        #self.panelA = tk.Label(self.bottom_frame_, text = 'image here')
        return
    


if __name__=="__main__":
    main_window = tk.Tk()
    WIDTH = 800
    HEIGHT = 600
    main_window.geometry("%sx%s" % (WIDTH, HEIGHT))
    #main_window.resizable(0, 0)
    main_window.title("Video Database")
    view=View(main_window)
    view.setup()
    main_window.mainloop()