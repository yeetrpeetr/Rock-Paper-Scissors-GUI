from tkinter import *
import random
computer = ['ROCK', 'PAPER', 'SCISSORS']


class RPS:
    def __init__(self, window ):
        window.geometry('500x300'); window.title('RPS'); window.resizable(0,0); window.configure(background='#CBC3E3')
        Rock = Button(window, background='white',  text = 'Rock',  width = 10, font = ('Times', 10), command = self.rock)
        Paper = Button(window, background='white', text = 'Paper',  width = 10,font = ('Times', 10), command = self.paper)
        Scissors = Button(window, background='white', text = 'Scissors',  width = 10, font = ('Times', 10), command = self.scissors)
        Reset = Button(window, background='white', text = 'Reset',  width = 10, font = ('Times', 10), command = self.reset)
        text = Label(root, background='#CBC3E3', font = ('Times', 10), width=10, text='OPPONENT')
        opp = Label(root, background='white', font = ('Times', 10), width=10, text='Waiting')

        text.place(x=200,y=175)
        opp.place(x=200,y=200)
        Rock.place(x=100,y=20);Paper.place(x=200,y=20);Scissors.place(x=300,y=20)
        Reset.place(x=200,y=100)

        self.is_rock = False
        self.is_paper = False
        self.is_scissors = False
        self.cont = True
 
    def rock(self):
        while self.cont:
            if not self.is_paper and not self.is_scissors:
                self.is_rock = True
            if not self.is_paper and not self.is_scissors and not self.is_rock:
                        opp = Label(root, background='white', font = ('Times', 10), width=10, text='Waiting')
                        opp.pack()
                        opp.place(x=200,y=200)
            else:
                opp = Label(root, background='white', font = ('Times', 10), width=10, text=random.choice(computer))
                opp.pack()
                opp.place(x=200,y=200)
            self.cont = False
 
    def paper(self):
        while self.cont:
            if not self.is_rock and not self.is_scissors:
                self.is_paper = True
            if not self.is_paper and not self.is_scissors and not self.is_rock:
                        opp = Label(root, background='white', font = ('Times', 10), width=10, text='Waiting')
                        opp.pack()
                        opp.place(x=200,y=200)
            else:
                opp = Label(root, background='white', font = ('Times', 10), width=10, text=random.choice(computer))
                opp.pack()
                opp.place(x=200,y=200)
            self.cont = False
 
    def scissors(self):
        while self.cont:
            if not self.is_rock and not self.is_paper:
                self.is_scissors = True
            if not self.is_paper and not self.is_scissors and not self.is_rock:
                        opp = Label(root, background='white', font = ('Times', 10), width=10, text='Waiting')
                        opp.pack()
                        opp.place(x=200,y=200)
            else:
                opp = Label(root, background='white', font = ('Times', 10), width=10, text=random.choice(computer))
                opp.pack()
                opp.place(x=200,y=200)
            self.cont = False

    def reset(self):
        if self.is_rock or self.is_paper or self.is_scissors:
            self.is_rock = False
            self.is_paper = False
            self.is_scissors = False
        if not self.is_paper and not self.is_scissors and not self.is_rock:
            opp = Label(root, background='white', font = ('Times', 10), width=10, text='Waiting')
            opp.pack()
            opp.place(x=200,y=200)
            self.cont = True
        
root = Tk()
app = RPS(root)
root.mainloop()