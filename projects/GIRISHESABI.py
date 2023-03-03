from tkinter import *

data = ('account','password')
trial_right = 3

def sign_in():
    global trial_right
    if trial_right<=0:
        return False

    uName =  name.get()
    Password = password.get()
    print(uName,'-',Password)
    print('Checking...')

    if (uName==data[0] and Password==data[1]):
        print('Entrance accepted...')
        result.config(text="ID NO:12345, Driver's  license NO:4321")
        cleanscreen()

    else:
        print("False information")
        trial_right -= 1
        result.config(text='FALSE INFORMATION! your trial right: %d'%trial_right)

def cleanscreen():
    greeting.config(text="Xalil Rasulov,welcome to our system...")
    askname.destroy()
    name.destroy()
    askpassw.destroy()
    btn.destroy()



window= Tk()
window.title("ENTRANCE SCREEN")
window.geometry('400x400+100+100')

greeting = Label(window)
greeting.config(text="WELOCME, PLEASE ENTER YOUR INFORMATIONS...")
greeting.pack()

askname=Label(window)
askname.config(text="USERNAME:")
askname.pack()

name = Entry(window)
name.pack()

askpassw = Label(window)
askpassw.config(text = "PASSQORD:")
askpassw.pack()

password = Entry(window)
password.pack()

btn = Button(window)
btn.config(text = "SIGN IN",command=sign_in)
btn.pack()

result = Label(window)
result.config(text="Haven't signed in")
result.pack()

mainloop()