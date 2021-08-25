#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 19:11:20 2021

@author: Fatima
"""

from tkinter import *
import random
root = Tk()
root.title("Encapsulation")
root.geometry("500x400")
root.config(bg="white")
label_score = Label(root, text="Score : 0",font=("Bahnschrift Light",15,"bold") ,bg="white")
label_score.place(relx=0.1,rely=0.1, anchor= CENTER)
label_name = Label(root,font=("Arial",40),bg="white")
label_name.place(relx=0.5,rely=0.3, anchor= CENTER)
input_value = Entry(root)
input_value.place(relx=0.5,rely=0.5, anchor= CENTER)

#define a class named game
class game:
    #define an init function, pass the method self to it
    def __init__(self):
        #assign value 0 to the private variable score
        self.__score=0
        
    def updateGame(self):
         #assign some values with color names to the list named text of the methid self 
        self.text = ["white","red","green","yellow","blue","pink","black"]

        #generate random number between 0 and 5 (if 5 colors are mentioned above) and assign it to self.random_number_for_text
        self.random_number_for_text=random.randint(0, 6)
        #assign some values with color names to the list named self.color 
        self.color=["white","red","green","yellow","blue","pink","black"]
        ##generate random number between 0 and 5 (if 5 colors are mentioned above) and assign it to self.random_number_for_color
        self.random_number_for_color=random.randint(1, 6)
        #show the value of list self.text according to the random_number_for_text on the label_name
        label_name["text"] =  self.text[self.random_number_for_text]
        
        #show the foreground color of label from the list self.color according to the random_number_for_color
        label_name["fg"] = self.color[self.random_number_for_color]

   #define the private function __update_score, pass self and input_value to it.
    def __update_score(self, input_value):
        
        #write an if condition to check if the input_value is equal to the List's(self.color) index value(self.random_number_for_color)
        if(input_value==self.color[random_number_for_color]):
            print(self.color[self.random_number_for_color])
            
            #update the private variable __score by adding random number(0,10) to it
            self.__score = self.__score + random.randint(1, 10)
            
            #display the private variable self.__score on the label_score, including string conversion
            label_score["text"] = "Score : "+str(self.__score)
            
            
    def get_user_value(self, input_value):
        #access the private function self.__update_score, pass the variable input_value to it
        self.__update_score(input_value)


#define an object for the class game
bored=game()

def getInput():
    ##get the color value from the input_value and assign it to the variable value
    value = input_value.get()
    #call the function get_user_value, pass the variable value into it
    bored.get_user_value(value)
    
    #call the function updateGame
    bored.updateGame()
    #clear the text inout "input_value" to keep it empty for next entry using delete()
    input_value.delete(0,END)

#call the function getInput for the button click
btn = Button(root, text="CHECK" ,command=getInput, bg="IndianRed1", fg="white", relief=FLAT,  padx=10, pady=1,  font=("Arial",15))
btn.place(relx=0.35,rely=0.65, anchor= CENTER)

#call the function updateGame for the button click
btn = Button(root, text="START" ,command=bored.updateGame , bg="dark olive green", fg="white", relief=FLAT,  padx=10, pady=1,  font=("Arial",15))
btn.place(relx=0.65,rely=0.65, anchor= CENTER)
root.mainloop()
