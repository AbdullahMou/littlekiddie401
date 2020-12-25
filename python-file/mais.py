from tkinter import *
import json
import random
import vlc
# from PIL import Image, ImageTk
class Little(Tk):
    """
    a class to create a container that takes a Frame().
    the Frame allows us to create several pages.
    * show_frame() will view the page
    * tkraise() will allow us to switch between pages
    """
    def __init__(self):
        Tk.__init__(self)
        File(self)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.minsize(640,400)
        for i in (home_page, story_page1, guessing_game, song_page):
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(home_page)
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()  # switch between pages
class home_page(Frame):
    """
    a class that creates the home page
    with buttons to navigate through pages(depending on categories)
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Welcome to littleKiddie")
        title.pack(padx=10, pady=10)
        pick = Label(self, text="To view a story, choose your favorite character:")
        pick.pack(padx=10, pady=10)
        first_category = Button(self, text="Cinderella", command=lambda: controller.show_frame(story_page1))
        first_category.pack()
        second_category = Button(self, text="Mickey Mouse", command=lambda: controller.show_frame(story_page))
        second_category.pack()
        third_category = Button(self, text="Ben Ten", command=lambda: controller.show_frame(story_page))
        third_category.pack()
        fourth_category = Button(self, text="Spongebob", command=lambda: controller.show_frame(story_page))
        fourth_category.pack()
        songs_gen = Label(self, text="Or would you like to listen to a song?")
        songs_gen.pack()
        song = Button(self, text="listen", command=lambda: controller.show_frame(song_page))
        song.pack()


class story_page1(Frame):
    """
    a class to view each story, taken from categories.
    page content:
    - title
    - body (story)
    - audio
    + generated randomly from JSON
    - TTS option (Text To Speech) ##
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        with open('../json/funny.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            title = Label(self ,text = data[random_index]['title'])
            title.pack()
            pargraph = Label(self, text= data[random_index]['pargraph'])
            pargraph.pack()
            p = vlc.MediaPlayer(data[random_index]['audio'])
        audio = Button(self, text="play audio", command=p.play)
        audio.pack()
        audio = Button(self, text="stop audio", command=p.stop)
        audio.pack()

        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        game = Button(self, text="Take a guessing game ", command=lambda: controller.show_frame(guessing_game))
        game.pack()
class guessing_game(Frame):
    """
    a class to view the game page.
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        submit = Button(self, text="Submit", command=lambda: controller.show_frame(story_page))
        submit.pack()
class song_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="song title") ##must be a variable
        label.pack(padx=10, pady=10)
        start_page = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        start_page.pack()
class File:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)



if __name__ == '__main__':
    root = Little()
    root.title('Little Kiddie')
    # load = Image.open('images\\wireframes.jpg')
    # render = ImageTk.PhotoImage(load)
    # img = Label(root, image = render)
    # img.place(x = 0, y= 0)
    root.mainloop()