# Import necessary modules from the tkinter library.
from tkinter import *
from tkinter import font
from tkinter import messagebox

# Function to display the quiz result when the user submits the quiz.
def result():
    # Define global variables for question variables, answer options, and the submit button.
    global var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,submit

    # Initialize the user's score to zero.
    score = 0

    # Check each question's answer and update the score.
    if var1.get() == 2:
        score += 1
    if var2.get() == 2:
        score += 1
    if var3.get() == 4:
        score += 1
    if var4.get() == 4:
        score += 1
    if var5.get() == 3:
        score += 1
    if var6.get() == 1:
        score += 1
    if var7.get() == 1:
        score += 1
    if var8.get() == 3:
        score += 1
    if var9.get() == 3:
        score += 1
    if var10.get() == 1:
        score += 1

    # Configure the text color of the correct answer options to green.
    a1.configure(fg='green')
    a2.configure(fg='green')
    a3.configure(fg='green')
    a4.configure(fg='green')
    a5.configure(fg='green')
    a6.configure(fg='green')
    a7.configure(fg='green')
    a8.configure(fg='green')
    a9.configure(fg='green')
    a10.configure(fg='green')

    # Disable the submit button to prevent multiple submissions.
    submit['state'] = DISABLED

    # Determine the user's performance based on their score.
    if score <= 3:
        performance = "\nPerformance : Poor"
    elif score <= 5:
        performance = "\nPerformance : Below Average "
    elif score <= 7: 
        performance = "\nPerformance : Average"
    elif score <= 9:
        performance = "\nPerformance : Above Average"
    elif score == 10:
        performance = "\nPerformance : Excellent"
           
    # Display the quiz result using a message box.   
    final = "YOUR FINAL SCORE IS " +str(score)
    messagebox.showinfo(title="RESULT", message= final + performance )
    
    
# Function to set up and display the quiz questions.   
def quiz():
    # Define global variables for question variables, answer options, and the submit button.
    global var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,submit

    # Create IntVar variables to store user's answer choices for each question.
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
   
    
    # Question 1 setup
    q1 = Label(window, text ="1. What is the capital city of India?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q1.place(x=50,y=230)
    Radiobutton(window, text = "Mumbai",fg='brown4' ,bg='burlywood', variable = var1, value = 1).place(x=60,y=250)
    a1 = Radiobutton(window, text = "New Delhi",fg='brown4' ,bg='burlywood', variable = var1, value = 2)
    a1.place(x=210,y=250)
    Radiobutton(window, text = "Kolkata",fg='brown4' ,bg='burlywood', variable = var1, value = 3).place(x=360,y=250)
    Radiobutton(window, text = "Bangalore",fg='brown4' ,bg='burlywood', variable = var1, value = 4).place(x=510,y=250)
        
    # Question 2 setup    
    q2 = Label(window, text ="2. Which river is often referred to as the Ganga in India?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q2.place(x=50,y=270)
    Radiobutton(window, text = "Brahmaputra",fg='brown4' ,bg='burlywood', variable = var2, value = 1).place(x=60,y=290)
    a2 = Radiobutton(window, text = "Yamuna ",fg='brown4' ,bg='burlywood', variable = var2, value = 2)
    a2.place(x=210,y=290)
    Radiobutton(window, text = "Godavari",fg='brown4' ,bg='burlywood', variable = var2, value = 3).place(x=360,y=290)
    Radiobutton(window, text = "Indus",fg='brown4' ,bg='burlywood', variable = var2, value = 4).place(x=510,y=290)

    # Question 3 setup
    q3 = Label(window, text ="3. Who is considered the Father of the Nation in India for his role in the country's independence movement?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q3.place(x=50,y=310)
    Radiobutton(window, text = "Jawaharlal Nehru",fg='brown4' ,bg='burlywood', variable = var3, value = 1).place(x=60,y=330)
    Radiobutton(window, text = "Sardar Vallabhbhai Patel",fg='brown4' ,bg='burlywood', variable = var3, value = 2).place(x=210,y=330)
    Radiobutton(window, text = "Subhas Chandra Bose",fg='brown4' ,bg='burlywood', variable = var3, value = 3).place(x=410,y=330)
    a3 = Radiobutton(window, text = "Mahatma Gandhi",fg='brown4' ,bg='burlywood', variable = var3, value = 4)
    a3.place(x=600,y=330)

    # Question 4 setup
    q4 = Label(window, text ="4. Which famous monument in India is known as the Symbol of Love and is a UNESCO World Heritage site?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q4.place(x=50,y=350)
    Radiobutton(window, text = "Red Fort",fg='brown4' ,bg='burlywood', variable = var4, value = 1).place(x=60,y=370)
    Radiobutton(window, text = "Qutub Minar",fg='brown4' ,bg='burlywood', variable = var4, value = 2).place(x=210,y=370)
    Radiobutton(window, text = "Hawa Mahal",fg='brown4' ,bg='burlywood', variable = var4, value = 3).place(x=360,y=370)
    a4 = Radiobutton(window, text = "Taj Mahal ",fg='brown4' ,bg='burlywood', variable = var4, value = 4)
    a4.place(x=510,y=370)

    # Question 5 setup
    q5 = Label(window, text ="5. India is a federal union comprising how many states and union territories combined?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q5.place(x=50,y=390)
    Radiobutton(window, text = "25 states and 8 union territories",fg='brown4' ,bg='burlywood', variable = var5, value = 1).place(x=60,y=410)
    Radiobutton(window, text = "28 states and 7 union territories",fg='brown4' ,bg='burlywood', variable = var5, value = 2).place(x=310,y=410)
    a5 = Radiobutton(window, text = "29 states and 9 union territories ",fg='brown4' ,bg='burlywood', variable = var5, value = 3)
    a5.place(x=560,y=410)
    Radiobutton(window, text = "30 states and 10 union territories",fg='brown4' ,bg='burlywood', variable = var5, value = 4).place(x=800,y=410)

    # Question 6 setup
    q6 = Label(window, text ="6. The Indian Premier League (IPL) is a popular professional league in which sport?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q6.place(x=50,y=430)
    a6 = Radiobutton(window, text = "Cricket ",fg='brown4' ,bg='burlywood', variable = var6, value = 1)
    a6.place(x=60,y=450)
    Radiobutton(window, text = "Soccer",fg='brown4' ,bg='burlywood', variable = var6, value = 2).place(x=210,y=450)
    Radiobutton(window, text = "Hockey",fg='brown4' ,bg='burlywood', variable = var6, value = 3).place(x=360,y=450)
    Radiobutton(window, text = "Tennis",fg='brown4' ,bg='burlywood', variable = var6, value = 4).place(x=510,y=450)

    # Question 7 setup
    q7 = Label(window, text ="7. Who was the first woman Prime Minister of India?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q7.place(x=50,y=470)
    a7 = Radiobutton(window, text = "Indira Gandhi ",fg='brown4' ,bg='burlywood', variable = var7, value = 1)
    a7.place(x=60,y=490)
    Radiobutton(window, text = "Sonia Gandhi",fg='brown4' ,bg='burlywood', variable = var7, value = 2).place(x=210,y=490)
    Radiobutton(window, text = "Mamata Banerjee",fg='brown4' ,bg='burlywood', variable = var7, value = 3).place(x=360,y=490)
    Radiobutton(window, text = "Jayalalitha",fg='brown4' ,bg='burlywood', variable = var7, value = 4).place(x=510,y=490)

    # Question 8 setup
    q8 = Label(window, text ="8. Which mountain range forms the northern boundary of India and separates it from the rest of Asia?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q8.place(x=50,y=510)
    Radiobutton(window, text = "Western Ghats",fg='brown4' ,bg='burlywood', variable = var8, value = 1).place(x=60,y=530)
    Radiobutton(window, text = "Eastern Ghats",fg='brown4' ,bg='burlywood', variable = var8, value = 2).place(x=210,y=530)
    a8 = Radiobutton(window, text = "Himalayas",fg='brown4' ,bg='burlywood', variable = var8, value = 3)
    a8.place(x=360,y=530)
    Radiobutton(window, text = "Vindhya Range",fg='brown4' ,bg='burlywood', variable = var8, value = 4).place(x=510,y=530)

    # Question 9 setup
    q9 = Label(window, text ="9. India's highest civilian award, the Bharat Ratna, has been awarded to individuals for their exceptional contributions to various fields. Who was the first recipient of the Bharat Ratna?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q9.place(x=50,y=550)
    Radiobutton(window, text = "Jawaharlal Nehru",fg='brown4' ,bg='burlywood', variable = var9, value = 1).place(x=60,y=570)
    Radiobutton(window, text = "C. V. Raman",fg='brown4' ,bg='burlywood', variable = var9, value = 2).place(x=210,y=570)
    a9 = Radiobutton(window, text = " Sarvepalli Radhakrishnan ",fg='brown4' ,bg='burlywood', variable = var9, value = 3)
    a9.place(x=360,y=570)
    Radiobutton(window, text = "Rajendra Prasad",fg='brown4' ,bg='burlywood', variable = var9, value = 4).place(x=560,y=570)

    # Question 10 setup
    q10 = Label(window, text ="10. The Kumbh Mela, a major pilgrimage and festival in Hinduism, is celebrated at four locations in India. Which river is the site of the Kumbh Mela in Allahabad (Prayagraj)?" ,font=q_font,fg='brown4' ,bg='burlywood')
    q10.place(x=50,y=590)
    a10 = Radiobutton(window, text = "Ganges ",fg='brown4' ,bg='burlywood', variable = var10, value = 1)
    a10.place(x=60,y=610)
    Radiobutton(window, text = "Yamuna",fg='brown4' ,bg='burlywood', variable = var10, value = 2).place(x=210,y=610)
    Radiobutton(window, text = "Saraswati",fg='brown4' ,bg='burlywood', variable = var10, value = 3).place(x=360,y=610)
    Radiobutton(window, text = "Godavari",fg='brown4' ,bg='burlywood', variable = var10, value = 4).place(x=510,y=610)

    # Create the "SUBMIT" button.
    submit = Button(window,text="SUBMIT",width=10, height=2,fg='brown4',bg='burlywood',command=result)
    submit.place(x=350,y=640)
    submit.config(bg='burlywood')    

# Create the main window.
window = Tk()
window.title("Quiz Game")
window.geometry("1500x1000")
window.configure(bg='burlywood')

# Define fonts for labels.
label_font = font.Font(size=24)
q_font = font.Font(size=14)

# Create the title label.
title = Label(window, text= "Welcome to the Quiz", font=label_font, fg='brown4' ,bg='burlywood')
title.place(x=300, y=60)

# Display instructions for the quiz.
inst = Label(window, text = "Instructions:",fg='brown4' ,bg='burlywood')
inst.place(x=50, y=100)
inst1 = Label(window, text ="*To begin, press the Start button." ,fg='brown4' ,bg='burlywood')
inst1.place(x=50,y=120)
inst2 = Label(window, text ="*To choose an answer, simply click or tap on the option you believe is correct" ,fg='brown4' ,bg='burlywood')
inst2.place(x=50,y=140)
inst3 = Label(window, text ="*After finishing the quiz, click or tap the Submit button and your final score will be displayed" ,fg='brown4' ,bg='burlywood')
inst3.place(x=50,y=160)

# Create the "START" button to begin the quiz.
start = Button(window,text="START",width=10, height=2,fg='brown4',bg='burlywood',command=quiz)
start.place(x=350,y=190)
start.config(bg='burlywood')


# Start the main loop.
window.mainloop()
