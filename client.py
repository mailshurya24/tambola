import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTk

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas

    nameWindow = Tk()
    nameWindow.title("Tambola")
    nameWindow.geometry('800x600')

    screenWidth = nameWindow.winfo_screenwidth()
    screenHeight = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas = Canvas(nameWindow, width = 500, height = 500)
    canvas.pack(fill = "both", expand = True)

    canvas.create_image(0, 0, image = bg, anchor = 'nw')
    canvas.create_text(screenWidth/4.5, screenHeight/8, text = "Enter Name:", font = ("Chalkboard SE", 20))

    nameEntry = Entry(nameWindow, width = 15, justify = 'center', font = ("Chalkboard SE", 20), bd = 5, bg = 'white')
    nameEntry.place(x = screenWidth/7, y = screenHeight/5.5)

    button = Button(nameWindow, text = "Sign In", font = ("Chalkboard SE", 20), width = 15, bg = "#80deea", bd = 3,
    command = saveName)
    button.place(x = screenWidth/6, y = screenHeight/4)

    nameWindow.resizable(True,True)
    nameWindow.mainloop()

def saveName():
    global server
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    server.send(playerName.encode())

def setup():
    global server
    global port
    global ip

    port = 6000
    ip = "127.0.0.1"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    thread = Thread(target = msg)
    thread.start()