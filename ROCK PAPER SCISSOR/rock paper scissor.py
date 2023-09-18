# Import necessary modules from Tkinter
from tkinter import *
from tkinter import font
import random

# Initialize scores for player and computer
score1 = 0
score2 = 0

# Function to randomly select a move for the computer
def game():
    x = ['rock','paper','scissors']
    player1 = random.choice(x)
    return player1

# Function to display the final result and reset scores
def stop():
    global score1
    global score2
    display.delete(0,'end')
    option1.configure(text= score1)
    option2.configure(text = score2)
    if score1>score2:
        display.insert(0,"CONGRATULATIONS.YOU WON THE GAME!!!")
    elif score1<score2:
        display.insert(0,"SORRY.YOU LOST THE GAME!")
    elif score1 == score2:
        display.insert(0,"ITS A TIE")
    score1 = 0
    score2 = 0
            
# Function for the "Rock" button    
def rock():
    global score1
    global score2
    display.delete(0,'end')
    x=game()
    option1.configure(text= "rock")
    option2.configure(text = x)
    if x=="scissors":
        display.insert(0,"you win")
        score1+=1
    elif x=="paper":
        display.insert(0,"computer wins")
        score2+=1
    else:
        display.insert(0,"tie")
        
# Function for the "Paper" button        
def paper():
    global score1
    global score2
    display.delete(0,'end')
    x=game()
    option1.configure(text= "paper")
    option2.configure(text = x)
    if x=="rock":
        display.insert(0,"you win")
        score1+=1
    elif x=="scissors":
        display.insert(0,"computer wins")
        score2+=1
    else:
        display.insert(0,"tie")
        
# Function for the "Scissors" button   
def scissors():  
    global score1
    global score2   
    display.delete(0,'end')
    x=game()
    option1.configure(text= "scissors")
    option2.configure(text = x)
    if x=="paper":
        display.insert(0,"you win")
        score1+=1
    elif x=="rock":
        display.insert(0,"computer wins")
        score2+=1
    else:
        display.insert(0,"tie")
        
        
    
    
# Create the main window
window = Tk()

window.title("Rock Paper Scissor")

window.geometry("800x500")

window.configure(bg='antiquewhite')

# Define fonts
label_font = font.Font(size=24)
para_font = font.Font(size=20)

# Create labels and place them in the window
title = Label(window, text= "Welcome to the Rock Paper Scissors Game\n", font=label_font, fg='red' ,bg='antiquewhite',).place(x=160, y=60)
instructions = Label(window, text= "* Choose rock, paper, or scissors.\n * Click STOP to view the final result",font=para_font, fg='black' ,bg='antiquewhite',).place(x=200, y=125)
players = Label(window, text= "You         vs      Computer",font=para_font, fg='blue' ,bg='antiquewhite',).place(x=250, y=180)

# Labels for player and computer choices
option1 = Label(window, text= "R/P/S",fg='blue' ,bg='antiquewhite')
option1.place(x=250,y=220)
option2 = Label(window, text= "R/P/S",fg='blue' ,bg='antiquewhite')
option2.place(x=400,y=220)

# Entry widget to display game messages
display = Entry(window,bg="white",fg="red",width=30)
display.place(x=230, y=250)

# Buttons for player choices
rock = Button(window, width=10, height=2, text="ROCK",fg ="blue", command=rock).place(x=160,y=300)
paper = Button(window, width=10, height=2, text="PAPER",fg ="blue", command=paper).place(x=280,y=300)
scissor = Button(window, width=10, height=2, text="SCISSORS",fg ="blue", command=scissors).place(x=400,y=300)

# Button to stop the game and display the final result
stop = Button(window, width=10, height=2, text="STOP",fg ="red", command=stop).place(x=280,y=350)

# Start the Tkinter main loop
window.mainloop()
