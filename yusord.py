#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:24:03 2021
@author: Fatima
"""
from tkinter import *
import random

root=Tk()
root.title("yusuky")
root.geometry("400x300")
wL=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print("sorry but i did not understant what text paramerter meant so it will be in console but you still had to press the button")




def rl():
    rN1=random.randint(0,25)
    rN2=random.randint(0,25)
    rN3=random.randint(0,25)
    rN4=random.randint(0,25)
    rN5=random.randint(0,25)
    random_alpha1=wL[rN1]
    random_alpha2=wL[rN2]
    random_alpha3=wL[rN3]
    random_alpha4=wL[rN4]
    random_alpha5=wL[rN5]
    rlf=random_alpha1+random_alpha2+random_alpha3+random_alpha4+random_alpha5
    print("your lucky word is : "+rlf)

    
btn=Button(root,text="gR",command=rl)
btn.pack()



root.mainloop()
