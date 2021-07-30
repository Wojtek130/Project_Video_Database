import datetime
from pubsub import pub
import tkinter as tk
from tkinter import *
from tkinter import ttk

from video import Video




class View:

    def __init__(self, main_window):
        self.main_window_ = main_window
        return

    def set_up(self):
        self.create_widgets()
        self.set_up_layout()

    def but_1_show_videos_clicked(self):
        try:
            self.but_5_sorting_alph_.pack_forget()
            self.keyword_tv_.pack_forget()
            self.keyword_tv_scrollbar_.pack_forget()
        except AttributeError:
            pass
        self.but_1_show_videos_['state'] = tk.DISABLED
        self.but_2_show_keywords_['state'] = tk.NORMAL
        value_inside = tk.StringVar(self.top_frame_2_)
        value_inside.set("Sort by")
        options_list = ["Video ID", "Episode No.", "Title", "State","Publication date"]
        self.but_4_sorting_ = tk.OptionMenu(self.top_frame_2_, value_inside, *options_list, command=self.but_4_sorting_clicked)
        self.but_8_edit_ = tk.Button(self.top_frame_2_, text = "Edit",command = self.but_8_edit_clicked)
        self.but_9_delete_ = tk.Button(self.top_frame_2_, text = "Delete",command = self.but_9_delete_clicked)
        self.but_4_sorting_.pack(side=LEFT, expand=True)
        self.but_8_edit_.pack(side=LEFT, expand=True)
        self.but_9_delete_.pack(side=LEFT, expand=True)
        self.but_8_edit_['state'] = tk.DISABLED
        self.but_9_delete_['state'] = tk.DISABLED
        self.arrange_video_tv()
        pub.sendMessage("but_1_show_videos_clicked", data = "Video ID")

    
    def but_2_show_keywords_clicked(self):
        try:
            self.but_4_sorting_.pack_forget()
            self.video_tv_.pack_forget()
            self.but_8_edit_.pack_forget()
            self.but_9_delete_.pack_forget()
            self.video_tv_scrollbar_.pack_forget()
        except AttributeError:
            pass
        self.but_1_show_videos_['state'] = tk.NORMAL
        self.but_2_show_keywords_['state'] = tk.DISABLED
        self.arrange_keyword_tv()
        value_inside = tk.StringVar(self.top_frame_2_)
        value_inside.set("Sort by")
        options_list = ["Keywords ID", "Name"]
        self.but_5_sorting_alph_ = tk.OptionMenu(self.top_frame_2_, value_inside, *options_list, command=self.but_5_sorting_clicked)
        self.but_5_sorting_alph_.pack(side=LEFT, expand=True)
        pub.sendMessage("but_2_show_keywords_clicked", data = "Video ID")

    def add_edit_pop_up_window(self, action):
        self.add_video_pop_up_ = tk.Toplevel()
        self.add_video_pop_up_.grab_set()
        tk.Label(self.add_video_pop_up_, text="Episode No.").grid(row=0)
        tk.Label(self.add_video_pop_up_, text="Title").grid(row=1)
        tk.Label(self.add_video_pop_up_, text="State").grid(row=2)
        tk.Label(self.add_video_pop_up_, text="Publication date").grid(row=3)
        tk.Label(self.add_video_pop_up_, text="Notes").grid(row=4)
        tk.Label(self.add_video_pop_up_, text="Key Words").grid(row=5)
        if action == "add":
            self.add_video_pop_up_.wm_title("Add Video")
            self.e_episode_no_ = tk.StringVar(value="{}".format(Video.current_video_id_))
            self.e_title_ = tk.StringVar(value="")
            self.e_state_ = tk.StringVar(value="")
            self.e_publication_date_ = tk.StringVar(value="01.01.2000")
            self.e_notes_ = tk.StringVar(value="")
            self.e_key_words_ = tk.StringVar("")
            self.but_6_submit_ = ttk.Button(self.add_video_pop_up_, text="Submit", command= lambda: self.but_6_submit_clicked("add"))
        elif action == "edit":
            self.add_video_pop_up_.wm_title("Edit Video")
            self.e_episode_no_ = tk.StringVar(value="{}".format(self.selected_values_[1])) ###
            self.e_title_ = tk.StringVar(value=self.selected_values_[2])
            self.e_state_ = tk.StringVar(value=self.selected_values_[3])
            dot_separated_pub_date = datetime.datetime.strptime(self.selected_values_[4], "%Y-%m-%d").strftime("%d.%m.%Y")
            self.e_publication_date_ = tk.StringVar(value=dot_separated_pub_date)
            self.e_notes_ = tk.StringVar(value=self.selected_values_[5])
            pub.sendMessage("get_all_keywords_for_vid", vid=self.selected_values_[0])
            print(self.keywords_array_for_vid_)
            keywords_string =', '.join(self.keywords_array_for_vid_) 
            self.e_key_words_ = tk.StringVar(value=keywords_string)
            self.but_6_submit_ = ttk.Button(self.add_video_pop_up_, text="Submit", command= lambda: self.but_6_submit_clicked("edit"))        
        e_episode_no = tk.Entry(self.add_video_pop_up_, textvariable=self.e_episode_no_)
        e_title = tk.Entry(self.add_video_pop_up_, textvariable=self.e_title_)
        e_state = ttk.Combobox(self.add_video_pop_up_, textvariable=self.e_state_, width = 17, state="readonly")
        e_state['values'] = (' nic', 'nagrane', 'obrabiane', 'opublikowane')
        e_publication_date = tk.Entry(self.add_video_pop_up_, textvariable=self.e_publication_date_)
        e_notes = tk.Entry(self.add_video_pop_up_, textvariable=self.e_notes_)
        e_key_words = tk.Entry(self.add_video_pop_up_, textvariable=self.e_key_words_)
        e_episode_no.grid(row=0, column=1)
        e_title.grid(row=1, column=1)
        e_state.grid(row=2, column=1)
        e_publication_date.grid(row=3, column=1)
        e_notes.grid(row=4, column=1)
        e_key_words.grid(row=5, column=1)
        self.but_7_cancel_ = ttk.Button(self.add_video_pop_up_, text="Cancel", command=self.but_7_cancel_clicked)
        self.but_6_submit_.grid(row=6, column=0)
        self.but_7_cancel_.grid(row=6, column=1)

    def but_3_add_video_clicked(self, *args):
        self.add_edit_pop_up_window("add")

    def but_4_sorting_clicked(self, sorting_option):
        for item in self.video_tv_.get_children():
            self.video_tv_.delete(item)
        pub.sendMessage("but_1_show_videos_clicked", data=sorting_option)

    def but_5_sorting_clicked(self, sorting_option):
        for item in self.keyword_tv_.get_children():
            self.keyword_tv_.delete(item)
        pub.sendMessage("but_2_show_keywords_clicked", data=sorting_option)

    def but_6_submit_data_tuple(self):
        episode_no = self.e_episode_no_.get()
        title = self.e_title_.get()
        state = self.e_state_.get()
        publication_date = self.e_publication_date_.get()
        if publication_date == "":
            pub_date = None
        else:
            try: 
                pub_date = datetime.datetime.strptime(publication_date, "%d.%m.%Y").date() #'24.05.2010'
                pub_date = pub_date.strftime("%d.%m.%Y")
            except:
                pub_date = None
                #pop window telling about wrong data format
        notes = self.e_notes_.get()
        key_words = self.e_key_words_.get()
        key_words_list = list(set(key_words.split(", ")))
        self.add_video_pop_up_.destroy()
        return (episode_no, title, state, pub_date, notes, key_words_list)
    
    def but_6_submit_clicked(self, action):
        data_tuple = self.but_6_submit_data_tuple()
        if action == "add":
            pub.sendMessage("but_6_submit_add_clicked", data = (Video(data_tuple[0],data_tuple[1], data_tuple[2], data_tuple[3], data_tuple[4]), data_tuple[5]))
        elif action == "edit":
            temp2 = list(self.selected_values_)
            temp2.pop()
            temp2.append(self.keywords_array_for_vid_)
            original_video_tuple = tuple(temp2)
            temp = list(data_tuple)
            temp.insert(0, original_video_tuple[0][0])
            data_tuple = tuple(temp)
            date_converted = datetime.datetime.strptime(original_video_tuple[4], "%Y-%m-%d").strftime("%d.%m.%Y")
            original_video_tuple = (original_video_tuple[0], original_video_tuple[1], original_video_tuple[2], original_video_tuple[3], date_converted, original_video_tuple[5], original_video_tuple[6])
            pub.sendMessage("but_6_submit_edit_clicked", data = (original_video_tuple, data_tuple))
        self.add_video_pop_up_.destroy()

    def but_7_cancel_clicked(self):
        self.add_video_pop_up_.destroy()

    def but_8_edit_clicked(self):
        print("Edit clicked")
        self.add_edit_pop_up_window(action="edit")
        #pub.sendMessage("edit_requested", data = self.selected_values_)
        
    def but_9_delete_clicked(self):
        pub.sendMessage("delete_requested", data = self.selected_values_)
        print("Delete clicked")

    def arrange_video_tv(self):
        #style = ttk.Style()
        #style.map('Treeview', foreground=self.fixed_map(style, 'foreground'), background=self.fixed_map(style, 'background'))
        self.video_tv_scrollbar_ = Scrollbar(self.bottom_frame_)
        self.video_tv_scrollbar_.pack(side=RIGHT, fill=Y)
        self.video_tv_ = ttk.Treeview(self.bottom_frame_, yscrollcommand=self.video_tv_scrollbar_)
        self.video_tv_scrollbar_.config(command=self.video_tv_.yview)
        self.video_tv_['columns']=('Video ID', 'Episode No.', 'Title', 'State', 'Publication date', 'Notes', 'Key words')
        self.video_tv_.column('#0', width=0, stretch=NO)
        self.video_tv_.column('Video ID', anchor=CENTER, width=80)
        self.video_tv_.column('Episode No.', anchor=CENTER, width=80)
        self.video_tv_.column('Title', anchor=CENTER, width=80)
        self.video_tv_.column('State', anchor=CENTER, width=80)
        self.video_tv_.column('Publication date', anchor=CENTER, width=100)
        self.video_tv_.column('Notes', anchor=CENTER, width=80)
        self.video_tv_.column('Key words', anchor=CENTER, width=250)
        self.video_tv_.heading('#0', text='', anchor=CENTER)
        self.video_tv_.heading('Video ID', text='Video ID', anchor=CENTER)
        self.video_tv_.heading('Episode No.', text='Episode No.', anchor=CENTER)
        self.video_tv_.heading('Title', text='Title', anchor=CENTER)
        self.video_tv_.heading('State', text='State', anchor=CENTER)
        self.video_tv_.heading('Publication date', text='Publication date', anchor=CENTER)
        self.video_tv_.heading('Notes', text='Notes', anchor=CENTER)
        self.video_tv_.heading('Key words', text='Key words', anchor=CENTER)
        self.video_tv_.tag_configure('nic', background='white')
        self.video_tv_.tag_configure('nagrane', background='#36c5f5')
        self.video_tv_.tag_configure('obrabiane', background='red')
        self.video_tv_.tag_configure('opublikowane', background='#7cf536')
        self.video_tv_.pack(fill="both", expand=True)
        self.video_tv_.bind("<Double-1>", self.tv_double_click)
        self.video_tv_.bind("<<TreeviewSelect>>", self.tv_select_click)

    def arrange_keyword_tv(self):
        self.keyword_tv_scrollbar_ = Scrollbar(self.bottom_frame_)
        self.keyword_tv_scrollbar_.pack(side=RIGHT, fill=Y)
        self.keyword_tv_ = ttk.Treeview(self.bottom_frame_, yscrollcommand=self.keyword_tv_scrollbar_)
        self.keyword_tv_scrollbar_.config(command=self.keyword_tv_.yview)
        self.keyword_tv_['columns']=('Keyword ID', 'Name', 'Episodes')
        self.keyword_tv_.column('#0', width=0, stretch=NO)
        self.keyword_tv_.column('Keyword ID', anchor=CENTER)
        self.keyword_tv_.column('Name', anchor=CENTER)
        self.keyword_tv_.column('Episodes', anchor=CENTER)
        self.keyword_tv_.heading('#0', text='', anchor=CENTER)
        self.keyword_tv_.heading('Keyword ID', text='Keyword ID', anchor=CENTER)
        self.keyword_tv_.heading('Name', text='Name', anchor=CENTER)
        self.keyword_tv_.heading('Episodes', text='Episodes', anchor=CENTER)
        self.keyword_tv_.pack(fill="both", expand=True)

    def insert_videos_data(self, videos_information_array):
        for i, a in enumerate(videos_information_array):
            state_tag = a[3]
            self.video_tv_.insert(parent='', index = i, values=a, tags=(state_tag,))
        

    def insert_keywords_data(self, keywords_information_array):
        for i, a in enumerate(keywords_information_array):
            self.keyword_tv_.insert(parent='', index = i, values=a)

    def set_up_layout(self):
        self.style_ = ttk.Style()
        self.style_.theme_use("clam")
        self.style_.map('Treeview', foreground=self.fixed_map('foreground'), background=self.fixed_map('background'))     
        self.style_.configure("Treeview.Heading", font=('Calibri', 10,'bold'), background="#bfbfbf")

        self.top_frame_.pack(side=TOP, fill=tk.X)
        #self.top_frame_2_.grid(row=1, column=0)
        self.bottom_frame_.pack(side=TOP, fill="both", expand=True)

        #self.top_frame_.pack(side = TOP)
        #self.bottom_frame_.pack (side=BOTTOM)
        self.top_frame_2_.pack(side = TOP, fill=tk.X)
        self.but_3_add_video_.pack( side=LEFT, expand=True)
        self.but_1_show_videos_.pack( side=LEFT, expand=True)
        self.but_2_show_keywords_.pack( side=LEFT, expand=True)
        

    def create_widgets(self):
        self.background_label_ = tk.Label(self.main_window_)
        self.top_frame_ = Frame(self.main_window_,borderwidth=2,highlightbackground="yellow",highlightcolor="yellow",highlightthickness=1)
        self.bottom_frame_ = Frame(self.main_window_,borderwidth=2,highlightbackground="green",highlightcolor="green",highlightthickness=1)
        self.top_frame_2_ = Frame(self.top_frame_, highlightbackground="blue", highlightthickness=1, highlightcolor="blue")        
        self.but_1_show_videos_ = tk.Button(self.top_frame_2_, text = "Videos Table",command = self.but_1_show_videos_clicked)
        self.but_2_show_keywords_ = tk.Button(self.top_frame_2_, text = "Keywords Table",command = self.but_2_show_keywords_clicked)
        self.but_3_add_video_ = tk.Button(self.top_frame_2_, text = "Add Video",command = self.but_3_add_video_clicked)
        #self.but_8_edit_ = tk.Button(self.top_frame_2_, text = "Edit",command = self.but_8_edit_clicked)
        #self.but_9_delete_ = tk.Button(self.top_frame_2_, text = "Delete",command = self.but_9_delete_clicked)
        
    def switch_button_state(self, button):
        if (button['state'] == tk.NORMAL):
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL

    def tv_double_click(self, event):
        current_record = self.video_tv_.focus()
        values = self.video_tv_.item(current_record, 'values')
        pub.sendMessage("edit_requested", data = values)
    

    def tv_select_click(self, event):
        print("select click")
        self.but_8_edit_["state"] = tk.NORMAL
        self.but_9_delete_["state"] = tk.NORMAL
        current_record = self.video_tv_.focus()
        self.selected_values_ = self.video_tv_.item(current_record, 'values')

    def all_keywords_for_vid_ready(self, data):
        self.keywords_array_for_vid_ = data

    def fixed_map(self, option):
        return [elm for elm in self.style_.map('Treeview', query_opt=option) if
            elm[:2] != ('!disabled', '!selected')]
    

if __name__=="__main__":
    main_window = tk.Tk()
    #WIDTH = 800
    #HEIGHT = 600
    #main_window.geometry("%sx%s" % (WIDTH, HEIGHT))
    #main_window.resizable(0, 0)
    main_window.title("Video Database")
    view=View(main_window)
    view.set_up()
    main_window.mainloop()