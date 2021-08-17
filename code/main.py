from controller import Controller
from tkinter import *

if __name__ == "__main__":
    main_window = Tk()
    WIDTH = 800
    HEIGHT = 800
    main_window.geometry("%sx%s" % (WIDTH, HEIGHT))
    main_window.title("Video Database")
    game_app = Controller(main_window)
    main_window.mainloop()