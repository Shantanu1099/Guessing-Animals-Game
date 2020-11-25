from tkinter import *
import os
top = Tk()
top.title("Game")
canvas = Canvas(top,width=600, height=500, bg='white')canvas.pack(expand=YES, fill=BOTH)
def abc():
	os.system('program_image.py')

gif1 = PhotoImage(file='gamesbannerTile_tcm1404258086.gif')canvas.create_image(130,150,image=gif1,anchor=NW)top.configure(background="white")
b1 = Button(top,text="Play",command=abc)
b1.place(x=200,y=450)
b2 = Button(top,text="Exit",command=top.destroy)
b2.place(x=400,y=450)
top.mainloop()