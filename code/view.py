from pubsub import pub
import tkinter as tk
from tkinter import *
from tkinter import ttk

class View:

    def __init__(self, main_window):
        self.main_window_ = main_window
        return

    def set_up(self):
        self.create_widgets()
        self.set_up_layout()

    def but_1_show_videos_clicked(self):
        print("loading table")
        self.but_1_show_videos_['state'] = tk.DISABLED
        self.but_2_show_keywords_['state'] = tk.NORMAL
        #self.switch_button_state(self.but_1_show_videos_)
        #self.switch_button_state(self.but_2_show_keywords_)
        self.but_3_add_video_ = tk.Button(self.top_frame_2_, text = "Add Video",command = self.but_3_add_video_clicked)
        self.but_3_add_video_.pack( side=LEFT)
        value_inside = tk.StringVar(self.top_frame_2_)
        value_inside.set("Sort by")
        options_list = ["Video ID", "Episode No.", "Title", "State","Publication date"]
        self.but_4_sorting_ = tk.OptionMenu(self.top_frame_2_, value_inside, *options_list, command=self.but_4_sorting_clicked)
        self.but_4_sorting_.pack(side=LEFT)
        self.tv_ = ttk.Treeview(self.bottom_frame_)
        self.tv_['columns']=('Video ID', 'Episode No.', 'Title', 'State', 'Publication date', 'Notes', 'Key words')
        self.tv_.column('#0', width=0, stretch=NO)
        self.tv_.column('Video ID', anchor=CENTER, width=80)
        self.tv_.column('Episode No.', anchor=CENTER, width=80)
        self.tv_.column('Title', anchor=CENTER, width=80)
        self.tv_.column('State', anchor=CENTER, width=80)
        self.tv_.column('Publication date', anchor=CENTER, width=100)
        self.tv_.column('Notes', anchor=CENTER, width=80)
        self.tv_.column('Key words', anchor=CENTER, width=80)

        self.tv_.heading('#0', text='', anchor=CENTER)
        self.tv_.heading('Video ID', text='Video ID', anchor=CENTER)
        self.tv_.heading('Episode No.', text='Episode No.', anchor=CENTER)
        self.tv_.heading('Title', text='Title', anchor=CENTER)
        self.tv_.heading('State', text='State', anchor=CENTER)
        self.tv_.heading('Publication date', text='Publication date', anchor=CENTER)
        self.tv_.heading('Notes', text='Notes', anchor=CENTER)
        self.tv_.heading('Key words', text='Key words', anchor=CENTER)
        self.tv_.pack()
        pub.sendMessage("but_1_show_videos_clicked")

    
    def but_2_show_keywords_clicked(self):
        try:
            self.but_3_add_video_.pack_forget()
            self.but_4_sorting_.pack_forget()
            self.tv_.pack_forget()
        except AttributeError:
            pass
        self.but_1_show_videos_['state'] = tk.NORMAL
        self.but_2_show_keywords_['state'] = tk.DISABLED
        #self.switch_button_state(self.but_1_show_videos_)
        #self.switch_button_state(self.but_2_show_keywords_)
        print("show keywords clicked")


    def but_3_add_video_clicked(self, *args):
        var = StringVar()
        label = Label( self.bottom_frame_, textvariable=var )

        var.set("Hey!? How are you doing?")
        label.pack_propagate()
        print("add video")

    def but_4_sorting_clicked(self, *args):
        print("sorting changed")


    def set_up_layout(self):
        self.top_frame_.pack(side = TOP)
        self.bottom_frame_.pack (side=BOTTOM)
        self.top_frame_2_.pack(side = TOP)
        self.but_1_show_videos_.pack( side=LEFT)
        self.but_2_show_keywords_.pack( side=LEFT)
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
        self.but_1_show_videos_ = tk.Button(self.top_frame_2_, text = "Videos Table",command = self.but_1_show_videos_clicked)
        self.but_2_show_keywords_ = tk.Button(self.top_frame_2_, text = "Keywords Table",command = self.but_2_show_keywords_clicked)
        #self.panelA = tk.Label(self.bottom_frame_, text = 'image here')
        return




    def switch_button_state(self, button):
        if (button['state'] == tk.NORMAL):
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL
    


if __name__=="__main__":
    main_window = tk.Tk()
    WIDTH = 800
    HEIGHT = 600
    main_window.geometry("%sx%s" % (WIDTH, HEIGHT))
    #main_window.resizable(0, 0)
    main_window.title("Video Database")
    view=View(main_window)
    view.set_up()
    main_window.mainloop()