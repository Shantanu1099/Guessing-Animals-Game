import random
import os
from tkinter import *
root=Tk()
root.title('GAME')
root.geometry('1200x600')
canvas = Canvas(root,width =1400, height =800, bg ='grey')
canvas.grid()
def vil():
    window =Tk()
    window.title('OPTIONS')
    window.geometry('1300x400')
    window.configure(background='dark orchid')
    l2 = Label(window, text="CHOOSE THE ANIMALS",font=(50), bg='dark orchid')
    l2.grid(row=0, columnspan=5, padx=20, pady=40)
            
    CheckVar1 = IntVar() 
    C1 = Checkbutton(window, text="Elephant",variable=CheckVar1,onvalue = 1, offvalue = 0,height=2, width=10, bg='red', bd='2')
    CheckVar2 = IntVar()
    C2 = Checkbutton(window, text="Tiger", variable=CheckVar2,onvalue = 1, offvalue = 0,height=2,width=10, bg='yellow', bd='2')
    CheckVar3 = IntVar()
    C3 = Checkbutton(window, text="Lion", variable=CheckVar3, onvalue = 1, offvalue = 0,height=2, width=10, bg='green', bd='2')
    CheckVar4 = IntVar()
    C4 = Checkbutton(window, text="Dog", variable=CheckVar4,onvalue = 1, offvalue = 0,height=2,width=10, bg='orange', bd='2')
    CheckVar5 = IntVar()
    C5 = Checkbutton(window, text="Cat", variable=CheckVar5, onvalue = 1, offvalue = 0,height=2, width=10, bg='green', bd='2')
    CheckVar6 = IntVar()
    C6 = Checkbutton(window, text="Peacock", variable=CheckVar6,onvalue = 1, offvalue = 0,height=2,width=10, bg='red', bd='2')
    CheckVar7 = IntVar()
    C7 = Checkbutton(window, text="Zebra", variable=CheckVar7,onvalue = 1, offvalue = 0,height=2, width=10, bg='yellow', bd='2')
    CheckVar8 = IntVar()
    C8 = Checkbutton(window, text="Panda", variable=CheckVar8, onvalue = 1, offvalue = 0,height=2,width=10, bg='red', bd='2')
    CheckVar9 = IntVar()
    C9 = Checkbutton(window, text="Owl", variable=CheckVar9,onvalue = 1, offvalue = 0,height=2, width=10, bg='orange', bd='2')
    C1.grid(row=1, column=0)
    C2.grid(row=2, column=0)
    C3.grid(row=3, column=0)
    C4.grid(row=1, column=1)
    C5.grid(row=2, column=1)
    C6.grid(row=3, column=1)
    C7.grid(row=1, column=2)
    C8.grid(row=2, column=2)
    C9.grid(row=3, column=2)
    def mget():
        v1=CheckVar1.get()
        v2=CheckVar2.get()
        v3=CheckVar3.get()
        v4=CheckVar4.get()
        v5=CheckVar5.get()
        v6=CheckVar6.get()
        v7=CheckVar7.get()
        v8=CheckVar8.get()
        v9=CheckVar9.get()
        print(v1,v2,v3,v4,v5,v6,v7,v8,v9)
    B = Button(window,text="SUBMIT",command=lambda:os.system('final.py'))
    B.grid(row=10, columnspan=3, padx=20, pady=40)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.mainloop()

a=random.randint(0,5)
if(a==0):
        gif1 = PhotoImage(file = 'dog.gif')
        gif2 = PhotoImage(file = 'cat.gif')
        gif3 = PhotoImage(file = 'elephant.gif')
        gif4 = PhotoImage(file = 'peacock.gif')
        gif5 = PhotoImage(file = 'lion.gif')
        canvas.create_image(170, 100, image=gif1, anchor='nw')
        canvas.create_image(620, 150, image=gif2, anchor='center')
        canvas.create_image(1070, 100, image=gif3, anchor='ne')
        canvas.create_image(385, 300, image=gif4, anchor='nw')
        canvas.create_image(835, 300, image=gif5, anchor='ne')
if(a==1):
        gif1 = PhotoImage(file = 'tiger.gif')
        gif2 = PhotoImage(file = 'zebra.gif')
        gif3 = PhotoImage(file = 'panda.gif')
        gif4 = PhotoImage(file = 'owl.gif')
        gif5 = PhotoImage(file = 'lion.gif')
        canvas.create_image(170, 100, image=gif1, anchor='nw')
        canvas.create_image(620, 150, image=gif2, anchor='center')
        canvas.create_image(1070, 100, image=gif3, anchor='ne')
        canvas.create_image(385, 300, image=gif4, anchor='nw')
        canvas.create_image(835, 300, image=gif5, anchor='ne')
if(a==2):
        gif1 = PhotoImage(file = 'owl.gif')
        gif2 = PhotoImage(file = 'peacock.gif')
        gif3 = PhotoImage(file = 'panda.gif')
        gif4 = PhotoImage(file = 'cat.gif')
        gif5 = PhotoImage(file = 'tiger.gif')
        canvas.create_image(170, 100, image=gif1, anchor='nw')
        canvas.create_image(620, 150, image=gif2, anchor='center')
        canvas.create_image(1070, 100, image=gif3, anchor='ne')
        canvas.create_image(385, 300, image=gif4, anchor='nw')
        canvas.create_image(835, 300, image=gif5, anchor='ne')
if(a==3):
        gif1 = PhotoImage(file = 'dog.gif')
        gif2 = PhotoImage(file = 'zebra.gif')
        gif3 = PhotoImage(file = 'elephant.gif')
        gif4 = PhotoImage(file = 'cat.gif')
        gif5 = PhotoImage(file = 'lion.gif')
        canvas.create_image(170, 100, image=gif1, anchor='nw')
        canvas.create_image(620, 150, image=gif2, anchor='center')
        canvas.create_image(1070, 100, image=gif3, anchor='ne')
        canvas.create_image(385, 300, image=gif4, anchor='nw')
        canvas.create_image(835, 300, image=gif5, anchor='ne')
if(a==4):
        gif1 = PhotoImage(file = 'owl.gif')
        gif2 = PhotoImage(file = 'peacock.gif')
        gif3 = PhotoImage(file = 'tiger.gif')
        gif4 = PhotoImage(file = 'cat.gif')
        gif5 = PhotoImage(file = 'elephant.gif')
        canvas.create_image(170, 100, image=gif1, anchor='nw')
        canvas.create_image(620, 150, image=gif2, anchor='center')
        canvas.create_image(1070, 100, image=gif3, anchor='ne')
        canvas.create_image(385, 300, image=gif4, anchor='nw')
        canvas.create_image(835, 300, image=gif5, anchor='ne')
if(a==5):
        gif1 = PhotoImage(file = 'lion.gif')
        gif2 = PhotoImage(file = 'peacock.gif')
        gif3 = PhotoImage(file = 'panda.gif')
        gif4 = PhotoImage(file = 'cat.gif')
        gif5 = PhotoImage(file = 'tiger.gif')
        canvas.create_image(170, 100, image=gif1, anchor='nw')
        canvas.create_image(620, 150, image=gif2, anchor='center')
        canvas.create_image(1070, 100, image=gif3, anchor='ne')
        canvas.create_image(385, 300, image=gif4, anchor='nw')
        canvas.create_image(835, 300, image=gif5, anchor='ne')
    
B = Button(root, text="REFRESH", width=10,command=root.destroy)
B.place(x=300, y=500)
B2 = Button(root, text="CHOOSE OPTION", command=vil)
B2.place(x=500, y=500)
B3=Button(root,text="QUIT",width=10,command=root.destroy)
B3.place(x=800,y=500)
root.mainloop()




