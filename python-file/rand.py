from tkinter import *
import json
import random
import spacy
import vlc
from tkinter import messagebox
from PyDictionary import PyDictionary
import inflect
import string
import pyttsx3
from PIL import Image,ImageTk
import  requests
from io import BytesIO
dictionary=PyDictionary()
sp = spacy.load('en_core_web_sm')


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

        # self.minsize(640,400)
        for i in (home_page, story_page1,story_page2,story_page3,story_page4 ,guessing_game1,guessing_game2,guessing_game3,guessing_game4, song_page):
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(home_page)

        # canvas = Canvas( Tk, width=300, height=300)
        # canvas.pack()
        #
        # img = PhotoImage(file="..\\images\\hi.jpg")
        # canvas.create_image(20, 20, anchor=NW, image=img)
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
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\v.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img  # Keep a reference in case this code is put in a function.
        bg = c.create_image(0, 0, anchor=NW, image=img)
        c.create_text(870, 160, text='Welcome to LittleKiddie', font=("Comic Sans MS", 30))


        # title = Label(self, text="Welcome to littleKiddie")
        # title.pack(padx=10, pady=10)
        # pick = Label(self, text="To view a story, choose from our categories:")
        # pick.pack(padx=10, pady=10)
        c.create_text(320, 480, text="Best Stories", font=("Comic Sans MS", 20))

        img_button = ImageTk.PhotoImage(
            Image.open('..\\images\\top-10-set-label-vector.jpg').resize((250, 250), Image.ANTIALIAS))
        first_category = Button(c, image=img_button, command=lambda: controller.show_frame(story_page1))
        first_category.place(x=200, y=200)
        first_category.background = img_button

        # first_category = Button(c, text="Collection of our Best", command=lambda: controller.show_frame(story_page1))
        # first_category.pack()

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
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\hi.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img
        bg = c.create_image(0, 0, anchor=NW, image=img)

        with open('../json/top10.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            data3 = data[random_index]['image']
            c.create_text(420, 200, text=data[random_index]['title'], font=("Comic Sans MS", 20))
            # c = Canvas(self)
            # response = requests.get(data3)
            # c.pack(fill=BOTH, anchor='nw', expand=True)
            # img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)).resize((200, 100), Image.ANTIALIAS))
            # c.background = img  # Keep a reference in case this code is put in a function.
            # bg = c.create_image(0, 0, anchor=NW, image=img)
            data2 = data[random_index]['pargraph']

            S = Scrollbar(c)
            T = Text(c, height=20, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
            S.pack(side=RIGHT, fill=Y)
            T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
            T.tag_configure('big', font=('Verdana', 20, 'bold'))
            T.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))
            T.place(x = 850, y = 140)
            T.insert(END, data2)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set)



            paragraphs_list1.insert(0,data[random_index]['pargraph'])
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(c, text="play audio", height=3, width=15,bg='#5bc6c9' ,command=p.play)
            audio.place(x = 220, y = 500)
            audio = Button(c, text="stop audio",height=3, width=15,bg='#5bc6c9' , command=p.stop)
            audio.place(x = 340, y = 500)



        home = Button(c, text="Home Page", height=3, width=15 ,bg='#5bc6c9' ,command=lambda: controller.show_frame(home_page))
        home.place(x = 460, y = 500)
        game = Button(c, text="Guessing Game",height=3, width=15,bg='#5bc6c9' , command=lambda: controller.show_frame(guessing_game1))
        game.place(x = 580, y = 500)


class story_page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\hi.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img  # Keep a reference in case this code is put in a function.
        bg = c.create_image(0, 0, anchor=NW, image=img)

        with open('../json/funny.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            # title = Label(c ,text = data[random_index]['title'])
            # title.pack()
            data3 = data[random_index]['image']
            # c.create_text(420, 200, text=data[random_index]['title'], font=("Comic Sans MS", 20))
            # c = Canvas(self)
            # response = requests.get(data3)
            # c.pack(fill=BOTH, anchor='nw', expand=True)
            # img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)).resize((200, 100), Image.ANTIALIAS))
            # c.background = img  # Keep a reference in case this code is put in a function.
            # bg = c.create_image(0, 0, anchor=NW, image=img)
            data2 = data[random_index]['pargraph']

            S = Scrollbar(self)
            T = Text(self, height=20, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
            S.pack(side=RIGHT, fill=Y)
            T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
            T.tag_configure('big', font=('Verdana', 20, 'bold'))
            T.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))
            T.place(x=850, y=140)
            T.insert(END, data2)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set)

            paragraphs_list2.insert(0, data[random_index]['pargraph'])
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(self, text="play audio", height=3, width=15, bg='#5bc6c9', command=p.play)
            audio.place(x=220, y=500)
            audio = Button(self, text="stop audio", height=3, width=15, bg='#5bc6c9', command=p.stop)
            audio.place(x=340, y=500)

        home = Button(self, text="Home Page", height=3, width=15, bg='#5bc6c9',
                      command=lambda: controller.show_frame(home_page))
        home.place(x=460, y=500)
        game = Button(self, text="Guessing Game", height=3, width=15, bg='#5bc6c9',
                      command=lambda: controller.show_frame(guessing_game1))
        game.place(x=580, y=500)

class story_page3(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\hi.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img  # Keep a reference in case this code is put in a function.
        bg = c.create_image(0, 0, anchor=NW, image=img)

        with open('../json/magic.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            # title = Label(c ,text = data[random_index]['title'])
            # title.pack()
            data3 = data[random_index]['image']
            c.create_text(420, 200, text=data[random_index]['title'], font=("Comic Sans MS", 20))
            # c = Canvas(self)
            # response = requests.get(data3)
            # c.pack(fill=BOTH, anchor='nw', expand=True)
            # img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)).resize((200, 100), Image.ANTIALIAS))
            # c.background = img  # Keep a reference in case this code is put in a function.
            # bg = c.create_image(0, 0, anchor=NW, image=img)
            data2 = data[random_index]['pargraph']

            S = Scrollbar(c)
            T = Text(c, height=20, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
            S.pack(side=RIGHT, fill=Y)
            T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
            T.tag_configure('big', font=('Verdana', 20, 'bold'))
            T.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))
            T.place(x=850, y=140)
            T.insert(END, data2)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set)

            paragraphs_list3.insert(0, data[random_index]['pargraph'])
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(c, text="play audio", height=3, width=15, bg='#5bc6c9', command=p.play)
            audio.place(x=220, y=500)
            audio = Button(c, text="stop audio", height=3, width=15, bg='#5bc6c9', command=p.stop)
            audio.place(x=340, y=500)

        home = Button(c, text="Home Page", height=3, width=15, bg='#5bc6c9',
                      command=lambda: controller.show_frame(home_page))
        home.place(x=460, y=500)
        game = Button(c, text="Guessing Game", height=3, width=15, bg='#5bc6c9',
                      command=lambda: controller.show_frame(guessing_game1))
        game.place(x=580, y=500)

class story_page4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        c = Canvas(self)
        c.pack(fill=BOTH, anchor='nw', expand=True)
        img = ImageTk.PhotoImage(Image.open('..\\images\\hi.jpg').resize((1540, 800), Image.ANTIALIAS))
        c.background = img  # Keep a reference in case this code is put in a function.
        bg = c.create_image(0, 0, anchor=NW, image=img)

        with open('../json/big_concept.json') as fp:
            data = json.load(fp)
            random_index = random.randint(0, len(data) - 1)
            # title = Label(c ,text = data[random_index]['title'])
            # title.pack()
            data3 = data[random_index]['image']
            c.create_text(420, 200, text=data[random_index]['title'], font=("Comic Sans MS", 20))
            # c = Canvas(self)
            # response = requests.get(data3)
            # c.pack(fill=BOTH, anchor='nw', expand=True)
            # img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)).resize((200, 100), Image.ANTIALIAS))
            # c.background = img  # Keep a reference in case this code is put in a function.
            # bg = c.create_image(0, 0, anchor=NW, image=img)
            data2 = data[random_index]['pargraph']

            S = Scrollbar(c)
            T = Text(c, height=20, width=50, wrap=WORD, padx=(10), pady=(10), font=('Arial', 12, 'bold'))
            S.pack(side=RIGHT, fill=Y)
            T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
            T.tag_configure('big', font=('Verdana', 20, 'bold'))
            T.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))
            T.place(x=850, y=140)
            T.insert(END, data2)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set)

            paragraphs_list4.insert(0, data[random_index]['pargraph'])
            p = vlc.MediaPlayer(data[random_index]['audio'])
            audio = Button(c, text="play audio", height=3, width=15, bg='#5bc6c9', command=p.play)
            audio.place(x=220, y=500)
            audio = Button(c, text="stop audio", height=3, width=15, bg='#5bc6c9', command=p.stop)
            audio.place(x=340, y=500)

        home = Button(c, text="Home Page", height=3, width=15, bg='#5bc6c9',
                      command=lambda: controller.show_frame(home_page))
        home.place(x=460, y=500)
        game = Button(c, text="Guessing Game", height=3, width=15, bg='#5bc6c9',
                      command=lambda: controller.show_frame(guessing_game1))
        game.place(x=580, y=500)
def tts(sentence):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    engine.setProperty('rate', 130)
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)
    engine.say(sentence)
    engine.runAndWait()


class guessing_game1(Frame):
    """
    a class to view the game page.
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        adjectives = []
        nouns = []
        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        story_in_game = Label(self, text= paragraphs_list1[0])
        story_in_game.pack()
        for i in paragraphs_list1[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'adjective':
                adjectives.append(i)
        random_adjective = random.choice(adjectives).translate(str.maketrans('', '', string.punctuation))

        random_adjective2 = random.choice(adjectives)

        for i in paragraphs_list1[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'noun, plural':
                nouns.append(i)
        random_noun = random.choice(nouns).translate(str.maketrans('', '', string.punctuation))


########
        global score
        score = 0
        ###########QUESTION1##############
        sentence1 = ' question number 1 : Enter a past tense verb from the above story'
        q1 = Button(self, text="play audio", command=lambda: tts(sentence1))
        q1.pack()
        question1=Label(self,text= 'Q1: Enter a past tense verb from the above story')
        question1.pack()
        enter_question1 = Entry(self)
        enter_question1.pack()
        ###########QUESTION2##############
        sentence2 = 'question number 2 : Enter a personal pronoun from the above story'
        q2 = Button(self, text="play audio", command=lambda: tts(sentence2))
        q2.pack()
        question2 = Label(self, text='Q2: Enter a personal pronoun from the above story')
        question2.pack()
        enter_question2 = Entry(self)
        enter_question2.pack()
        ###########QUESTION3##############
        sentence3 = f'question number 3 : What is the meaning of {random_adjective}?'
        q3 = Button(self, text="play audio", command=lambda: tts(sentence3))
        q3.pack()
        question3 = Label(self, text=f'Q3: What is the meaning of {random_adjective}?')
        question3.pack()
        enter_question3 = Entry(self)
        enter_question3.pack()
        synonyms_list=dictionary.synonym(random_adjective)
        random_synonym= random.choice(synonyms_list)
        ###########QUESTION4##############
        sentence4 = f'question number 4 : What is the opposite of {random_adjective2}?'
        q4 = Button(self, text="play audio", command=lambda: tts(sentence4))
        q4.pack()
        question4 = Label(self, text=f'Q4: What is the opposite of {random_adjective2}?')
        question4.pack()
        antonym_list=dictionary.antonym(random_adjective2)
        random_antonym = random.choice(antonym_list).translate(str.maketrans('', '', string.punctuation))
        m = IntVar()
        option1 = Radiobutton(self, text=f'(a){random_antonym}', variable= m, value= 1)
        option1.pack()
        option2 = Radiobutton(self, text=f'(b){random_synonym}', variable= m, value= 2)
        option2.pack()

        ############QUESTION5##############
        sentence5 = f'question number 5 : What is the singular noun of {random_noun}?'
        q5 = Button(self, text="play audio", command=lambda: tts(sentence5))
        q5.pack()
        question5 = Label(self, text=f'Q3: What is the singular noun of {random_noun}?')
        question5.pack()
        enter_question5 = Entry(self)
        enter_question5.pack()
        # noun_list=dictionary.singular(random_adjective2)
        # random_antonym = random.choice(antonym_list)
        p = inflect.engine()

        def pop_up():
            global score
            user_input_question1 = enter_question1.get()
            user_input_question2 = enter_question2.get()
            user_input_question3 = enter_question3.get()
            user_input_question4 = m.get()
            user_input_question5 = enter_question5.get()
            if spacy.explain(sp(user_input_question1.lower())[0].tag_)== 'verb, past tense' and user_input_question1 in paragraphs_list1[0]:
                print('hi')
                score += 1
            else:
                print('wrong1')
            if spacy.explain(sp(user_input_question2.lower())[0].tag_)== 'pronoun, personal' and user_input_question2 in paragraphs_list1[0]:
                print('hello')
                score += 1
            else:
                print('wrong2')
            if user_input_question3 in synonyms_list :
                score += 1
            else:
                print('wrong3')
            if user_input_question4 ==  1 :
                score += 1
            else:
                print('wrong4')
            if user_input_question5 == p.singular_noun(random_noun):
                score += 1
            else:
                print('wrong5')
            messagebox.showinfo('Result',f'Your score is {str(score)}. Thanks for playing.')
        submit = Button(self, text="Submit", command=pop_up)
        submit.pack()
class guessing_game2(Frame):
    """
    a class to view the game page.
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        adjectives = []
        nouns = []
        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        story_in_game = Label(self, text=paragraphs_list2[0])
        story_in_game.pack()
        for i in paragraphs_list2[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'adjective':
                adjectives.append(i)
        random_adjective = random.choice(adjectives).translate(str.maketrans('', '', string.punctuation))

        random_adjective2 = random.choice(adjectives)

        for i in paragraphs_list2[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'noun, plural':
                nouns.append(i)
        random_noun = random.choice(nouns).translate(str.maketrans('', '', string.punctuation))

        ########
        global score
        score = 0
        ###########QUESTION1##############
        sentence1 = ' question number 1 : Enter a past tense verb from the above story'
        q1 = Button(self, text="play audio", command=lambda: tts(sentence1))
        q1.pack()
        question1 = Label(self, text=' Enter a past tense verb from the above story')
        question1.pack()
        enter_question1 = Entry(self)
        enter_question1.pack()
        ###########QUESTION2##############
        sentence2 = 'question number 2 : Enter a personal pronoun from the above story'
        q2 = Button(self, text="play audio", command=lambda: tts(sentence2))
        q2.pack()
        question2 = Label(self, text=' Enter a personal pronoun from the above story')
        question2.pack()
        enter_question2 = Entry(self)
        enter_question2.pack()
        ###########QUESTION3##############
        sentence3 = f'question number 3 : What is the meaning of {random_adjective}?'
        q3 = Button(self, text="play audio", command=lambda: tts(sentence3))
        q3.pack()
        question3 = Label(self, text=f' What is the meaning of {random_adjective}?')
        question3.pack()
        enter_question3 = Entry(self)
        enter_question3.pack()
        synonyms_list = dictionary.synonym(random_adjective)
        random_synonym = random.choice(synonyms_list)
        ###########QUESTION4##############
        sentence4 = f'question number 4 : What is the opposite of {random_adjective2}?'
        q4 = Button(self, text="play audio", command=lambda: tts(sentence4))
        q4.pack()
        question4 = Label(self, text=f' What is the opposite of {random_adjective2}?')
        question4.pack()
        antonym_list = dictionary.antonym(random_adjective2)
        random_antonym = random.choice(antonym_list).translate(str.maketrans('', '', string.punctuation))
        m = IntVar()
        option1 = Radiobutton(self, text=f'(a){random_antonym}', variable=m, value=1)
        option1.pack()
        option2 = Radiobutton(self, text=f'(b){random_synonym}', variable=m, value=2)
        option2.pack()

        ############QUESTION5##############
        sentence5 = f'question number 5 : What is the singular noun of {random_noun}?'
        q5 = Button(self, text="play audio", command=lambda: tts(sentence5))
        q5.pack()
        question5 = Label(self, text=f'Q3: What is the singular noun of {random_noun}?')
        question5.pack()
        enter_question5 = Entry(self)
        enter_question5.pack()
        # noun_list=dictionary.singular(random_adjective2)
        # random_antonym = random.choice(antonym_list)
        p = inflect.engine()

        def pop_up():
            global score
            user_input_question1 = enter_question1.get()
            user_input_question2 = enter_question2.get()
            user_input_question3 = enter_question3.get()
            user_input_question4 = m.get()
            user_input_question5 = enter_question5.get()
            if spacy.explain(sp(user_input_question1.lower())[0].tag_) == 'verb, past tense' and user_input_question1 in \
                    paragraphs_list2[0]:
                print('hi')
                score += 1
            else:
                print('wrong1')
            if spacy.explain(
                    sp(user_input_question2.lower())[0].tag_) == 'pronoun, personal' and user_input_question2 in \
                    paragraphs_list2[0]:
                print('hello')
                score += 1
            else:
                print('wrong2')
            if user_input_question3 in synonyms_list:
                score += 1
            else:
                print('wrong3')
            if user_input_question4 == 1:
                score += 1
            else:
                print('wrong4')
            if user_input_question5 == p.singular_noun(random_noun):
                score += 1
            else:
                print('wrong5')
            messagebox.showinfo('Result', f'Your score is {str(score)}. Thanks for playing.')

        submit = Button(self, text="Submit", command=pop_up)
        submit.pack()

class guessing_game3(Frame):
    """
    a class to view the game page.
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        adjectives = []
        nouns = []
        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        story_in_game = Label(self, text=paragraphs_list3[0])
        story_in_game.pack()
        for i in paragraphs_list3[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'adjective':
                adjectives.append(i)
        random_adjective = random.choice(adjectives).translate(str.maketrans('', '', string.punctuation))

        random_adjective2 = random.choice(adjectives)

        for i in paragraphs_list3[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'noun, plural':
                nouns.append(i)
        random_noun = random.choice(nouns).translate(str.maketrans('', '', string.punctuation))

        ########
        global score
        score = 0
        ###########QUESTION1##############
        sentence1 = ' question number 1 : Enter a past tense verb from the above story'
        q1 = Button(self, text="play audio", command=lambda: tts(sentence1))
        q1.pack()
        question1 = Label(self, text='Enter a past tense verb from the above story')
        question1.pack()
        enter_question1 = Entry(self)
        enter_question1.pack()
        ###########QUESTION2##############
        sentence2 = 'question number 2 : Enter a personal pronoun from the above story'
        q2 = Button(self, text="play audio", command=lambda: tts(sentence2))
        q2.pack()
        question2 = Label(self, text='Enter a personal pronoun from the above story')
        question2.pack()
        enter_question2 = Entry(self)
        enter_question2.pack()
        ###########QUESTION3##############
        sentence3 = f'question number 3 : What is the meaning of {random_adjective}?'
        q3 = Button(self, text="play audio", command=lambda: tts(sentence3))
        q3.pack()
        question3 = Label(self, text=f'What is the meaning of {random_adjective}?')
        question3.pack()
        enter_question3 = Entry(self)
        enter_question3.pack()
        synonyms_list = dictionary.synonym(random_adjective)
        random_synonym = random.choice(synonyms_list)
        ###########QUESTION4##############
        sentence4 = f'question number 4 : What is the opposite of {random_adjective2}?'
        q4 = Button(self, text="play audio", command=lambda: tts(sentence4))
        q4.pack()
        question4 = Label(self, text=f'What is the opposite of {random_adjective2}?')
        question4.pack()
        antonym_list = dictionary.antonym(random_adjective2)
        random_antonym = random.choice(antonym_list).translate(str.maketrans('', '', string.punctuation))
        m = IntVar()
        option1 = Radiobutton(self, text=f'(a){random_antonym}', variable=m, value=1)
        option1.pack()
        option2 = Radiobutton(self, text=f'(b){random_synonym}', variable=m, value=2)
        option2.pack()

        ############QUESTION5##############
        sentence5 = f'question number 5 : What is the singular noun of {random_noun}?'
        q5 = Button(self, text="play audio", command=lambda: tts(sentence5))
        q5.pack()
        question5 = Label(self, text=f' What is the singular noun of {random_noun}?')
        question5.pack()
        enter_question5 = Entry(self)
        enter_question5.pack()
        # noun_list=dictionary.singular(random_adjective2)
        # random_antonym = random.choice(antonym_list)
        p = inflect.engine()

        def pop_up():
            global score
            user_input_question1 = enter_question1.get()
            user_input_question2 = enter_question2.get()
            user_input_question3 = enter_question3.get()
            user_input_question4 = m.get()
            user_input_question5 = enter_question5.get()
            if spacy.explain(sp(user_input_question1.lower())[0].tag_) == 'verb, past tense' and user_input_question1 in paragraphs_list3[0]:
                print('hi')
                score += 1
            else:
                print('wrong1')
            if spacy.explain(sp(user_input_question2.lower())[0].tag_) == 'pronoun, personal' and user_input_question2 in paragraphs_list3[0]:
                print('hello')
                score += 1
            else:
                print('wrong2')
            if user_input_question3 in synonyms_list:
                score += 1
            else:
                print('wrong3')
            if user_input_question4 == 1:
                score += 1
            else:
                print('wrong4')
            if user_input_question5 == p.singular_noun(random_noun):
                score += 1
            else:
                print('wrong5')
            messagebox.showinfo('Result', f'Your score is {str(score)}. Thanks for playing.')

        submit = Button(self, text="Submit", command=pop_up)
        submit.pack()

class guessing_game4(Frame):
    """
    a class to view the game page.
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        adjectives = []
        nouns = []
        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        home = Button(self, text="Go to the home page", command=lambda: controller.show_frame(home_page))
        home.pack()
        story_in_game = Label(self, text=paragraphs_list4[0])
        story_in_game.pack()
        for i in paragraphs_list4[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'adjective':
                adjectives.append(i)
        random_adjective = random.choice(adjectives).translate(str.maketrans('', '', string.punctuation))

        random_adjective2 = random.choice(adjectives)

        for i in paragraphs_list4[0].split():
            if spacy.explain(sp(i.lower())[0].tag_) == 'noun, plural':
                nouns.append(i)
        random_noun = random.choice(nouns).translate(str.maketrans('', '', string.punctuation))

        ########
        global score
        score = 0
        ###########QUESTION1##############
        sentence1 = ' question number 1 : Enter a past tense verb from the above story'
        q1 = Button(self, text="play audio", command=lambda: tts(sentence1))
        q1.pack()
        question1 = Label(self, text='Enter a past tense verb from the above story')
        question1.pack()
        enter_question1 = Entry(self)
        enter_question1.pack()
        ###########QUESTION2##############
        sentence2 = 'question number 2 : Enter a personal pronoun from the above story'
        q2 = Button(self, text="play audio", command=lambda: tts(sentence2))
        q2.pack()
        question2 = Label(self, text='Enter a personal pronoun from the above story')
        question2.pack()
        enter_question2 = Entry(self)
        enter_question2.pack()
        ###########QUESTION3##############
        sentence3 = f'question number 3 : What is the meaning of {random_adjective}?'
        q3 = Button(self, text="play audio", command=lambda: tts(sentence3))
        q3.pack()
        question3 = Label(self, text=f'What is the meaning of {random_adjective}?')
        question3.pack()
        enter_question3 = Entry(self)
        enter_question3.pack()
        synonyms_list = dictionary.synonym(random_adjective)
        random_synonym = random.choice(synonyms_list)
        ###########QUESTION4##############
        sentence4 = f'question number 4 : What is the opposite of {random_adjective2}?'
        q4 = Button(self, text="play audio", command=lambda: tts(sentence4))
        q4.pack()
        question4 = Label(self, text=f'What is the opposite of {random_adjective2}?')
        question4.pack()
        antonym_list = dictionary.antonym(random_adjective2)
        random_antonym = random.choice(antonym_list).translate(str.maketrans('', '', string.punctuation))
        m = IntVar()
        option1 = Radiobutton(self, text=f'(a){random_antonym}', variable=m, value=1)
        option1.pack()
        option2 = Radiobutton(self, text=f'(b){random_synonym}', variable=m, value=2)
        option2.pack()

        ############QUESTION5##############
        sentence5 = f'question number 5 : What is the singular noun of {random_noun}?'
        q5 = Button(self, text="play audio", command=lambda: tts(sentence5))
        q5.pack()
        question5 = Label(self, text=f'What is the singular noun of {random_noun}?')
        question5.pack()
        enter_question5 = Entry(self)
        enter_question5.pack()
        # noun_list=dictionary.singular(random_adjective2)
        # random_antonym = random.choice(antonym_list)
        p = inflect.engine()

        def pop_up():
            global score
            user_input_question1 = enter_question1.get()
            user_input_question2 = enter_question2.get()
            user_input_question3 = enter_question3.get()
            user_input_question4 = m.get()
            user_input_question5 = enter_question5.get()
            if spacy.explain(sp(user_input_question1.lower())[0].tag_) == 'verb, past tense' and user_input_question1 in paragraphs_list4[0]:
                print('hi')
                score += 1
            else:
                print('wrong1')
            if spacy.explain(sp(user_input_question2.lower())[0].tag_) == 'pronoun, personal' and user_input_question2 in paragraphs_list4[0]:
                print('hello')
                score += 1
            else:
                print('wrong2')
            if user_input_question3 in synonyms_list:
                score += 1
            else:
                print('wrong3')
            if user_input_question4 == 1:
                score += 1
            else:
                print('wrong4')
            if user_input_question5 == p.singular_noun(random_noun):
                score += 1
            else:
                print('wrong5')
            messagebox.showinfo('Result', f'Your score is {str(score)}. Thanks for playing.')

        submit = Button(self, text="Submit", command=pop_up)
        submit.pack()
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