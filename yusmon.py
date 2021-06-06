#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:20:48 2021

@author: Fatima
"""

from tkinter import *
from PIL import ImageTk, Image
import random

root=Tk()
root.title("Endless Pokemon Game")
root.geometry("800x600")
root.configure(background="orange")

pikachu =ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
charmender =ImageTk.PhotoImage(Image.open ("charmender.jpg"))
bulbasour =ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
squirtle =ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
ratata =ImageTk.PhotoImage(Image.open ("ratata.jpg"))
persion =ImageTk.PhotoImage(Image.open ("persion.jpg"))
paras =ImageTk.PhotoImage(Image.open ("paras.jpg"))
nidoking =ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
meowth =ImageTk.PhotoImage(Image.open ("meowth.jpg"))
kadabra =ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
jigglypuff =ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
Iyvasour =ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))
abra =ImageTk.PhotoImage(Image.open ("abra.jpg"))
charazard =ImageTk.PhotoImage(Image.open ("charmender.jpg"))
charmadar =ImageTk.PhotoImage(Image.open ("charmender.jpg"))


player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)



player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor =  CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3 , anchor =  CENTER)



player_2_score_label = Label(root , bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor =  CENTER)

apl=[charmadar,charazard,abra,Iyvasour,jigglypuff,kadabra,meowth,nidoking,paras,persion,ratata,squirtle,bulbasour,charmender,pikachu]
ap=[50,200,30,200,70,70,70-10,90,40,43,697,8954,954056879650,45654,46435]


img=ImageTk.PhotoImage(Image.open ("button.jpg"))

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0,10)
    random_pokemon = pokemon_list[random_no]
    label["image"]=random_pokemon
   
    random_power_list = power_list[random_no]
    player1_score = player1_score + random_power_list
    player_1_score_label["text"] = str( player1_score)
   
   
player_1_btn = Button(root, image = img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)

player2_score = 0
def player2():
    global player2_score
    random_no = random.randint(0,10)
    random_pokemon = pokemon_list[random_no]
    label["image"]=random_pokemon
   
    random_power_list = power_list[random_no]
    player2_score = player2_score + random_power_list
    player_2_score_label["text"] = str( player2_score)
   
   
player_2_btn = Button(root, image = img, command = player2)
player_2_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)





label = Label(root)
label.place(relx = 0.5, rely = 0.5 , anchor =  CENTER)

root.mainloop()
