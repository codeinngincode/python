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
fl=Label(root)
fl.pack()
fl1=Label(root)
fl1.pack()
rnl=Label(root)
lf=Label(root)
lf.pack()
lf1=Label(root)
lf1.pack()
rnl.pack()
en=Entry(root)
en.pack()
en1=Entry(root)
en1.pack()
wL=[""]
cn=[""]



def af():
    fn=en.get()
    fn1=en1.get()
    wL.append(fn)
    cl.append(fn1)
    fl["text"]="your contry list : "+str(wL)
    fl1["text"]="your city list : "+str(cl)
    
    


def rl():
    l=len(wL)
    rn=random.randint(0,l-1)
    rnl["text"]=str(rn)
    grn=wL[rn]
    grn1=cl[rn]
    lf["text"]="r contry is : "+str(grn)
    lf["text"]="r city is : "+str(grn1)
btnw=Button(root,text="fa",command=af)
btnw.pack()

    
btn=Button(root,text="gR",command=rl)
btn.pack()



root.mainloop()
