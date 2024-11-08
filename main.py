from tkinter import Tk, Label, Button, Entry
from tkinter.messagebox import showerror
from pyautogui import size, click, moveTo, mouseDown, mouseUp
from time import sleep

def GetScreenSize():
    ViewScreenSizeX, ViewScreenSizeY = size()
    # print(ViewScreenSizeX, ViewScreenSizeY)
    lab1.config(text=f"Your screen size is {ViewScreenSizeX}*{ViewScreenSizeY}", fg="#cf1c13")

def ErorrMessage(error):
    showerror(title="Error Message", message=f"{error}")

def DataFunction():
    pass

def ClickScreen():
    Xaxis, Yaxis = size()
    
    try:
        ScreenSizeX = int(getvalueX.get())
    except:
        ScreenSizeX = Xaxis/2
    try:
        ScreenSizeY = int(getvalueY.get())
    except:
        ScreenSizeY = Yaxis/2
    try:
        ClickNumber = int(ent3.get())
    except:
        ClickNumber = 10
    try:
        ClickTime = float(ent4.get())
    except:
        ClickTime = 0.1
    lab7.config(text="complate : 00")

    if ((0 < ScreenSizeX < Xaxis) and (0 < ScreenSizeY < Yaxis) and (0 < ClickNumber < 10000) and (0 < ClickTime < 10)):
        for i in range(ClickNumber):
            click(ScreenSizeX, ScreenSizeY)
            lab7.config(text=f"complate : {str(i+1)}")
            sleep(ClickTime)
    else:
        ErorrMessage("Limit Out!")

def HoldScreen():
    Xaxis, Yaxis = size()
    
    try:
        ScreenSizeX = int(getvalueX.get())
    except:
        ScreenSizeX = Xaxis/2
    try:
        ScreenSizeY = int(getvalueY.get())
    except:
        ScreenSizeY = Yaxis/2
    try:
        HoldTime = int(getHoldValue.get())
    except:
        HoldTime = 5

    # Move the mouse to a specific position (optional)
    moveTo(ScreenSizeX, ScreenSizeY)

    # Hold down the left mouse button
    mouseDown(button='left')

    # Keep it held for 3 seconds
    sleep(HoldTime)

    # Release the left mouse button
    mouseUp(button='left')
    




root = Tk()

root.title("Screen Click")
root.geometry("600x750+20+30")  # widght * hight + x + y
root.resizable(False, False)
root.config(bg="#70dcb8")
root.attributes("-alpha", 0.8)
# root.iconbitmap("logo.ico")


# Header
lab0 = Label(root, text="Screen click", bg="#70dcb8", fg="#c813cf", font=("Arial", 12, "bold italic")).place(x=190, y=10, height=30, width=220)

# Screen size
lab1 = Label(root, text="Your Screen Size is 0000*0000", bg="#70dcb8", font=("Arial", 10, "bold italic"))
lab1.place(x=20, y=80, height=30, width=300)

btn1 = Button(root, text="Get Screen Size", font=("Kanit", 7, "bold"), command=GetScreenSize).place(x=400, y=80, height=30, width=140)

# Tuch screen
lab2 = Label(root, text="Enter value :", bg="#70dcb8", font=("Arial", 13, "bold")).place(x=20, y=150, height=30, width=170)

# X asix value
lab3 = Label(root, text="Enter the X axis :", bg="#70dcb8", font=("Arial", 10, "bold")).place(x=30, y=210, height=25, width=200)

getvalueX = Entry(root, font=("Arial", 10, "bold italic"))
getvalueX.place(x=310, y=210, height=25, width=100)

# Y asis value
lab4 = Label(root, text="Enter the Y axis :", bg="#70dcb8", font=("Arial", 10, "bold")).place(x=30, y=250, height=25, width=200)

getvalueY = Entry(root, font=("Arial", 10, "bold italic"))
getvalueY.place(x=310, y=250, height=25, width=100)

# Number of click
lab5 = Label(root, text="Enter the number of click :", bg="#70dcb8", font=("Arial", 10, "bold")).place(x=50, y=290, height=25, width=250)

ent3 = Entry(root, font=("Arial", 10, "bold italic"))
ent3.place(x=310, y=290, height=25, width=100)

# Time of click
lab6 = Label(root, text="Enter the time of tuch :", bg="#70dcb8", font=("Arial", 10, "bold")).place(x=30, y=330, height=25, width=260)

ent4 = Entry(root, font=("Arial", 10, "bold italic"))
ent4.place(x=310, y=330, height=25, width=100)

# Time of hold
lab9 = Label(root, text="Enter the time of hold :", bg="#70dcb8", font=("Arial", 10, "bold")).place(x=30, y=370, height=25, width=260)

getHoldValue = Entry(root, font=("Arial", 10, "bold italic"))
getHoldValue.place(x=310, y=370, height=25, width=100)

# click complate text
lab7 = Label(root, text="complate : 00", bg="#70dcb8", font=("Arial", 8, "italic"))
lab7.place(x=230, y=430, height=20, width=140)

# Click button
btm2 = Button(root, text="Start Click", bg="#dd4918", font=("Kanit", 10, "bold"), command=ClickScreen).place(x=200, y=500, height=40, width=200)

# Hold Button
btm3 = Button(root, text="Start Hold", bg="#dd4918", font=("Kanit", 10, "bold"), command=HoldScreen).place(x=200, y=560, height=40, width=200)

# Developer info
lab8 = Label(root, text="Developer : Md Rifat Rahman \nFrom : Enjoy Tech And Software \ncopyright ©", bg="#fff", font=("Kanit", 6, "bold italic"))
lab8.place(x=0, y=700, height=50, width=600)


if __name__== "__main__":
    root.mainloop()



"""
import pyautogui
import time

time.sleep(6)

# Move the mouse to a specific position (optional)
pyautogui.moveTo(960, 360)

# Hold down the left mouse button
pyautogui.mouseDown(button='left')

# Keep it held for 3 seconds
time.sleep(60)

# Release the left mouse button
pyautogui.mouseUp(button='left')
"""
