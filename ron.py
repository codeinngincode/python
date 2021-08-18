#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:06:45 2021

@author: Fatima
"""
from tkinter import *
root = Tk()
root.title("Encapsulation")
root.geometry("400x400")


label_name = Label(root, text="Name: ")
label_name.place(relx=0.3,rely=0.1, anchor= CENTER)

input_name = Entry(root)
input_name.place(relx=0.6,rely=0.1, anchor= CENTER)

label_password = Label(root, text="Password: ")
label_password.place(relx=0.3,rely=0.2, anchor= CENTER)

input_password = Entry(root)
input_password.place(relx=0.6,rely=0.2, anchor= CENTER)

label_captcha = Label(root, text="Captcha: ")
label_captcha.place(relx=0.3,rely=0.3, anchor= CENTER)

input_captcha = Entry(root)
input_captcha.place(relx=0.6,rely=0.3, anchor= CENTER)

label_show_name = Label(root)
label_show_name.place(relx=0.5,rely=0.7, anchor= CENTER)

label_show_password = Label(root)
label_show_password.place(relx=0.5,rely=0.8, anchor= CENTER)

label_show_captcha = Label(root)
label_show_captcha.place(relx=0.5,rely=0.9, anchor= CENTER)


class userDB():
    def __init__(self):
        ##create a private variable named username, assign a name inside it
        self.__username  = "yusuf"
        
        ##create a private variable named password, assign a value inside it
        self.__password = "koki"
        
        #create a normal variable called captcha and give some random letters inside it
        self.captcha = "87i9"
        
        
    def showUser(self):
        ##show the private variable username on the label label_show_name
        label_show_name["text"] = "Name : "+self.__username
        
        ##show the private variable password on the label label_show_password
        label_show_password["text"] = "Password : "+self.__password
        ##show the variable captcha on the label label_show_captcha
        label_show_captcha["text"] = "captcha "+self.captcha
        
        
##create an object named user and for the class userDB()        
user=userDB()


def addUser():
    global user
    
    ##get the value from text input named input_name and store it in the variable username, access it using the object
    user.username = input_name.get()
    
    ##get the value from text input named input_password and store it in the variable password, access it using the object
    user.password = input_password.get()
    ##get the value from text input named input_captcha and store it in the variable captcha, access it using the object
    user.captcha = input_captcha.get()
    
    print("Details Updated")
btn = Button(root, text="Update Login Details", command=addUser)
btn.place(relx=0.3,rely=0.5, anchor= CENTER)
btn = Button(root, text="Show Profile", command=user.showUser)
btn.place(relx=0.7,rely=0.5, anchor= CENTER)
root.mainloop()
