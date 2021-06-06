
from tkinter import *
import random

root=Tk()
root.title("Color Dictionary")
root.geometry("600x400")

dictionary = {"colour" : ["firebrick 4","navy","sandy brown","indian red","turquoise4","gold4","cyan"]}

def randomColor():
    random_no =random.randint(0,7)
    print(dic["colour"][random_no])
    root.configure(background = dictionary["colour"][random_no])
    
btn = Button(root,text = "click me", command = randomColor)
btn.pack()

root.mainloop()
