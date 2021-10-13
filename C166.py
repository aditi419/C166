from tkinter import *
from tkinter import Entry
from PIL import ImageTk,Image
root=Tk()
root.title("C166")
root.geometry('600x600')

color_label = Label(root,text='Enter a color')
color_label.place(root,relx=0.8,rely=0.9,anchor=CENTER)

input_box = Entry(root)
input_box.insert(0,'black')
input_box.place(root,relx=0.6,rely=0.9,anchor=CENTER)

canvas = Canvas(root,width=600,height=500,bg=white,highlightbackground='blue')
canvas.pack()

img = ImageTk.PhotoImage(Image.open('start_point1.png'))
my_image = canvas.create_image(50,50,image=img)

direction = ''
oldx = 50
oldy = 50
newx = 50
newy = 50

def draw(direction,oldx,oldy,newx,newy):
    fill_color = input_box.get()
    
root.bind('<Up>',up_dir)
root.bind('<Down>',down_dir)
root.bind('<Left>',left_dir)
root.bind('<Right>',right_dir)
    
root.mainloop()




