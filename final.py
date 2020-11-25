from tkinter import *
import os
top = Tk()
top.title("Game end")
canvas = Canvas(top,width=600, height=500, bg='white')canvas.pack(expand=YES, fill=BOTH)
gif1 = PhotoImage(file='win.gif')canvas.create_image(130,150,image=gif1,anchor=NW)top.configure(background="white")

b2 = Button(top,text="Exit",command=top.destroy)
b2.place(x=300,y=450)
top.mainloop()