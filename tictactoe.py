"""from tkinter import *
from tkinter import messagebox
import random as r
def button(frame):          #Function to define a button
    b=Button(frame,padx=1,bg="papaya whip",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b
def change_a():             #Function to change the operand for the next player
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
def reset():                #Resets the game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
def check():                #Checks for victory or Draw
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text=a+"'s Chance")
###############   Main Program #################
root=Tk()                   #Window defined
root.title("Tic-Tac-Toe")   #Title given
a=r.choice(['O','X'])       #Two operators defined
colour={'O':"deep sky blue",'X':"lawn green"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s Chance",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()"""
import tkinter
import tkinter.messagebox as tmsg

class mainApp(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.geometry('240x260')
        self.resizable(0,0)
        self.title('Tic Tac Toe')
        container = tkinter.Frame(self,width=240,height=260)
        container.pack(side='top',fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in {StartPage,tictactoe}:
            page_name = F.__name__
            frame = F(parent=container,controller=self) 
            self.frames[page_name] = frame
            frame.grid(row=0,column=0,sticky="NSEW")
        self.show_frame("StartPage")

    def playMode(self,mode):
        self.mode = 'Comp'

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tkinter.Frame):
    def __init__(self, parent,controller):
        tkinter.Frame.__init__(self,parent)
        self.controller = controller
        
        tkinter.Label(self,text='Tic Tac Toe').pack()
        tkinter.Button(self,text='With Player',command=lambda: self.controller.show_frame("tictactoe")).pack()
        tkinter.Button(self,text='With Computer').pack()

class tictactoe(tkinter.Frame):
    def __init__(self,parent,controller,mode=None):
        tkinter.Frame.__init__(self,parent)
        self.controller = controller
        self.button = [[],[],[]]
        self.chance = 'X'
        self.color = 'red'
        for r in range(3):
            for c in range(3):
                self.button[r].append(tkinter.Button(self,font='arial 30',relief='sunken',width=3,height=1))
                self.button[r][c].config(command= lambda row=r,column=c:self.click(row,column))
                self.button[r][c].grid(row=r,column=c)
        self.Label = tkinter.Label(self,text=f"{self.chance}'s chance",font='arial 15')
        self.Label.grid(row=3,column=0,columnspan=2)
        tkinter.Button(self,text='Go back',command=lambda : controller.show_frame("StartPage")).grid(row=3,column=2)

    def click(self,row,column):
        self.button[row][column].config(text=self.chance,fg='blue',state="disabled",disabledforeground=self.color)
        
        if self.chance == 'X':
            self.color = 'blue'          
            self.chance = 'O'
        else:
            self.color = 'red' 
            self.chance = 'X'
        self.Label.config(text=f"{self.chance}'s chance")
        self.check()
        if self.boardFull():
            tmsg.showinfo("Winner","Draw")
            self.reset()

    def boardFull(self):
        for r in range(3):
            for c in range(3):
                if self.button[r][c]['text'] == '':
                    return False
        return True

    def check(self):
        #rows
        for i in range(3):
            if self.button[i][0]['text'] == self.button[i][1]['text']==self.button[i][2]['text']!='':
                tmsg.showinfo("Winner",f"{self.button[i][0]['text']} Won")
                self.reset()
        
        #columns
        for i in range(3):
            if self.button[0][i]['text'] == self.button[1][i]['text']==self.button[2][i]['text']!='':
                tmsg.showinfo("Winner",f"{self.button[0][i]['text']} Won")
                self.reset()
        
        #diagonal
        if self.button[0][0]['text'] == self.button[1][1]['text']==self.button[2][2]['text']!='':
                tmsg.showinfo("Winner",f"{self.button[0][0]['text']} Won")
                self.reset()
        elif self.button[2][0]['text'] == self.button[1][1]['text']==self.button[0][2]['text']!='':
                tmsg.showinfo("Winner",f"{self.button[2][0]['text']} Won")
                self.reset()


    def reset(self):
        self.chance = 'X'
        self.color = 'red'
        for r in range(3):
            for c in range(3):
                self.button[r][c].config(state='active',text='')
        self.Label.config(text=f"{self.chance}'s chance")



if __name__ == "__main__":
    window = mainApp()
    # print(window.color)
    window.mainloop()