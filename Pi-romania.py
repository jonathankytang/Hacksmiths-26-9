from tkinter import*
import math
from decimal import Decimal
import sys 

def window1Close():
    window1.destroy()
    
def window2Close():
    window2.destroy()

def window3Close():
    window3.destroy()
    
def quitProgram():
    root.destroy()
    sys.exit()

def finite():
    userInput = int(VuserInput.get())
    while userInput != "":
        array = []
        for i in range(1 , (int(userInput)+1)):
            pi = math.pi
            x = Decimal(pi) 

            output = round(x , int(i))

            array.append(str(output))

            
        global window1
        window1 = Tk()
        window1.title = ("Finite List")
        text2 = Label(window1, text="Here we go:", font="Arial 80 bold")
        text2.pack()
        for item in array:
            text = Label(window1, text=item, font="Arial 20")
            text.pack()
        button9 = Button(window1, text="Close Window", command=window1Close)
        button9.pack()
        window1.mainloop()

    else:
        #User Interface - error message for not inputting a new file name
        global window3
        window3 = Tk()
        window3.title = ("Error")
        window3Header1 = Label(window3, text="ERROR", font="Arial 36 bold")
        window3Header1.pack()
        window3Header2 = Label(window3, text="Please enter a new file name ", font="Arial 18")
        window3Header2.pack()
        button4 = Button(window3, text="Close", command=window3Close)
        button4.pack()
        window3.mainloop()
        

def infinite():
    global window2
    window2 = Tk()
    window2.title = ("Ininite List")
    window2Header1 = Label(window2, text="Nah this don't work yet", font="Arial 50")
    window2Header1.pack()
    button1 = Button(window2, text="Close window", command=window2Close)
    button1.pack()
    window2.mainloop()
    

root = Tk()
root.title = ("Home")
root.geometry = ("700 x 700")

VuserInput = IntVar()
VuserInput.set(2)

blank1 = Label(root, text="").grid(row=1, column=1, columnspan=3)
logo = PhotoImage(file="Goldsmiths_small_1.gif")
img = Label(root, image = logo).grid(row=2, column=1, columnspan=3)

header1 = Label(root, text="Pi-romania", font="Arial 50 bold").grid(row=3, column=1, columnspan=3)

blank2 = Label(root, text="").grid(row=4, column=1, columnspan=3)

subheader1 = Label(root, text="1. Finite", font="Arial 30 bold").grid(row=5, column=1, columnspan=3)

userInputheader = Label(root, text="Enter how many decimal places you want pi to", font="Arial 20").grid(row=6, column=1, columnspan=3)
userInputTb = Entry(root, textvariable=VuserInput).grid(row=7, column=1, columnspan=3)
button1 = Button(root, text="Go!", command=finite).grid(row=8, column=1, columnspan=3)
blank3 = Label(root, text="").grid(row=9, column=1, columnspan=3)

subheader2 = Label(root, text="2. Infinite", font="Arial 30 bold").grid(row=10, column=1, columnspan=3)
subsubheader1 = Label(root, text="Click 'GO!' to see!", font="Arial 20").grid(row=11, column=1, columnspan=3)
button2 = Button(root, text="Go!", command=infinite).grid(row=12, column=1, columnspan=3)

blank4 = Label(root, text="").grid(row=13, column=1, columnspan=3)
button3 = Button(root, text="Quit Program", command=quitProgram).grid(row=14, column=3)

root.mainloop()
