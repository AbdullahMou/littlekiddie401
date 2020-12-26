from tkinter import *
import json
import random
import spacy
import vlc
import pyttsx3
import keyboard
import win32clipboard


# from PIL import Image, ImageTk

paragraphs_list1 = []
paragraphs_list2 = []
paragraphs_list3 = []
paragraphs_list4 = []


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
        for i in (home_page, story_page1,story_page2,story_page3,story_page4 ,guessing_game1,guessing_game2,guessing_game3,guessing_game4, song_page):
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
        pick = Label(self, text="To view a story, choose from our categories:")
        pick.pack(padx=10, pady=10)
        first_category = Button(self, text="Collection of our Best", command=lambda: controller.show_frame(story_page1))
        first_category.pack()

        second_category = Button(self, text="Funny", command=lambda: controller.show_frame(story_page2))
        second_category.pack()
        third_category = Button(self, text="Magic", command=lambda: controller.show_frame(story_page3))
        third_category.pack()
        fourth_category = Button(self, text="Moral", command=lambda: controller.show_frame(story_page4))
        fourth_category.pack()
        songs_gen = Label(self, text="Or would you like to listen to a song?")
        songs_gen.pack()
        song = Button(self, text="listen", command=lambda: controller.show_frame(song_page))
        song.pack()


class story_page1(Frame):
    # paragraphs_list = []
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

        with open('../json/top10.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            title = Label(self ,text = data[random_index]['title'])
            title.pack()
            data2 = data[random_index]['pargraph']
            pargraph = Label(self, text= data2)
            pargraph.pack()
            paragraphs_list1.insert(0,data[random_index]['pargraph'])
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(self, text="play audio", command=p.play)
            audio.pack()
            audio = Button(self, text="stop audio", command=p.stop)
            audio.pack()


        def tts():
            engine = pyttsx3.init()  # object creation

            """ RATE"""
            rate = engine.getProperty('rate')  # getting details of current speaking rate
            print(rate)  # printing current voice rate
            engine.setProperty('rate', 150)  # setting up new voice rate

            """VOLUME"""
            volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
            print(volume)  # printing current volume level
            engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

            """VOICE"""
            voices = engine.getProperty('voices')  # getting details of current voice
            # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female


            engine.say('hello')





            # engine.stop()





        tts_button = Button(self, text="listen", command=lambda:tts() )
        tts_button.pack()

        tts_button = Button(self, text="listen", command=lambda: engine.endLoop())
        tts_button.pack()
        # tts_button_stop = Button(self, text="listen", command=lambda:)
        # tts_button_stop.pack()

        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        game = Button(self, text="Take a guessing game ", command=lambda: controller.show_frame(guessing_game1))
        game.pack()


class story_page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        with open('../json/funny.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            title = Label(self, text=data[random_index]['title'])
            title.pack()
            pargraph = Label(self, text=data[random_index]['pargraph'])
            pargraph.pack()

            paragraphs_list2.insert(0,data[random_index]['pargraph'])
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(self, text="play audio", command=p.play)
            audio.pack()
            audio = Button(self, text="stop audio", command=p.stop)
            audio.pack()

        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        game = Button(self, text="Take a guessing game ", command=lambda: controller.show_frame(guessing_game2))
        game.pack()

class story_page3(Frame):


    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        with open('../json/magic.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            title = Label(self, text=data[random_index]['title'])
            title.pack()
            pargraph = Label(self, text=data[random_index]['pargraph'])
            pargraph.pack()

            paragraphs_list3.insert(0, data[random_index]['pargraph'])
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(self, text="play audio", command=p.play)
            audio.pack()
            audio = Button(self, text="stop audio", command=p.stop)
            audio.pack()

        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        game = Button(self, text="Take a guessing game ", command=lambda: controller.show_frame(guessing_game3))
        game.pack()

class story_page4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        with open('../json/big_concept.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            title = Label(self, text=data[random_index]['title'])
            title.pack()
            pargraph = Label(self, text=data[random_index]['pargraph'])
            pargraph.pack()

            paragraphs_list4.insert(0, data[random_index]['pargraph'])
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(self, text="play audio", command=p.play)
            audio.pack()
            audio = Button(self, text="stop audio", command=p.stop)
            audio.pack()

        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        game = Button(self, text="Take a guessing game ", command=lambda: controller.show_frame(guessing_game4))
        game.pack()




class guessing_game1(Frame):
    """
    a class to view the game page.
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        submit = Button(self, text="Submit", command=lambda: controller.show_frame(story_page1))
        submit.pack()


        story_in_game = Label(self, text= paragraphs_list1[0])
        story_in_game.pack()

########
    def game(self, story):
        score = 0
        sp = spacy.load('en_core_web_sm')
        userInput = Entry(self, 'enter a past tense verb > ')
        userInput.pack()
        if spacy.explain(sp(userInput)[0].tag_) == 'verb, past tense' and userInput in story:
            score += 1
        score.pack()

class guessing_game2(Frame):
    """
    a class to view the game page.
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        submit = Button(self, text="Submit", command=lambda: controller.show_frame(story_page1))
        submit.pack()


        story_in_game = Label(self, text= paragraphs_list2[0])
        story_in_game.pack()

class guessing_game3(Frame):
    """
    a class to view the game page.
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        submit = Button(self, text="Submit", command=lambda: controller.show_frame(story_page1))
        submit.pack()


        story_in_game = Label(self, text= paragraphs_list3[0])
        story_in_game.pack()

class guessing_game4(Frame):
    """
    a class to view the game page.
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        submit = Button(self, text="Submit", command=lambda: controller.show_frame(story_page1))
        submit.pack()


        story_in_game = Label(self, text= paragraphs_list4[0])
        story_in_game.pack()

class song_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="song title")
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
        # TKINTER SOURCE CODE: https://www.youtube.com/watch?v=39P4BMvvLdM&ab_channel=IntrotoComputerScience


## SPACY STARTS HERE



if __name__ == '__main__':
    root = Little()
    root.title('Little Kiddie')
    # # load = Image.open('images\\wireframes.jpg')
    # # render = ImageTk.PhotoImage(load)
    # # img = Label(root, image = render)
    # # img.place(x = 0, y= 0)
    root.mainloop()
