#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:24:03 2021

@author: yusuf
"""
from tkinter import *
import random

root=Tk()
root.title("yusandom")
root.geometry("400x300")
inl=Label(root)
isl=Label(root)
rpl=["shoes","pizza","burger","bbq kit","laptop","tent","flares","emergence flares","mini house","turtuga","minitureiseare","mini stuff"]



def rl():
    rL=random.randint(0,11)
    rlf=rpl[rL]
    isl["text"]="items "+str(rlf)
    print(str(rL))
    
    
btn=Button(root,text="gR",command=rl)
btn.pack()
inl.pack()
isl.pack()

root.mainloop()
