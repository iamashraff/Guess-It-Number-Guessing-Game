'''
--------------------------------
https://github.com/iamashraff
https://ashraff.me
© 2023 Ashraff
--------------------------------
'''
import os
import tkinter as tk
from tkinter import StringVar, ttk, messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import random
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame import mixer


window = tk.Tk()
window.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + '\icon.ico')
window.title("Guess It !")
window.geometry("350x510")
window.resizable(0,0)

# Create frame
style = ttk.Style(window)
dir_path = os.path.dirname(os.path.realpath(__file__))
window.tk.call('source', os.path.join(dir_path, 'azure.tcl'))
style.theme_use('azure')
style.configure("Accentbutton", foreground='white')
frame = tk.Frame()
frame.pack()
imgdir= os.path.dirname(os.path.realpath(__file__))
playerName = 'Anonymous'

#Randomly pick playimg
def randomImgPickFile():
    randomImg = random.randint(1,7)
    imgplayfile = 'playimg\\' + str(randomImg) + '.png'
    return imgplayfile

imgplayfile = randomImgPickFile()

#Randomly assign playimg
def randomImgShuffle():
    imgplay = Image.open(os.path.join(imgdir, randomImgPickFile()))
    resized_imgplay = imgplay.resize((140,140))
    imgplay = ImageTk.PhotoImage(resized_imgplay)
    playimg.config(image=imgplay)
    playimg.image = imgplay

#Play music
def playMusic(loop,file):
    pygame.mixer.music.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sound\\' + file))
    pygame.mixer.music.play(loops=loop)
    pygame.mixer.music.set_volume(0.2)

#Play sound effects
def playSfx(file):
    sfx = mixer.Sound(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sound\\' + file))
    sfx.play()


pygame.init()
playMusic(-1, 'main.mp3')

# Function to center window
def centerWindow(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Generate random numbers and assigned to list
def generateRandom():
    randNumbers = []
    for i in range(3):  
        rd = random.randint(0, 9)
        randNumbers.append(rd)
    return randNumbers

randomList = generateRandom()
count = 0

fermibeepsound = [0,0,0]

# Check if the number is correct
def checkNumber():
    counter()
    randomImgShuffle()
    randNumbers = randomList
    guesses = []
    guesses.append(int(number1.get()))
    guesses.append(int(number2.get()))
    guesses.append(int(number3.get()))
    result = []
    print(randNumbers)
    playSfx('beep.mp3')
    if(guesses == randNumbers):
        correctAnswer()
    else:
        for i in range(3):
            if(guesses[i] == randNumbers[i]):
                result.insert(i,'Fermi')
                fermibeepsound[i] +=1
                if (fermibeepsound[i] == 1):
                    playSfx('beep2.mp3')
            elif(guesses[i] in randNumbers):
                result.insert(i,'Pico')
            elif(guesses[i] != randNumbers[i]):
                result.insert(i,'Nano')
        label.config(text=result)

#Function to check number without initiate the counter
def checkNumberwoCounter():
    randNumbers = randomList
    guesses = []
    guesses.append(int(number1.get()))
    guesses.append(int(number2.get()))
    guesses.append(int(number3.get()))
    result = []
    print(randNumbers)
    if(guesses == randNumbers):
        correctAnswer()
    else:
        for i in range(3):
            if(guesses[i] == randNumbers[i]):
                result.insert(i,'Fermi')
            elif(guesses[i] in randNumbers):
                result.insert(i,'Pico')
            elif(guesses[i] != randNumbers[i]):
                result.insert(i,'Nano')
        label.config(text=result)

#Function to initiate counter
def counter():
    global count
    count +=1
    labelCount.config(text="Guesses : " + str(count))

start_time = 0
minutes = 0
seconds = 0
timer_running = False

#Function to start timer
def start_timer():
    global start_time, timer_running
    start_time = time.time()
    timer_running = True
    update_label()

#Function to stop timer
def stop_timer():
    global timer_running
    timer_running = False

#Update the timer laber
def update_label():
    global timer_running
    global minutes
    global seconds
    if timer_running:
        elapsed_time = int(time.time() - start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        labelTimer.config(text="{:02d}:{:02d}".format(minutes, seconds))
        labelTimer.after(1000, update_label)

#Invoked if btnStart is clicked
def startBtn():
    global start_time
    global count
    global randomList
    global fermibeepsound
    start_time = 0
    count = 0
    for i in range(3):
        fermibeepsound[i] = 0
    randomList = generateRandom()
    labelCount.config(text="Guesses : " + str(count))
    logo.grid_forget()
    btnPlay.grid_forget()
    btnScoreboard.grid_forget()
    btnHelp.grid_forget()
    btnAbout.grid_forget()
    btnExit.grid_forget()
    labelCopyright.grid_forget()
    labelCount.grid(row=0, column=0, pady=10)
    labelTimer.grid(row=0, column=2, pady=10)
    playimg.grid(row=1, column=0, columnspan=4)
    label.grid(row=2, column=0,  pady=10, columnspan=4)
    number1.grid(row=3, column=0, padx=20)
    number1.delete(0, 'end')
    number1.insert(0, '0')
    number2.grid(row=3, column=1, padx=20)
    number2.delete(0, 'end')
    number2.insert(0, '0')
    number3.grid(row=3, column=2, padx=20, pady=30)
    number3.delete(0, 'end')
    number3.insert(0, '0')
    btnCheck.grid(row=4, column=0, columnspan=2)
    btnSurrender.grid(row=4, column=1, columnspan=4, pady=10)
    window.geometry("450x400")
    start_timer()
    checkNumberwoCounter()
    playMusic(-1, 'play.mp3')
    playSfx('gamestart.mp3')

#Invoked if btnMainMenu is clicked
def mainmenuBtn():
    window.geometry("350x510")
    logo.grid(row=1, column=0, columnspan=4, pady=10)
    btnPlay.grid(row=2, column=0, columnspan=4, pady=5)
    btnScoreboard.grid(row=3, column=0, columnspan=4, pady=5)
    btnHelp.grid(row=4, column=0, columnspan=4, pady=5)
    btnAbout.grid(row=5, column=0, columnspan=4, pady=5)
    btnExit.grid(row=6, column=0, columnspan=4, pady=5)
    labelCopyright.grid(row=7, column=0, columnspan=4, ipady=30)
    surrenderimg.grid_forget()
    correctimg.grid_forget()
    labelEnd.grid_forget()
    labelEnd2.grid_forget()
    labelAnswer.grid_forget()
    labelTime.grid_forget()
    btnMainMenu.grid_forget()
    btnPlayAgain.grid_forget()
    labelCountResult.grid_forget()
    playMusic(-1, 'main.mp3')

#Invoked if btnSurrender is clicked
def surrenderBtn():
    stop_timer()
    window.geometry("350x450")
    playimg.grid_forget()
    labelCount.grid_forget()
    labelTimer.grid_forget()
    label.grid_forget()
    number1.grid_forget()
    number2.grid_forget()
    number3.grid_forget()
    btnCheck.grid_forget()
    btnSurrender.grid_forget()
    surrenderimg.grid(row=0, column=0, columnspan=4, pady=30)
    labelEnd.grid(row=1, column=0,  pady=10, columnspan=4)
    labelEnd.config(text='Surrendered !', foreground='red')
    labelAnswer.grid(row=2, column=0, columnspan=4, pady=10)
    labelAnswer.config(text='Correct answer is '+ ' '.join(map(str, randomList)) + '.', foreground='green')
    labelTime.grid(row=3, column=0, columnspan=4)
    labelTime.config(text="Time: {:02d}:{:02d}".format(minutes, seconds))
    labelCountResult.grid(row=4, column=0, columnspan=4, pady=10)
    labelCountResult.config(text="You have guess " + str(count) + ' time(s) !')
    btnPlayAgain.grid(row=5, column=0, columnspan=4, pady=5)
    btnMainMenu.grid(row=6, column=0, columnspan=4)
    savetoScoreboard('Surrendered')
    playMusic(1, 'gameover.mp3')

#Invoked if answer provided is correct
def correctAnswer():
    stop_timer()
    window.geometry("350x450")
    playimg.grid_forget()
    labelCount.grid_forget()
    labelTimer.grid_forget()
    label.grid_forget()
    number1.grid_forget()
    number2.grid_forget()
    number3.grid_forget()
    btnCheck.grid_forget()
    btnSurrender.grid_forget()
    correctimg.grid(row=0, column=0, columnspan=4, pady=30)
    labelEnd.grid(row=1, column=0, columnspan=4)
    labelEnd.config(text='Congratulations !', foreground='green')
    labelEnd2.grid(row=2, column=0, columnspan=4)
    labelEnd2.config(text=' '.join(map(str, randomList)) + ' is a correct answer.', foreground='green')
    labelTime.grid(row=3, column=0, pady=10, columnspan=4)
    labelTime.config(text="Time: {:02d}:{:02d}".format(minutes, seconds))
    labelCountResult.grid(row=4, column=0, columnspan=4, pady=10)
    labelCountResult.config(text="You have guess " + str(count) + ' time(s) !')
    btnPlayAgain.grid(row=5, column=0, columnspan=4, pady=5)
    btnMainMenu.grid(row=6, column=0, columnspan=4)
    savetoScoreboard('Solved')
    playMusic(1, 'congrats.mp3')

#Invoked if btnHelp is clicked
def helpBtn():
    playSfx('click.mp3')
    messagebox.showinfo("Help", "Guess the 3 numbers range from 0 to 9 in the shortest time possible !\n\nThe hint will be shown as the following:\n1. Fermi - If the number is guessed in the correct position\n2. Pico - If the number guessed is correct but in a different position\n3. Nano - If the number guessed does not match any of the three numbers\n\nGood Luck & Have Fun !")

#Invoked if btnAbout is clicked
def aboutBtn():
    playSfx('click.mp3')
    messagebox.showinfo("About", "Developed by Ashraff\nhttps://github.com/iamashraff\n\n- Icon by SoulGIE@Flaticon\n- SFX by Pixabay\n- Azure ttk theme by rdbende\n- Pygame module library which is distributed under GNU LGPL version 2.1.\n\n© 2023 Ashraff")

#Invoked if btnExit is clicked
def exitBtn():
    playSfx('click.mp3')
    btnPlay.grid_forget()
    btnScoreboard.grid_forget()
    btnHelp.grid_forget()
    btnAbout.grid_forget()
    btnExit.grid_forget()
    labelCopyright.grid_forget()
    window.geometry("350x300")
    img = Image.open(os.path.join(imgdir, 'dispimg\\thankyou.png'))
    resized_img = img.resize((230, 220))
    img = ImageTk.PhotoImage(resized_img)
    logo.config(image=img)
    logo.image = img
    labelClosing.grid(row=2, column=0, pady=10, columnspan=4)
    countdownClosing(3)

#Function to countdown of closing application
def countdownClosing(remaining):
    if remaining < 0:
        window.destroy()
    else:
        labelClosing.configure(text=f"Leaving you in {remaining} seconds...")
        playSfx('click.mp3')
        window.after(1000, countdownClosing, remaining - 1)

#Invoked if btnPlayAgain is clicked
def playAgain():
    global start_time
    global count
    global randomList
    start_time = 0
    count = 0
    randomList = generateRandom()
    labelCount.config(text="Guesses : " + str(count))
    surrenderimg.grid_forget()
    correctimg.grid_forget()
    labelEnd.grid_forget()
    labelEnd2.grid_forget()
    labelAnswer.grid_forget()
    labelTime.grid_forget()
    labelCountResult.grid_forget()
    btnPlayAgain.grid_forget()
    btnMainMenu.grid_forget()
    startBtn()

#Invoked if btnScoreboard is clicked
def scoreboardBtn():
    scoreboard = tk.Toplevel(frame)
    scoreboard.title('Scoreboard')
    scoreboard.resizable(0,0)
    scoreboard.attributes('-top', True)
    scoreboard.grab_set()
    table = ttk.Treeview(scoreboard, selectmode="extended")
    # Define the columns of the table
    table['columns'] = ('Name', 'Guesses', 'Time', 'Status')
    # Format the columns
    table.column('#0', width=0, stretch=tk.NO)
    table.column('Name', anchor=tk.CENTER, width=100)
    table.column('Guesses', anchor=tk.CENTER, width=100)
    table.column('Time', anchor=tk.CENTER, width=100)
    table.column('Status', anchor=tk.CENTER, width=100)
    # Create headings
    table.heading('#0', text='', anchor=tk.CENTER)
    table.heading('Name', text='Name', anchor=tk.CENTER)
    table.heading('Guesses', text='Guesses', anchor=tk.CENTER)
    table.heading('Time', text='Time', anchor=tk.CENTER)
    table.heading('Status', text='Status', anchor=tk.CENTER)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dir_path, 'score.txt')
    with open(filepath) as file:
        for line in file:
            columns = line.strip().split(',')
            table.insert(parent='', index='end', values=columns)
    table.pack()
    centerWindow(scoreboard)
    playSfx('click.mp3')

#Function to enter player name at game start
def enterplayerName():
    global playerName
    playerName = simpledialog.askstring("Player Name", "Please enter your name:", parent=frame)
    if playerName is None:
        playerName = 'Anonymous'
    else:
        if playerName == '':
            playerName = 'Anonymous'
        print(playerName)
        startBtn()

#Invoked once player has ended the game
def savetoScoreboard(status):
    global playerName
    global count
    global minutes
    global seconds
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dir_path, 'score.txt')
    
    with open(filepath, 'a') as file:
        file.write(str(playerName)+','+str(count)+','+"{:02d}:{:02d}".format(minutes, seconds)+','+status+'\n')


def spinbox_callback():
    playSfx('beep.mp3')

#Validate the input number value in the game
def validate(*args):
    try:
        value1 = int(number1.get())
        if value1 > 9:
            number1.delete(0, 'end')
            number1.insert(0, '9')
            messagebox.showerror("Error","Value cannot more than 9 !")
    except ValueError:
        number1.delete(0, 'end')
        number1.insert(0, '0')
        messagebox.showerror("Error","Only numeric value is accepted !")

    try:
        value2 = int(number2.get())
        if value2 > 9:
            number2.delete(0, 'end')
            number2.insert(0, '9')
            messagebox.showerror("Error","Value cannot more than 9 !")
    except ValueError:
        number2.delete(0, 'end')
        number2.insert(0, '0')
        messagebox.showerror("Error","Only numeric value is accepted !")
    
    try:
        value3 = int(number3.get())
        if value3 > 9:
            number3.delete(0, 'end')
            number3.insert(0, '9')
            messagebox.showerror("Error","Value cannot more than 9 !")
    except ValueError:
        number3.delete(0, 'end')
        number3.insert(0, '0')
        messagebox.showerror("Error","Only numeric value is accepted !")



# Logo
img = Image.open(os.path.join(imgdir, 'dispimg\\guesslogo.png'))
resized_img = img.resize((185,220))
img = ImageTk.PhotoImage(resized_img)
logo = ttk.Label(frame, image=img)
logo.config(image=img)
logo.grid(row=1, column=0, columnspan=4, pady=10)
labelClosing = ttk.Label(frame, font=('Helvetica', 12))

#Play button
btnPlay = ttk.Button(frame, style="Accentbutton", text="Play", command=enterplayerName)
btnPlay.grid(row=2, column=0, columnspan=4, pady=5)
btnScoreboard = ttk.Button(frame, text="Scoreboard", command=scoreboardBtn)
btnScoreboard.grid(row=3, column=0, columnspan=4, pady=5)
btnHelp = ttk.Button(frame, text="Help", command=helpBtn)
btnHelp.grid(row=4, column=0, columnspan=4, pady=5)
btnAbout = ttk.Button(frame, text="About", command=aboutBtn)
btnAbout.grid(row=5, column=0, columnspan=4, pady=5)
btnExit = ttk.Button(frame, text="Exit", command=exitBtn)
btnExit.grid(row=6, column=0, columnspan=4, pady=5)
labelCopyright = ttk.Label(frame, text='© 2023 Ashraff', font=('Helvetica 10'), foreground='grey')
labelCopyright.grid(row=7, column=0, columnspan=4, ipady=30)

#-----------------------------

imgplay = Image.open(os.path.join(imgdir, imgplayfile))
resized_imgplay = imgplay.resize((140,140))
imgplay = ImageTk.PhotoImage(resized_imgplay)
playimg = ttk.Label(frame, image=imgplay)
playimg.config(image=imgplay)

labelCount = ttk.Label(frame, text='Guesses : 0', font=('Helvetica 12 bold'))
labelTimer = ttk.Label(frame, text='00:00', font=('Helvetica 12 bold'))
label = ttk.Label(frame, text='Guess the number', font=('Helvetica', 17))
number1 = ttk.Spinbox(frame, width=5, from_=0, to=9, increment=1, font=('Arial', 13), command=spinbox_callback)
number1.bind('<KeyRelease>', validate)
number2 = ttk.Spinbox(frame, width=5, from_=0, to=9, increment=1, font=('Arial', 13), command=spinbox_callback)
number2.bind('<KeyRelease>', validate)
number3 = ttk.Spinbox(frame, width=5, from_=0, to=9, increment=1, font=('Arial', 13), command=spinbox_callback)
number3.bind('<KeyRelease>', validate)
btnCheck = ttk.Button(frame, style="Accentbutton", text="Check Guesses", command=checkNumber)
btnSurrender = ttk.Button(frame, text="Surrender", command=surrenderBtn)
btnPlayAgain = ttk.Button(frame, style="Accentbutton", text="Play Again", command=playAgain)
btnMainMenu = ttk.Button(frame, text="Main Menu", command=mainmenuBtn)
#-----------------------------
#END GAME

imgsurr = Image.open(os.path.join(imgdir, 'dispimg\\surrender.png'))
resized_imgsurr = imgsurr.resize((140,140))
imgsurr = ImageTk.PhotoImage(resized_imgsurr)
surrenderimg = ttk.Label(frame, image=imgsurr)
surrenderimg.config(image=imgsurr)

imgcorrect = Image.open(os.path.join(imgdir, 'dispimg\\correct.png'))
resized_imgcorrect = imgcorrect.resize((140,140))
imgcorrect = ImageTk.PhotoImage(resized_imgcorrect)
correctimg = ttk.Label(frame, image=imgcorrect)
correctimg.config(image=imgcorrect)

labelEnd = ttk.Label(frame, font=('Arial', 17))
labelEnd2 = ttk.Label(frame, font=('Arial', 13))
labelAnswer = ttk.Label(frame, font=('Arial', 12))
labelTime = ttk.Label(frame, font=('Arial', 11))
labelCountResult = ttk.Label(frame, font=('Arial', 11))
#-----------------------------
centerWindow(window)
window.mainloop()