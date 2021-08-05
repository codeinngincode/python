#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:03:05 2021

@author: Fatima
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
root = Tk()
root.geometry("900x500")
#----------------------------loading image------------
image = ImageTk.PhotoImage(Image.open ("image1.png"))
place_image=Label(root)
place_image["image"]=image
place_image.place(relx=0.7, rely=0.5,anchor=CENTER)
#----------------------------heading of application--------------
label = Label(root, text="Assigning Jobs", font=("French Script MT", 20, "bold"), fg="dark olive green")
label.place(relx=0.01, rely=0.06,anchor=W)

#------------------Label for string Docter-------------
label_Burgerist=Label(root,text="Burgerist : ")
label_Burgerist.place(relx=0.04, rely=0.15,anchor=CENTER)

#------------------Label for string IT professional-------------
label_IT=Label(root,text="IT professional : ")
label_IT.place(relx=0.06, rely=0.45,anchor=CENTER)

#------------------Label for string "Chemical Engineer ------------
label_chemical=Label(root,text="Chemical Engineer : ")
label_chemical.place(relx=0.07, rely=0.75,anchor=CENTER)
#---------------------entry elements--------------------------------
entry_Burgerist = Entry(root)
entry_Burgerist.place(relx=0.25, rely=0.15,anchor=CENTER)

entry_IT = Entry(root)
entry_IT.place(relx=0.25, rely=0.45,anchor=CENTER)

entry_chemical = Entry(root)
entry_chemical.place(relx=0.25, rely=0.75,anchor=CENTER)
#------------------------Labels selected--------------------------
label_selected_Burgerist=Label(root, font=("times",12,"bold"),fg="dark olive green")
label_selected_Burgerist.place(relx=0.01, rely=0.3,anchor=W)

label_selected_IT=Label(root,font=("times",12,"bold"),fg="dark olive green")
label_selected_IT.place(relx=0.01, rely=0.6,anchor=W)

label_selected_chemical=Label(root, font=("times",12,"bold"),fg="dark olive green")
label_selected_chemical.place(relx=0.01, rely=0.9,anchor=W)

class parent():
    def __init__(self):
        print("This is parent class")
        
    def Burgerist(Burgerist_name):
        
        #add Burger joint names to the below list
        Burger_joint_list = ["burger burger burger burger bbbbbbbburger","Donals","jam&bread","life&death","world tree","cosmic seed"]
        
        #edit the range for random number 0 to number of Burger joints added
        random_Burger_joint = random.randint(0,5)
        
        #edit the text to show Burgerist_name+has been alloted to + list of Burger joint names, pass the random_Burger joint inside the list
        label_selected_Burgerist['text'] = Burgerist_name+" has been alloted to "+Burger_joint_list[random_Burger_joint]
        
    def softwareEngineer(it_professional_name):
        
        #add software company names to the below list
        IT_company_list = ["IT","UST","Home is the best","play around","monjag","microsoft","apple","linux","amazon random person"]
        
        #edit the range based on number of companies given
        random_IT_company = random.randint(0,8)
        
        #edit the text it_professional_name+has been alloted to + the list of the software companies, pass random_IT_company into it
        label_selected_IT['text'] = it_professional_name+" has been alloted to "+IT_company_list[random_IT_company]
        
        
    def chemicalEngineer(chemical_engineer_name):
        
        #add chemical engineering company names to the below list
        company_list = ["laf out loud","laf inside","cola.co","pepsi.co","seven up","apple","apple by apple software comany"]
        
        #edit the range based on number of companies given
        random_company = random.randint(0,6)
        
        #edit the text chemical_engineer_name+has been alloted to+ the list name created for chem engg company, pass random_company into it
        label_selected_chemical['text'] = chemical_engineer_name+" has been alloted to "+company_list[random_company]
        
class child1(parent):
    def __init__(self):
        print("This is child1 class")
    def getBurgerist(self):
        
        #get the value from the text input entry_Burgerist and store it in the variable called name
        name = entry_Burgerist.get()
        
        #Call the function Burgerist using class called parent, pass the variable name into it
        parent.Burgerist(name)
        
class child2(parent):
    def __init__(self):
        print("This is child2 class")
    def getIT(self):
        
        #get the value from the text input entry_IT and store it in the variable called name
        name = entry_IT.get()
        
        #Call the function softwareEngineer using class called parent, pass the variable name into it
        parent.softwareEngineer(name)
        
class child3(parent):
    def __init__(self):
        print("This is child3 class")
    def getChemical(self):
        #get the value from the text input entry_chemical and store it in the variable called name
        name = entry_chemical.get()
        
        #Call the function chemicalEngineer using class called parent, pass the variable name into it
        parent.chemicalEngineer(name)


        
#create an object to access the class child1     
children=child1()
children2=child2()
children3=child3()
#create an object to access the class child2    


#create an object to access the class child3   



#call the function object1.getBurgerist when the button is clicked
btn_Burgerist = Button(root, text="Show the Burger joint alloted", command= children.getBurgerist,bg="#1763A5", fg="white",relief = FLAT)
btn_Burgerist.place(relx=0.1, rely=0.23,anchor=CENTER)

#call the function object2.getIT when the button is clicked
btn_it = Button(root, text="Show the IT company alloted", command=children2.getIT  ,bg="#1763A5", fg="white",relief = FLAT)
btn_it.place(relx=0.11, rely=0.53,anchor=CENTER)

#call the function object3.getChemical when the button is clicked
btn_chemical = Button(root, text="Show the chemical company alloted", command= children3.getChemical  , bg="#1763A5", fg="white",relief = FLAT)
btn_chemical.place(relx=0.13, rely=0.83,anchor=CENTER)
root.mainloop()
