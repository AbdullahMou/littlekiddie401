from tkinter import *
import pygame
pygame.init()
root = Tk()
root.title('Piano')
root.geometry('1365x431')
root.configure(background = 'white')
abc = Frame(root,background = 'pink' )
abc.pack(side="top", fill="both", expand=True)
str1= StringVar()
def very_fast_fun(note):
    str1.set('C#')
    sound = pygame.mixer.Sound(note)
    sound.play()


##########################################
btnC = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nC',fg= 'black', bg = '#55CAD0',  command = lambda: very_fast_fun('..\\Music_Notes\\C.wav'))
btnC.place(x=0,y=0)
btnD = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nD',fg= 'black', bg = '#6ED2D1', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\D.wav'))
btnD.place(x=65,y=0)
btnE = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nE',fg= 'black', bg = '#AED7CA', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\E.wav'))
btnE.place(x=130,y=0)
btnF = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nF',fg= 'black', bg = '#C7DAC7', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\F.wav'))
btnF.place(x=195,y=0)
btnG = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nG',fg= 'black', bg = '#E7CCAD', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\G.wav'))
btnG.place(x=260,y=0)
btnA = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA',fg= 'black',  bg = '#E7CCB0', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\A.wav'))
btnA.place(x=325,y=0)
btnB = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nB',fg= 'black', bg = '#FACAAF', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\B.wav'))
btnB.place(x=390,y=0)
btnC1 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nC',fg= 'black',  bg = '#FEA780', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\C_Drum.wav'))
btnC1.place(x=455,y=0)
btnD1 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nD',fg= 'black', bg = '#FDA280', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\D_Drum.wav'))
btnD1.place(x=520,y=0)
btnE1 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nE',fg= 'black',  bg = '#FE9B83',  justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\E_Drum.wav'))
btnE1.place(x=585,y=0)
btnF1 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nF',fg= 'black', bg = '#FB8F7D', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\F_Drum.wav'))
btnF1.place(x=650,y=0)
#
btn12 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nG',fg= 'black',  bg = '#F47E7D', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\G_Drum.wav'))
btn12.place(x=715,y=0)
#
btn13 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA',fg= 'black',  bg = '#F27B7D', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\A_Drum.wav'))
btn13.place(x=780,y=0)
#
btn14 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nB',fg= 'black', bg = '#EF7D80', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\B_Drum.wav'))
btn14.place(x=845,y=0)
#
btn15 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nC',fg= 'black',  bg = '#D77679', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\C1.wav'))
btn15.place(x=910,y=0)
#
btn16 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nD',fg= 'black',  bg = '#EDA6A8', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\D1.wav'))
btn16.place(x=975,y=0)
#
btn17 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nE',fg= 'black',  bg = '#F2C39E', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\E1.wav'))
btn17.place(x=1040,y=0)
#
btn18 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nF',fg= 'black', bg = '#E2D2B7', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\F1.wav'))
btn18.place(x=1105,y=0)
#
btn19 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nG',fg= 'black', bg = '#A5D8CC', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\G.wav'))
btn19.place(x=1170,y=0)
#
btn20 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA',fg= 'black',  bg = '#76D6D4', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\A.wav'))
btn20.place(x=1235,y=0)
#
btn21 = Button(abc,height = 18,width=5,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nB',fg= 'black',  bg = '#56CBD1', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Bb.wav'))
btn21.place(x=1300,y=0)
####################################################################
btnCs = Button(abc,height = 10,width=4,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nC',fg= 'white',bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\C_s.wav'))
btnCs.place(x=36,y=0)

btnDs = Button(abc,height = 10,width=4,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nD',fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\D_s.wav'))
btnDs.place(x=102,y=0)

btnFs = Button(abc,height = 10,width=4,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nE',fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\F_s.wav'))
btnFs.place(x=232,y=0)

btnGs = Button(abc,height = 10,width=4,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nF',fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\G_s.wav'))
btnGs.place(x=298,y=0)

btnBb = Button(abc,height = 10,width=4,font=('arial') ,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nG',fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Bb.wav'))
btnBb.place(x=363,y=0)

btnCs1 = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\C1_Drum.wav'))
btnCs1.place(x=493,y=0)

btnDs1 = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white',bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\D1_Drum.wav'))
btnDs1.place(x=557,y=0)

btn8b = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\F1_Drum.wav'))
btn8b.place(x=686,y=0)

btn9b = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white',bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\Gq_Drum.wav'))
btn9b.place(x=752,y=0)

btn10b = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\A_Drum.wav'))
btn10b.place(x=818,y=0)

btn11b = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white',bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\C_s1.wav'))
btn11b.place(x=946,y=0)

btn12b = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white',bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\D_s1.wav'))
btn12b.place(x=1013,y=0)

btn13b = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\Fq_Drum.wav'))
btn13b.place(x=1142,y=0)

btn14b = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\Gq_Drum.wav'))
btn14b.place(x=1208,y=0)

btn15b = Button(abc,height = 10,width=4,font=('arial') ,fg= 'white', bg = 'black', justify=CENTER, command = lambda: very_fast_fun('..\\Music_Notes\\Steel_Drum\\A_Drum.wav'))
btn15b.place(x=1273,y=0)




if __name__ == '__main__':
    root.mainloop()