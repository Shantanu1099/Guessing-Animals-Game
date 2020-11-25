from tkinter import *
import os
root=Tk()
canvas = Canvas(root,width = 800, height = 550, bg = 'grey')
canvas.pack()
def abc():
	os.system('game2.py')
	root.destroy()
def vil():
    window =Tk()
    window.geometry('500x300')
    l2=Label(window,text="Choose the Animals",font=("Arial Bold",30))
    l2.grid(row=0,columnspan=5)
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3= IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6= IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    CheckVar9= IntVar()
    C1 = Checkbutton(window, text = "Elephant", variable = CheckVar1,
                 onvalue = 1, offvalue = 0, height=2,width = 10,bg='red',bd='2')
    C2 = Checkbutton(window, text = "Tiger", variable = CheckVar2, 
                 onvalue = 1, offvalue = 0, height=2, 
                 width = 10,bg='yellow',bd='2')
    C3 = Checkbutton(window, text = "Lion", variable = CheckVar3,
                 onvalue = 1, offvalue = 0, height=2,width = 10,bg='green',bd='2')
    C4 = Checkbutton(window, text = "Dog", variable = CheckVar4, 
                 onvalue = 1, offvalue = 0, height=2, 
                 width = 10,bg='orange',bd='2')
    C5 = Checkbutton(window, text = "Cat", variable = CheckVar5,
                 onvalue = 1, offvalue = 0, height=2,width = 10,bg='orange',bd='2')
    C6 = Checkbutton(window, text = "Peacock", variable = CheckVar6, 
                 onvalue = 1, offvalue = 0, height=2, 
                 width = 10,bg='green',bd='2')
    C7 = Checkbutton(window, text = "Zebra", variable = CheckVar7,
                 onvalue = 1, offvalue = 0, height=2,width = 10,bg='yellow',bd='2')
    C8 = Checkbutton(window, text = "Panda", variable = CheckVar8, 
                 onvalue = 1, offvalue = 0, height=2, 
                 width = 10,bg='red',bd='2')
    C9 = Checkbutton(window, text = "Owl", variable = CheckVar9,
                 onvalue = 1, offvalue = 0, height=2,width = 10,bg='orange',bd='2')
    C1.grid(row=1,column=0)
    C2.grid(row=2,column=0)
    C3.grid(row=3,column=0)
    C4.grid(row=1,column=1)
    C5.grid(row=2,column=1)
    C6.grid(row=3,column=1)
    C7.grid(row=1,column=2)
    C8.grid(row=2,column=2)
    C9.grid(row=3,column=2)
    B = Button(window, text = "Submit")
    B.grid(row=10,columnspan=3)
    window.mainloop()


gif1 = PhotoImage(file = 'zebra.gif')
gif2 = PhotoImage(file = 'lion.gif')
gif3 = PhotoImage(file = 'tiger.gif')
gif4 = PhotoImage(file = 'elephant.gif')
gif5 = PhotoImage(file = 'peacock.gif')
canvas.create_image(400,300, image = gif5, anchor = NW)
canvas.create_image(200,300, image = gif4, anchor = NW)
canvas.create_image(600,100, image = gif3, anchor = NW)
canvas.create_image(350,100, image = gif2, anchor = NW)
canvas.create_image(100,100, image = gif1, anchor = NW)
B = Button(root, text = "Refresh",command=abc)
B.place(x = 350,y = 500)
B2=Button(root, text="OK", command=vil)
B2.place(x=450,y=500)
root.mainloop()


