import urllib.request
from tkinter import *
import json
import random
import pyttsx3
import spacy
import vlc
from tkinter import messagebox
from PyDictionary import PyDictionary
import inflect
import string
import  pygame
from PIL import Image, ImageTk
from io import BytesIO
import os



dictionary = PyDictionary()
sp = spacy.load('en_core_web_sm')
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
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.geometry('1920x1080')
        for i in (
                home_page, story_page1, story_page2, story_page3, story_page4, guessing_game1, guessing_game2,
                guessing_game3,
                guessing_game4,song_page):
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
    callback puzzel and piano are functions for the last two features
    """

    def __init__(self, parent, controller):
        """
        buttons and labels
        """
        Frame.__init__(self, parent)
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\mais97.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        c.create_image(0, 0, anchor=NW, image=img)

        c.create_text(750, 100, text='Welcome to LittleKiddie', font=("Comic Sans MS", 30))
        c.create_text(320, 480, text="Best Stories", font=("Comic Sans MS", 20))

        img_button = ImageTk.PhotoImage(Image.open('..\\images\\numbers12.png').resize((250, 250), Image.ANTIALIAS))
        first_category = Button(c, image=img_button, command=lambda: controller.show_frame(story_page1))
        first_category.place(x=200, y=200)
        first_category.background = img_button

        c.create_text(620, 480, text="Funny Stories", font=("Comic Sans MS", 20))

        img_button2 = ImageTk.PhotoImage(Image.open('..\\images\\patric.jpg').resize((250, 250), Image.ANTIALIAS))
        second_category = Button(c, image=img_button2, command=lambda: controller.show_frame(story_page2))
        second_category.place(x=490, y=200)
        second_category.background = img_button2

        c.create_text(920, 480, text="Magical Stories", font=("Comic Sans MS", 20))

        img_button3 = ImageTk.PhotoImage(Image.open('..\\images\\unicorn.jpg').resize((250, 250), Image.ANTIALIAS))
        third_category = Button(c, image=img_button3, command=lambda: controller.show_frame(story_page3))
        third_category.place(x=790, y=200)
        third_category.background = img_button3

        c.create_text(1220, 480, text="Moral Stories", font=("Comic Sans MS", 20))

        img_button4 = ImageTk.PhotoImage(Image.open('..\\images\\morallove.png').resize((250, 250), Image.ANTIALIAS))
        fourth_category = Button(c, image=img_button4, command=lambda: controller.show_frame(story_page4))
        fourth_category.place(x=1080, y=200)
        fourth_category.background = img_button4

        img_button5 = ImageTk.PhotoImage(Image.open('..\\images\\songs97.jpg').resize((250, 150), Image.ANTIALIAS))
        song = Button(c, image=img_button5, command=lambda: controller.show_frame(song_page))
        song.place(x=870, y=570)
        song.background = img_button5

        def callback():
            """
            to run puzzle file
            """
            filename = 'puzzle_game.py'
            os.system(filename)

        img_button6 = ImageTk.PhotoImage(Image.open('..\\images\\slide-pu.jpg').resize((250, 150), Image.ANTIALIAS))
        game = Button(self, image=img_button6, command=lambda: callback())
        game.place(x=585, y=570)
        game.background = img_button6

        def callback_piano():
            """
            to run piano file
            """
            filename = 'piano.py'
            os.system(filename)

        img_button7 = ImageTk.PhotoImage(Image.open('..\\images\\piano.jpg').resize((250, 150), Image.ANTIALIAS))
        game2 = Button(self, image=img_button7, command=lambda: callback_piano())
        game2.place(x=300, y=570)
        game2.background = img_button7



class story_page1(Frame):
    """
    a class to view each  best10 story
    page content:
    - title
    - body (story)
    - audio
    - generated randomly from JSON
    - navigate to guessing game page

    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        """
        creating a canvas to display everything 
        """
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\hi.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        c.create_image(0, 0, anchor=NW, image=img)

        with open('../json/top10.json') as fp:
            """
            getting the data from the json file randomly 
            """
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            data3 = data[random_index]['image']
            URL = data3
            u = urllib.request.urlopen(URL)
            raw_data = u.read()
            u.close()
            im = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(im.resize((240, 240), Image.ANTIALIAS))
            label = Label(c, image=photo)
            label.image = photo
            label.place(x=310, y=230)
            c.create_text(420, 200, text=data[random_index]['title'], font=("Comic Sans MS", 20))
            data2 = data[random_index]['pargraph']

            """
            to display the body of the story in a scrollbar
            """
            S = Scrollbar(c)
            T = Text(c, height=20, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
            S.pack(side=RIGHT, fill=Y)
            T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
            T.tag_configure('big', font=('Verdana', 20, 'bold'))
            T.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
            T.place(x=850, y=140)
            T.insert(END, data2)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set, state=DISABLED)
            paragraphs_list1.insert(0, data[random_index]['pargraph'])
            """
            audio
            """
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(c, text="play audio", height=3, width=15, bg='#5bc6c9', command=p.play)
            audio.place(x=220, y=500)
            audio = Button(c, text="stop audio", height=3, width=15, bg='#5bc6c9', command=p.stop)
            audio.place(x=340, y=500)
        """
        buttons for the gussing game and the home page 
        """
        home = Button(c, text="Home Page", height=3, width=15, bg='#5bc6c9',command=lambda: controller.show_frame(home_page))
        home.place(x=460, y=500)
        game = Button(c, text="Guessing Game", height=3, width=15, bg='#5bc6c9',command=lambda: controller.show_frame(guessing_game1))
        game.place(x=580, y=500)


class story_page2(Frame):
    """
    a class to view each  funny story
    page content:
    - title
    - body (story)
    - audio
    - generated randomly from JSON
    - navigate to guessing game page
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        """
        creating a canvas to display everything 
        """
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\hi.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        c.create_image(0, 0, anchor=NW, image=img)

        with open('../json/funny.json') as fp:
            """
            getting the data from the json file randomly 
            """
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            data3 = data[random_index]['image']
            URL = data3
            u = urllib.request.urlopen(URL)
            raw_data = u.read()
            u.close()
            im = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(im.resize((240, 240), Image.ANTIALIAS))
            label = Label(c, image=photo)
            label.image = photo
            label.place(x=310, y=230)
            c.create_text(420, 200, text=data[random_index]['title'], font=("Comic Sans MS", 20))
            data2 = data[random_index]['pargraph']

            """
            to display the body of the story in a scrollbar
            """
            S = Scrollbar(c)
            T = Text(c, height=20, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
            S.pack(side=RIGHT, fill=Y)
            T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
            T.tag_configure('big', font=('Verdana', 20, 'bold'))
            T.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
            T.place(x=850, y=140)
            T.insert(END, data2)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set, state=DISABLED)
            paragraphs_list2.insert(0, data[random_index]['pargraph'])

            """
            audio
            """
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(c, text="play audio", height=3, width=15, bg='#5bc6c9', command=p.play)
            audio.place(x=220, y=500)
            audio = Button(c, text="stop audio", height=3, width=15, bg='#5bc6c9', command=p.stop)
            audio.place(x=340, y=500)

        """
        buttons for the gussing game and the home page 
        """
        home = Button(c, text="Home Page", height=3, width=15, bg='#5bc6c9',command=lambda: controller.show_frame(home_page))
        home.place(x=460, y=500)
        game = Button(c, text="Guessing Game", height=3, width=15, bg='#5bc6c9',command=lambda: controller.show_frame(guessing_game2))
        game.place(x=580, y=500)


class story_page3(Frame):
    """
       a class to view each  magical story
       page content:
       - title
       - body (story)
       - audio
       - generated randomly from JSON
       - navigate to guessing game page
       """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        """
        creating a canvas to display everything 
        """
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\hi.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        c.create_image(0, 0, anchor=NW, image=img)
        """
        getting the data from the json file randomly 
        """
        with open('../json/magic.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            data3 = data[random_index]['image']
            URL = data3
            u = urllib.request.urlopen(URL)
            raw_data = u.read()
            u.close()
            im = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(im.resize((240, 240), Image.ANTIALIAS))
            label = Label(c, image=photo)
            label.image = photo
            label.place(x=310, y=230)
            c.create_text(420, 200, text=data[random_index]['title'], font=("Comic Sans MS", 20))
            data2 = data[random_index]['pargraph']

            """
            to display the body of the story in a scrollbar
            """
            S = Scrollbar(c)
            T = Text(c, height=20, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
            S.pack(side=RIGHT, fill=Y)
            T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
            T.tag_configure('big', font=('Verdana', 20, 'bold'))
            T.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
            T.place(x=850, y=140)
            T.insert(END, data2)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set, state=DISABLED)
            paragraphs_list3.insert(0, data[random_index]['pargraph'])

            """
            audio
            """
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(c, text="play audio", height=3, width=15, bg='#5bc6c9', command=p.play)
            audio.place(x=220, y=500)
            audio = Button(c, text="stop audio", height=3, width=15, bg='#5bc6c9', command=p.stop)
            audio.place(x=340, y=500)

        """
        buttons for the gussing game and the home page 
        """
        home = Button(c, text="Home Page", height=3, width=15, bg='#5bc6c9',command=lambda: controller.show_frame(home_page))
        home.place(x=460, y=500)
        game = Button(c, text="Guessing Game", height=3, width=15, bg='#5bc6c9',command=lambda: controller.show_frame(guessing_game3))
        game.place(x=580, y=500)


class story_page4(Frame):
    """
       a class to view each  moral story,
       page content:
       - title
       - body (story)
       - audio
       - generated randomly from JSON
       - navigate to guessing game page
       """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        c = Canvas(self)
        """
         creating a canvas to display everything 
        """
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\hi.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img  # Keep a reference in case this code is put in a function.
        c.create_image(0, 0, anchor=NW, image=img)

        with open('../json/big_concept.json') as fp:
            """
            getting the data from the json file randomly 
            """
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            data3 = data[random_index]['image']
            URL = data3
            u = urllib.request.urlopen(URL)
            raw_data = u.read()
            u.close()
            im = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(im.resize((240, 240), Image.ANTIALIAS))
            label = Label(c, image=photo)
            label.image = photo
            label.place(x=310, y=230)
            c.create_text(420, 200, text=data[random_index]['title'], font=("Comic Sans MS", 20))
            data2 = data[random_index]['pargraph']

            """
            to display the body of the story in a scrollbar
            """
            S = Scrollbar(c)
            T = Text(c, height=20, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
            S.pack(side=RIGHT, fill=Y)
            T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
            T.tag_configure('big', font=('Verdana', 20, 'bold'))
            T.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
            T.place(x=850, y=140)
            T.insert(END, data2)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set, state=DISABLED)
            paragraphs_list4.insert(0, data[random_index]['pargraph'])

            """
            audio
            """
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(c, text="play audio", height=3, width=15, bg='#5bc6c9', command=p.play)
            audio.place(x=220, y=500)
            audio = Button(c, text="stop audio", height=3, width=15, bg='#5bc6c9', command=p.stop)
            audio.place(x=340, y=500)

        """
        buttons for the gussing game and the home page 
        """
        home = Button(c, text="Home Page", height=3, width=15, bg='#5bc6c9',command=lambda: controller.show_frame(home_page))
        home.place(x=460, y=500)
        game = Button(c, text="Guessing Game", height=3, width=15, bg='#5bc6c9',command=lambda: controller.show_frame(guessing_game4))
        game.place(x=580, y=500)


def tts(sentence):
    """
    a function that takes a sentence as  a param .
    using pyttsx3 it plays this sentence

    """
    engine = pyttsx3.init()
    engine.getProperty('rate')
    engine.setProperty('rate', 130)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(sentence)
    engine.runAndWait()


class guessing_game1(Frame):
    """
    a class to view the game page. for the best10 stories
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        """
         creating a canvas to display everything 
        """
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\guessing-background.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        c.create_image(0, 0, anchor=NW, image=img)

        """
        to display the body of the story in a scrollbar
        """
        S = Scrollbar(c)
        T = Text(c, height=31, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
        S.pack(side=RIGHT, fill=Y)
        T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        T.tag_configure('big', font=('Verdana', 20, 'bold'))
        T.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
        T.place(x=150, y=70)
        T.insert(END, paragraphs_list1[0])
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set, state=DISABLED)

        """
        finding and pushing all the adjectives and nouns in order to creat the questions randomly 
        """
        adjectives = []
        nouns = []
        for i in paragraphs_list1[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'adjective':
                adjectives.append(i)
        random_adjective = random.choice(adjectives).translate(str.maketrans('', '', string.punctuation))
        random_adjective2 = random.choice(adjectives).translate(str.maketrans('', '', string.punctuation))
        for i in paragraphs_list1[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'noun, plural':
                nouns.append(i)
        random_noun = random.choice(nouns).translate(str.maketrans('', '', string.punctuation))

        """
        questions and the scores 
        """
        global score
        score = 0
        ###########QUESTION1##############
        sentence1 = ' question number 1 : Enter a past tense verb from the above story'
        q1 = Button(c, text="play audio", command=lambda: tts(sentence1))
        q1.place(x=1225, y=55, height=35, width=80)
        c.create_text(985, 70, text='Enter a past tense verb from the above story', font=("Comic Sans MS", 15))
        enter_question1 = Entry(c)
        enter_question1.place(x=850, y=100, height=40, width=300)

        ###########QUESTION2##############
        sentence2 = 'question number 2 : Enter a personal pronoun from the above story'
        q2 = Button(c, text="play audio", command=lambda: tts(sentence2))
        q2.place(x=1225, y=185, height=35, width=80)
        c.create_text(1000, 200, text='Enter a personal pronoun from the above story', font=("Comic Sans MS", 15))
        enter_question2 = Entry(c)
        enter_question2.place(x=850, y=225, height=40, width=300)

        ###########QUESTION3##############
        T.tag_config(f' {random_adjective}', background='#FF80DF')
        T.tag_config(f' {random_adjective2}', background='#99BBFF')
        def search(text_widget, keyword, tag):
            pos = '1.0'
            while True:
                idx = text_widget.search(keyword, pos, END)
                if not idx:
                    break
                pos = '{}+{}c'.format(idx, len(keyword))
                text_widget.tag_add(tag, idx, pos)
        search(T, f' {random_adjective}', f' {random_adjective}')
        search(T, f' {random_adjective2}', f' {random_adjective2}')
        sentence3 = f'question number 3 : What is the meaning of {random_adjective}?'
        q3 = Button(c, text="play audio", command=lambda: tts(sentence3))
        q3.place(x=1225, y=315, height=35, width=80)
        c.create_text(925, 330, text=f'What is the meaning of {random_adjective}?', font=("Comic Sans MS", 15))
        enter_question3 = Entry(c)
        enter_question3.place(x=850, y=350, height=40, width=300)
        synonyms_list = dictionary.synonym(random_adjective)
        random.choice(synonyms_list)
        random_synonym2 = random.choice(synonyms_list)
        def hint_pop_up():
            """
            creating the hint
            """
            messagebox.showinfo('Hint', f'The answer is {random_synonym2}')
        img_button_hint = ImageTk.PhotoImage(Image.open('..\\images\\lightbulb.png').resize((45, 30), Image.ANTIALIAS))
        hint_button = Button(c,bg='#dac7ff',bd=0, image=img_button_hint, command=hint_pop_up)
        hint_button.place(x=800, y=352)
        hint_button.background = img_button_hint

        ###########QUESTION4##############
        sentence4 = f'question number 4 : What is the opposite of {random_adjective2}?'
        q4 = Button(c, text="play audio", command=lambda: tts(sentence4))
        q4.place(x=1225, y=435, height=35, width=80)
        c.create_text(945, 450, text=f'What is the opposite of {random_adjective2}?', font=("Comic Sans MS", 15))
        antonym_list = dictionary.antonym(random_adjective2)
        syn_list = dictionary.synonym(random_adjective2)
        random_antonym = random.choice(antonym_list).translate(str.maketrans('', '', string.punctuation))
        random_syn = random.choice(syn_list).translate(str.maketrans('', '', string.punctuation))
        m = IntVar()
        option1 = Radiobutton(c, text=f'(a){random_antonym}', variable=m, value=1, font=("Comic Sans MS", 12),bg='#DAC7FF', selectcolor='#F9C6DE', activebackground='#F9C6DE', highlightcolor='#F9C6DE')
        option1.place(x=900, y=475)
        option2 = Radiobutton(c, text=f'(b){random_syn}', variable=m, value=2, font=("Comic Sans MS", 12), bg='#DAC7FF', selectcolor='#F9C6DE', activebackground='#F9C6DE', highlightcolor='#F9C6DE')
        option2.place(x=900, y=525)

        ############QUESTION5##############
        sentence5 = f'question number 5 : What is the singular noun of {random_noun}?'
        q5 = Button(c, text="play audio", command=lambda: tts(sentence5))
        q5.place(x=1225, y=585, height=35, width=80)
        c.create_text(965, 600, text=f'What is the singular noun of {random_noun}?', font=("Comic Sans MS", 15))
        enter_question5 = Entry(c)
        enter_question5.place(x=850, y=650, height=40, width=300)
        p = inflect.engine()

        def pop_up():
            """
            to view the game's result
            """
            global score
            user_input_question1 = enter_question1.get()
            user_input_question2 = enter_question2.get()
            user_input_question3 = enter_question3.get()
            user_input_question4 = m.get()
            user_input_question5 = enter_question5.get()
            if spacy.explain(sp(user_input_question1.lower())[0].tag_) == 'verb, past tense' and user_input_question1 in \
                    paragraphs_list1[0]:
                score += 1
            if spacy.explain(
                    sp(user_input_question2.lower())[0].tag_) == 'pronoun, personal' and user_input_question2 in \
                    paragraphs_list1[0]:
                score += 1
            if user_input_question3 in synonyms_list:
                score += 1
            if user_input_question4 == 1:
                score += 1
            if user_input_question5 == p.singular_noun(random_noun):
                score += 1
            messagebox.showinfo('Result', f'Your score is {str(score)}. Thanks for playing.')
            enter_question1.delete(0, 'end')
            enter_question2.delete(0, 'end')
            enter_question3.delete(0, 'end')
            enter_question5.delete(0, 'end')
            score = 0
        """
        submit button
        """
        submit = Button(c, bg='#3f51b5', font='bold', text="Submit", command=pop_up)
        submit.place(x=925, y=725, height=45, width=150)
        """
        homepage button
        """
        home = Button(c, bg='#3f51b5', font='bold', text="Home Page", command=lambda: controller.show_frame(home_page))
        home.place(x=283, y=725, height=45, width=150)



class guessing_game2(Frame):
    """
    a class to view the game page. for the funny stories
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        """
         creating a canvas to display everything 
        """
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\guessing-background.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        c.create_image(0, 0, anchor=NW, image=img)

        """
         to display the body of the story in a scrollbar
        """
        S = Scrollbar(c)
        T = Text(c, height=31, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
        S.pack(side=RIGHT, fill=Y)
        T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        T.tag_configure('big', font=('Verdana', 20, 'bold'))
        T.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
        T.place(x=150, y=70)
        T.insert(END, paragraphs_list2[0])
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set, state=DISABLED)

        """
        finding and pushing all the adjectives and nouns in order to creat the questions randomly 
        """
        adjectives = []
        nouns = []
        for i in paragraphs_list2[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'adjective':
                adjectives.append(i)
        random_adjective = random.choice(adjectives).translate(str.maketrans('', '', string.punctuation))
        random_adjective2 = random.choice(adjectives)
        for i in paragraphs_list2[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'noun, plural':
                nouns.append(i)
        random_noun = random.choice(nouns).translate(str.maketrans('', '', string.punctuation))

        """
        questions and the scores 
        """
        global score
        score = 0
        ###########QUESTION1##############
        sentence1 = ' question number 1 : Enter a past tense verb from the above story'
        q1 = Button(c, text="play audio", command=lambda: tts(sentence1))
        q1.place(x=1225, y=55, height=35, width=80)
        c.create_text(985, 70, text='Enter a past tense verb from the above story', font=("Comic Sans MS", 15))
        enter_question1 = Entry(c)
        enter_question1.place(x=850, y=100, height=40, width=300)

        ###########QUESTION2##############
        sentence2 = 'question number 2 : Enter a personal pronoun from the above story'
        q2 = Button(c, text="play audio", command=lambda: tts(sentence2))
        q2.place(x=1225, y=185, height=35, width=80)
        c.create_text(1000, 200, text='Enter a personal pronoun from the above story', font=("Comic Sans MS", 15))
        enter_question2 = Entry(c)
        enter_question2.place(x=850, y=225, height=40, width=300)

        ###########QUESTION3##############
        T.tag_config(f' {random_adjective}', background='#FF80DF')
        T.tag_config(f' {random_adjective2}', background='#99BBFF')
        def search(text_widget, keyword, tag):
            pos = '1.0'
            while True:
                idx = text_widget.search(keyword, pos, END)
                if not idx:
                    break
                pos = '{}+{}c'.format(idx, len(keyword))
                text_widget.tag_add(tag, idx, pos)
        search(T, f' {random_adjective}', f' {random_adjective}')
        search(T, f' {random_adjective2}', f' {random_adjective2}')
        sentence3 = f'question number 3 : What is the meaning of {random_adjective}?'
        q3 = Button(c, text="play audio", command=lambda: tts(sentence3))
        q3.place(x=1225, y=315, height=35, width=80)
        c.create_text(925, 330, text=f'What is the meaning of {random_adjective}?', font=("Comic Sans MS", 15))
        enter_question3 = Entry(c)
        enter_question3.place(x=850, y=350, height=40, width=300)
        synonyms_list = dictionary.synonym(random_adjective)
        random.choice(synonyms_list)
        random_synonym2 = random.choice(synonyms_list)

        def hint_pop_up():
            """
            creating the hint
            """
            messagebox.showinfo('Hint', f'The answer is {random_synonym2}')

        img_button_hint = ImageTk.PhotoImage(Image.open('..\\images\\lightbulb.png').resize((45, 30), Image.ANTIALIAS))
        hint_button = Button(c,bg='#dac7ff',bd=0, image=img_button_hint, command=hint_pop_up)
        hint_button.place(x=800, y=352)
        hint_button.background = img_button_hint

        ###########QUESTION4##############
        sentence4 = f'question number 4 : What is the opposite of {random_adjective2}?'
        q4 = Button(c, text="play audio", command=lambda: tts(sentence4))
        q4.place(x=1225, y=435, height=35, width=80)
        c.create_text(945, 450, text=f'What is the opposite of {random_adjective2}?', font=("Comic Sans MS", 15))
        antonym_list = dictionary.antonym(random_adjective2)
        syn_list = dictionary.synonym(random_adjective2)
        random_syn = random.choice(syn_list).translate(str.maketrans('', '', string.punctuation))
        random_antonym = random.choice(antonym_list).translate(str.maketrans('', '', string.punctuation))
        m = IntVar()
        option1 = Radiobutton(c, text=f'(a){random_antonym}', variable=m, value=1, font=("Comic Sans MS", 12),bg='#DAC7FF', selectcolor='#F9C6DE', activebackground='#F9C6DE', highlightcolor='#F9C6DE')
        option1.place(x=900, y=475)
        option2 = Radiobutton(c, text=f'(b){random_syn}', variable=m, value=2, font=("Comic Sans MS", 12),bg='#DAC7FF', selectcolor='#F9C6DE', activebackground='#F9C6DE', highlightcolor='#F9C6DE')
        option2.place(x=900, y=525)

        ############QUESTION5##############
        sentence5 = f'question number 5 : What is the singular noun of {random_noun}?'
        q5 = Button(c, text="play audio", command=lambda: tts(sentence5))
        q5.place(x=1225, y=585, height=35, width=80)
        c.create_text(965, 600, text=f'What is the singular noun of {random_noun}?', font=("Comic Sans MS", 15))
        enter_question5 = Entry(c)
        enter_question5.place(x=850, y=650, height=40, width=300)
        p = inflect.engine()

        def pop_up():
            """
            to view the game's result
            """
            global score
            user_input_question1 = enter_question1.get()
            user_input_question2 = enter_question2.get()
            user_input_question3 = enter_question3.get()
            user_input_question4 = m.get()
            user_input_question5 = enter_question5.get()
            if spacy.explain(sp(user_input_question1.lower())[0].tag_) == 'verb, past tense' and user_input_question1 in \
                    paragraphs_list2[0]:
                score += 1
            if spacy.explain(
                    sp(user_input_question2.lower())[0].tag_) == 'pronoun, personal' and user_input_question2 in \
                    paragraphs_list2[0]:
                score += 1
            if user_input_question3 in synonyms_list:
                score += 1
            if user_input_question4 == 1:
                score += 1
            if user_input_question5 == p.singular_noun(random_noun):
                score += 1
            messagebox.showinfo('Result', f'Your score is {str(score)}. Thanks for playing.')
            enter_question1.delete(0, 'end')
            enter_question2.delete(0, 'end')
            enter_question3.delete(0, 'end')
            enter_question5.delete(0, 'end')
            score = 0
        """
        submit buttons
        """
        submit = Button(self, bg='#3f51b5', font='bold', text="Submit", command=pop_up)
        submit.place(x=925, y=725, height=45, width=150)
        """
        homepage button
        """
        home = Button(c,  bg='#3f51b5', font='bold',text="Home Page", command=lambda: controller.show_frame(home_page))
        home.place(x=283, y=725, height=45, width=150)


class guessing_game3(Frame):
    """
    a class to view the game page. for the magical stories
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        """
         creating a canvas to display everything 
        """
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\guessing-background.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        c.create_image(0, 0, anchor=NW, image=img)

        """
         to display the body of the story in a scrollbar
        """
        S = Scrollbar(c)
        T = Text(c, height=31, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
        S.pack(side=RIGHT, fill=Y)
        T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        T.tag_configure('big', font=('Verdana', 20, 'bold'))
        T.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
        T.place(x=150, y=70)
        T.insert(END, paragraphs_list3[0])
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set, state=DISABLED)

        """
        finding and pushing all the adjectives and nouns in order to creat the questions randomly 
        """
        adjectives = []
        nouns = []
        for i in paragraphs_list3[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'adjective':
                adjectives.append(i)
        random_adjective = random.choice(adjectives).translate(str.maketrans('', '', string.punctuation))
        random_adjective2 = random.choice(adjectives)
        for i in paragraphs_list3[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'noun, plural':
                nouns.append(i)
        random_noun = random.choice(nouns).translate(str.maketrans('', '', string.punctuation))

        """
        questions and the scores 
        """
        global score
        score = 0
        ###########QUESTION1##############
        sentence1 = ' question number 1 : Enter a past tense verb from the above story'
        q1 = Button(c, text="play audio", command=lambda: tts(sentence1))
        q1.place(x=1225, y=55, height=35, width=80)
        c.create_text(985, 70, text='Enter a past tense verb from the above story', font=("Comic Sans MS", 15))
        enter_question1 = Entry(c)
        enter_question1.place(x=850, y=100, height=40, width=300)

        ###########QUESTION2##############
        sentence2 = 'question number 2 : Enter a personal pronoun from the above story'
        q2 = Button(c, text="play audio", command=lambda: tts(sentence2))
        q2.place(x=1225, y=185, height=35, width=80)
        c.create_text(1000, 200, text='Enter a personal pronoun from the above story', font=("Comic Sans MS", 15))
        enter_question2 = Entry(c)
        enter_question2.place(x=850, y=225, height=40, width=300)

        ###########QUESTION3##############
        T.tag_config(f' {random_adjective}', background='#FF80DF')
        T.tag_config(f' {random_adjective2}', background='#99BBFF')
        def search(text_widget, keyword, tag):
            pos = '1.0'
            while True:
                idx = text_widget.search(keyword, pos, END)
                if not idx:
                    break
                pos = '{}+{}c'.format(idx, len(keyword))
                text_widget.tag_add(tag, idx, pos)
        search(T, f' {random_adjective}', f' {random_adjective}')
        search(T, f' {random_adjective2}', f' {random_adjective2}')
        sentence3 = f'question number 3 : What is the meaning of {random_adjective}?'
        q3 = Button(c, text="play audio", command=lambda: tts(sentence3))
        q3.place(x=1225, y=315, height=35, width=80)
        c.create_text(925, 330, text=f'What is the meaning of {random_adjective}?', font=("Comic Sans MS", 15))
        enter_question3 = Entry(c)
        enter_question3.place(x=850, y=350, height=40, width=300)
        synonyms_list = dictionary.synonym(random_adjective)
        random.choice(synonyms_list)
        random_synonym2 = random.choice(synonyms_list)
        def hint_pop_up():
            """
            creating the hint
            """
            messagebox.showinfo('Hint', f'The answer is {random_synonym2}')
        img_button_hint = ImageTk.PhotoImage(Image.open('..\\images\\lightbulb.png').resize((45, 30), Image.ANTIALIAS))
        hint_button = Button(c,bg='#dac7ff',bd=0, image=img_button_hint, command=hint_pop_up)
        hint_button.place(x=800, y=352)
        hint_button.background = img_button_hint

        ###########QUESTION4##############
        sentence4 = f'question number 4 : What is the opposite of {random_adjective2}?'
        q4 = Button(c, text="play audio", command=lambda: tts(sentence4))
        q4.place(x=1225, y=435, height=35, width=80)
        c.create_text(945, 450, text=f'What is the opposite of {random_adjective2}?', font=("Comic Sans MS", 15))
        antonym_list = dictionary.antonym(random_adjective2)
        syn_list = dictionary.synonym(random_adjective2)
        random_syn = random.choice(syn_list).translate(str.maketrans('', '', string.punctuation))
        random_antonym = random.choice(antonym_list).translate(str.maketrans('', '', string.punctuation))
        m = IntVar()
        option1 = Radiobutton(c, text=f'(a){random_antonym}', variable=m, value=1, font=("Comic Sans MS", 12), bg='#DAC7FF', selectcolor='#F9C6DE', activebackground='#F9C6DE', highlightcolor='#F9C6DE')
        option1.place(x=900, y=475)
        option2 = Radiobutton(c, text=f'(b){random_syn}', variable=m, value=2, font=("Comic Sans MS", 12), bg='#DAC7FF', selectcolor='#F9C6DE', activebackground='#F9C6DE', highlightcolor='#F9C6DE')
        option2.place(x=900, y=525)

        ############QUESTION5##############
        sentence5 = f'question number 5 : What is the singular noun of {random_noun}?'
        q5 = Button(c, text="play audio", command=lambda: tts(sentence5))
        q5.place(x=1225, y=585, height=35, width=80)
        c.create_text(965, 600, text=f'What is the singular noun of {random_noun}?', font=("Comic Sans MS", 15))
        enter_question5 = Entry(c)
        enter_question5.place(x=850, y=650, height=40, width=300)
        p = inflect.engine()

        def pop_up():
            """
            to view the game's result
            """

            global score
            user_input_question1 = enter_question1.get()
            user_input_question2 = enter_question2.get()
            user_input_question3 = enter_question3.get()
            user_input_question4 = m.get()
            user_input_question5 = enter_question5.get()
            if spacy.explain(sp(user_input_question1.lower())[0].tag_) == 'verb, past tense' and user_input_question1 in \
                    paragraphs_list3[0]:
                score += 1
            if spacy.explain(
                    sp(user_input_question2.lower())[0].tag_) == 'pronoun, personal' and user_input_question2 in \
                    paragraphs_list3[0]:
                score += 1
            if user_input_question3 in synonyms_list:
                score += 1
            if user_input_question4 == 1:
                score += 1
            if user_input_question5 == p.singular_noun(random_noun):
                score += 1
            messagebox.showinfo('Result', f'Your score is {str(score)}. Thanks for playing.')
            enter_question1.delete(0, 'end')
            enter_question2.delete(0, 'end')
            enter_question3.delete(0, 'end')
            enter_question5.delete(0, 'end')
            score = 0

        """
        submit button
        """
        submit = Button(self, bg='#3f51b5', font='bold', text="Submit", command=pop_up)
        submit.place(x=925, y=725, height=45, width=150)
        """
        home page 
        """
        home = Button(c,  bg='#3f51b5', font='bold',text="Home Page", command=lambda: controller.show_frame(home_page))
        home.place(x=283, y=725, height=45, width=150)



class guessing_game4(Frame):
    """
    a class to view the game page. for the moral stories
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        c = Canvas(self)
        """
         creating a canvas to display everything 
        """
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\guessing-background.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        c.create_image(0, 0, anchor=NW, image=img)

        """
         to display the body of the story in a scrollbar
        """
        S = Scrollbar(c)
        T = Text(c, height=31, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
        S.pack(side=RIGHT, fill=Y)
        T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        T.tag_configure('big', font=('Verdana', 20, 'bold'))
        T.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
        T.place(x=150, y=70)
        T.insert(END, paragraphs_list4[0])
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set, state=DISABLED)

        """
        finding and pushing all the adjectives and nouns in order to creat the questions randomly 
        """
        adjectives = []
        nouns = []
        for i in paragraphs_list4[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'adjective':
                adjectives.append(i)
        random_adjective = random.choice(adjectives).translate(str.maketrans('', '', string.punctuation))

        random_adjective2 = random.choice(adjectives)
        for i in paragraphs_list4[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'noun, plural':
                nouns.append(i)
        random_noun = random.choice(nouns).translate(str.maketrans('', '', string.punctuation))

        """
        questions and the scores 
        """
        global score
        score = 0
        ###########QUESTION1##############
        sentence1 = ' question number 1 : Enter a past tense verb from the above story'
        q1 = Button(c, text="play audio", command=lambda: tts(sentence1))
        q1.place(x=1225, y=55, height=35, width=80)
        c.create_text(985, 70, text='Enter a past tense verb from the above story', font=("Comic Sans MS", 15))
        enter_question1 = Entry(c)
        enter_question1.place(x=850, y=100, height=40, width=300)

        ###########QUESTION2##############
        sentence2 = 'question number 2 : Enter a personal pronoun from the above story'
        q2 = Button(c, text="play audio", command=lambda: tts(sentence2))
        q2.place(x=1225, y=185, height=35, width=80)
        c.create_text(1000, 200, text='Enter a personal pronoun from the above story', font=("Comic Sans MS", 15))
        enter_question2 = Entry(c)
        enter_question2.place(x=850, y=225, height=40, width=300)

        ###########QUESTION3##############
        T.tag_config(f' {random_adjective}', background='#FF80DF')
        T.tag_config(f' {random_adjective2}', background='#99BBFF')
        def search(text_widget, keyword, tag):
            pos = '1.0'
            while True:
                idx = text_widget.search(keyword, pos, END)
                if not idx:
                    break
                pos = '{}+{}c'.format(idx, len(keyword))
                text_widget.tag_add(tag, idx, pos)
        search(T, f' {random_adjective}', f' {random_adjective}')
        search(T, f' {random_adjective2}', f' {random_adjective2}')
        sentence3 = f'question number 3 : What is the meaning of {random_adjective}?'
        q3 = Button(c, text="play audio", command=lambda: tts(sentence3))
        q3.place(x=1225, y=315, height=35, width=80)
        c.create_text(925, 330, text=f'What is the meaning of {random_adjective}?', font=("Comic Sans MS", 15))
        enter_question3 = Entry(c)
        enter_question3.place(x=850, y=350, height=40, width=300)
        synonyms_list = dictionary.synonym(random_adjective)
        random.choice(synonyms_list)
        random_synonym2 = random.choice(synonyms_list)
        def hint_pop_up():
            """
            creating the hint
            """
            messagebox.showinfo('Hint', f'The answer is {random_synonym2}')
        img_button_hint = ImageTk.PhotoImage(Image.open('..\\images\\lightbulb.png').resize((45, 30), Image.ANTIALIAS))
        hint_button = Button(c,bg='#dac7ff',bd=0, image=img_button_hint, command=hint_pop_up)
        hint_button.place(x=800, y=352)
        hint_button.background = img_button_hint

        ###########QUESTION4##############
        sentence4 = f'question number 4 : What is the opposite of {random_adjective2}?'
        q4 = Button(c, text="play audio", command=lambda: tts(sentence4))
        q4.place(x=1225, y=435, height=35, width=80)
        c.create_text(945, 450, text=f'What is the opposite of {random_adjective2}?', font=("Comic Sans MS", 15))
        antonym_list = dictionary.antonym(random_adjective2)
        syn_list = dictionary.synonym(random_adjective2)
        random_syn = random.choice(syn_list).translate(str.maketrans('', '', string.punctuation))
        random_antonym = random.choice(antonym_list).translate(str.maketrans('', '', string.punctuation))
        m = IntVar()
        option1 = Radiobutton(c, text=f'(a){random_antonym}', variable=m, value=1, font=("Comic Sans MS", 12), bg='#DAC7FF', selectcolor='#F9C6DE', activebackground='#F9C6DE', highlightcolor='#F9C6DE')
        option1.place(x=900, y=475)
        option2 = Radiobutton(c, text=f'(b){random_syn}', variable=m, value=2, font=("Comic Sans MS", 12), bg='#DAC7FF', selectcolor='#F9C6DE', activebackground='#F9C6DE', highlightcolor='#F9C6DE')
        option2.place(x=900, y=525)

        ############QUESTION5##############
        sentence5 = f'question number 5 : What is the singular noun of {random_noun}?'
        q5 = Button(c, text="play audio", command=lambda: tts(sentence5))
        q5.place(x=1225, y=585, height=35, width=80)
        c.create_text(965, 600, text=f'What is the singular noun of {random_noun}?', font=("Comic Sans MS", 15))
        enter_question5 = Entry(c)
        enter_question5.place(x=850, y=650, height=40, width=300)
        p = inflect.engine()
        def pop_up():
            """
            to view the game's result
            """

            global score
            user_input_question1 = enter_question1.get()
            user_input_question2 = enter_question2.get()
            user_input_question3 = enter_question3.get()
            user_input_question4 = m.get()
            user_input_question5 = enter_question5.get()
            if spacy.explain(sp(user_input_question1.lower())[0].tag_) == 'verb, past tense' and user_input_question1 in \
                    paragraphs_list4[0]:
                score += 1
            if spacy.explain(
                    sp(user_input_question2.lower())[0].tag_) == 'pronoun, personal' and user_input_question2 in \
                    paragraphs_list4[0]:
                score += 1
            if user_input_question3 in synonyms_list:
                score += 1
            if user_input_question4 == 1:
                score += 1
            if user_input_question5 == p.singular_noun(random_noun):
                score += 1
            messagebox.showinfo('Result', f'Your score is {str(score)}. Thanks for playing.')
            enter_question1.delete(0, 'end')
            enter_question2.delete(0, 'end')
            enter_question3.delete(0, 'end')
            enter_question5.delete(0, 'end')
            score = 0
        """
        submit button
        """
        submit = Button(self, bg='#3f51b5', font='bold', text="Submit", command=pop_up)
        submit.place(x=925, y=725, height=45, width=150)
        """
        home page button
        """
        home = Button(c, bg='#3f51b5', font='bold', text="Home Page", command=lambda: controller.show_frame(home_page))
        home.place(x=283, y=725, height=45, width=150)






class song_page(Frame):
    """
    a class to view a set of songs with the ability to pause and stop
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        c = Canvas(self)
        pygame.mixer.init()
        def play(song):
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(-1)

        def pause():
            pygame.mixer.music.pause()
            button_pause = ImageTk.PhotoImage(Image.open('..\\images\\play.png').resize((70, 70), Image.ANTIALIAS))
            b_pause = Button(c, image=button_pause, command=lambda: unpause(), bg='#abd4f6', bd=0)
            b_pause.place(x=650, y=650)
            b_pause.background = button_pause

        def stop():
            pygame.mixer.music.stop()

        def unpause():
            pygame.mixer.music.unpause()
            button_unpause = ImageTk.PhotoImage(Image.open('..\\images\\pause.png').resize((70, 70), Image.ANTIALIAS))
            b_unpause = Button(c, image=button_unpause, command=lambda: pause(), bg='#abd4f6', bd=0)
            b_unpause.place(x=650, y=650)
            b_unpause.background = button_unpause

        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\songs_back.png').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        c.create_image(0, 0, anchor=NW, image=img)

        button1 = ImageTk.PhotoImage(Image.open('..\\images\\1.png').resize((200, 200), Image.ANTIALIAS))
        first_song = Button(c, image=button1, command=lambda: play('..\\songs\\1_In_His_Hands.mp3'))
        first_song.place(x=20, y=340)
        first_song.background = button1

        button2 = ImageTk.PhotoImage(Image.open('..\\images\\2.png').resize((200, 200), Image.ANTIALIAS))
        secound_song = Button(c, image=button2, command=lambda: play('..\\songs\\2_Good_Morning.mp3'))
        secound_song.place(x=250, y=560)
        secound_song.background = button2

        button3 = ImageTk.PhotoImage(Image.open('..\\images\\4.png').resize((200, 200), Image.ANTIALIAS))
        third_song = Button(c, image=button3, command=lambda: play('..\\songs\\8_Friends.mp3'))
        third_song.place(x=480, y=340)
        third_song.background = button3

        button4 = ImageTk.PhotoImage(Image.open('..\\images\\3.png').resize((200, 200), Image.ANTIALIAS))
        forth_song = Button(c, image=button4, command=lambda: play('..\\songs\\3_Body_Parts.mp3'))
        forth_song.place(x=250, y=340)
        forth_song.background = button4

        button5 = ImageTk.PhotoImage(Image.open('..\\images\\7.png').resize((200, 200), Image.ANTIALIAS))
        fifth_song = Button(c, image=button5, command=lambda: play('..\\songs\\5_Funny_Long_Song.mp3'))
        fifth_song.place(x=250, y=110)
        fifth_song.background = button5

        button6 = ImageTk.PhotoImage(Image.open('..\\images\\6.png').resize((200, 200), Image.ANTIALIAS))
        sixth_song = Button(c, image=button6, command=lambda: play('..\\songs\\6_Sing_for_Me.mp3'))
        sixth_song.place(x=840, y=340)
        sixth_song.background = button6

        button7 = ImageTk.PhotoImage(Image.open('..\\images\\8.png').resize((200, 200), Image.ANTIALIAS))
        seventh_song = Button(c, image=button7, command=lambda: play('..\\songs\\7_Ready_to_Get_Washed.mp3'))
        seventh_song.place(x=1070, y=340)
        seventh_song.background = button7

        button8 = ImageTk.PhotoImage(Image.open('..\\images\\9.png').resize((200, 200), Image.ANTIALIAS))
        eighth_song = Button(c, image=button8, command=lambda: play('..\\songs\\bluebird-through-my-window.mp3'))
        eighth_song.place(x=1070, y=560)
        eighth_song.background = button8

        button9 = ImageTk.PhotoImage(Image.open('..\\images\\10.png').resize((200, 200), Image.ANTIALIAS))
        ninth_song = Button(c, image=button9, command=lambda: play('..\\songs\\dancing-rainbow-colors.mp3'))
        ninth_song.place(x=1300, y=340)
        ninth_song.background = button9

        button10 = ImageTk.PhotoImage(Image.open('..\\images\\5.png').resize((200, 200), Image.ANTIALIAS))
        tenth_song = Button(c, image=button10, command=lambda: play('..\\songs\\4_Clap_Your_Hands.mp3'))
        tenth_song.place(x=1070, y=110)
        tenth_song.background = button10

        buttonstop = ImageTk.PhotoImage(Image.open('..\\images\\stop.png').resize((70, 70), Image.ANTIALIAS))
        b_stop = Button(c, image=buttonstop, command=lambda: stop(), bg='#abd4f6', bd=0)
        b_stop.place(x=820, y=650)
        b_stop.background = buttonstop


        button_unpause = ImageTk.PhotoImage(Image.open('..\\images\\pause.png').resize((70, 70), Image.ANTIALIAS))
        b_unpause = Button(c, image=button_unpause, command=lambda: pause(), bg='#abd4f6', bd=0)
        b_unpause.place(x=650, y=650)
        b_unpause.background = button_unpause

        home = Button(c, text="Home Page", height=2, width=10, bg='#3085D1', command=lambda: controller.show_frame(home_page) , font = ' bold')
        home.place(x=20, y=650)


if __name__ == '__main__':
    root = Little()
    root.title('Little Kiddie')
    root.mainloop()
    # TKINTER SOURCE CODE: https://www.youtube.com/watch?v=39P4BMvvLdM&ab_channel=IntrotoComputerScience
