from tkinter import *

def write(x):
    s = len(entrance.get())
    entrance.insert(s,str(x))
    # print(x)

calculation = 5
s1 = 0

def procedures(x):
    global calculation
    calculation = x
    global s1
    s1= float(entrance.get())
    print(calculation)
    print(s1)
    entrance.delete(0,'end')


s2= 0
def calculate():
    global s2
    s2 = float(entrance.get())
    print(s2)
    global calculation
    result=0
    if(calculation==0):
        result = s1 + s2
    elif(calculation==1):
        result = s1 - s2
    elif(calculation == 2):
        result = s1 * s2
    elif (calculation == 3):
        result = s1 / s2

    entrance.delete(0,'end')
    entrance.insert(0,str(result))






pencere = Tk()
pencere.geometry('250x300')

entrance = Entry(font='Verdana 14 bold',width=15,justify=RIGHT)
entrance.place(x=20,y=20)

b = []

for i in range(1,10):
    b.append(Button(text=str(i), font='Verdana 14 bold',command= lambda x=i:write(x)))

sayac = 0
for i in range(0, 3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=50+i*50)
        sayac += 1

procedure = []

for i in range(0,4):
    procedure.append(Button(font='Verdana 14 bold',width=2,command=lambda x=i:procedures(x)))

procedure[0]['text'] = '+'
procedure[1]['text'] = '-'
procedure[2]['text'] = 'x'
procedure[3]['text'] = ':'

for i in range(0,4):
    procedure[i].place(x=170,y=50+50*i)

sb= Button(text=0,font='Verdana 14 bold',command=lambda x=0:write(x))
sb.place(x=20,y=200)

nb=Button(text='.',font='Verdana 14 bold',command=lambda x='.':write(x))
nb.place(x=70,y=200)

eb= Button(text='=',fg='RED',font='Verdana 14 bold',command=calculate)
eb.place(x=120,y=200)

pencere.mainloop()