from tkinter import *
root = Tk()
root.title("CardioVascular_Diagnose_Report")
root.geometry("600x600")
root.configure(background="gold2")

Qn1_radioButton=StringVar(value="0")

Qn1=Label(root, text =" pain or pressure in the chest ", bg = "salmon",fg= "white")
Qn1.place(relx=0.5 ,rely=0.2 ,anchor= CENTER )
Qn1_r1=Radiobutton(root, text = "yes", variable=Qn1_radioButton, value="yes",bg ="salmon")
Qn1_r1.place(relx=0.5 ,rely=0.25 ,anchor= CENTER )
Qn1_r2=Radiobutton(root, text = "no", variable=Qn1_radioButton, value="no",bg ="salmon")
Qn1_r2.place(relx=0.5 ,rely=0.3 ,anchor= CENTER )

Qn2_radioButton=StringVar(value="0")
Qn2=Label(root, text ="pain or discomfort in the arms, left",bg ="salmon",fg= "white")
Qn2.place(relx=0.5 ,rely=0.35 ,anchor= CENTER )
Qn2_r1=Radiobutton(root, text = "yes", variable=Qn2_radioButton, value="yes",bg ="salmon")
Qn2_r1.place(relx=0.5 ,rely=0.4 ,anchor= CENTER )
Qn2_r2=Radiobutton(root, text = "no", variable=Qn2_radioButton, value="no",bg ="salmon")
Qn2_r2.place(relx=0.5 ,rely=0.45 ,anchor= CENTER )

Qn3_radioButton=StringVar(value="0")
Qn3=Label(root, text ="shoulder, elbows, jaw, or back.",bg ="salmon",fg="white")
Qn3.place(relx=0.5 ,rely=0.5 ,anchor= CENTER )
Qn3_r1=Radiobutton(root, text = "yes", variable=Qn3_radioButton, value="yes",bg ="salmon")
Qn3_r1.place(relx=0.5 ,rely=0.55 ,anchor= CENTER )
Qn3_r2=Radiobutton(root, text = "no", variable=Qn3_radioButton, value="no",bg ="salmon")
Qn3_r2.place(relx=0.5 ,rely=0.60 ,anchor= CENTER )


Qn4_radioButton=StringVar(value="0")
Qn4=Label(root, text ="shortness of breath.",bg ="salmon",fg= "white")
Qn4.place(relx=0.5 ,rely=0.65 ,anchor= CENTER )
Qn4_r1=Radiobutton(root, text = "yes", variable=Qn4_radioButton, value="yes",bg ="salmon")
Qn4_r1.place(relx=0.5 ,rely=0.70 ,anchor= CENTER )
Qn4_r2=Radiobutton(root, text = "no", variable=Qn4_radioButton, value="no",bg ="salmon")
Qn4_r2.place(relx=0.5 ,rely=0.75,anchor= CENTER )

Qn5_radioButton=StringVar(value="0")
Qn5=Label(root, text ="are you dead",bg ="salmon",fg= "white")
Qn5.place(relx=0.5 ,rely=0.80,anchor= CENTER )
Qn5_r1=Radiobutton(root, text = "yes", variable=Qn5_radioButton, value="yes",bg ="salmon")
Qn5_r1.place(relx=0.5 ,rely=0.85 ,anchor= CENTER )
Qn5_r2=Radiobutton(root, text = "no", variable=Qn5_radioButton, value="no",bg ="salmon")
Qn5_r2.place(relx=0.5 ,rely=0.90 ,anchor= CENTER )

def Heart_score():
    score = 0
    if Qn1_radioButton.get()=="yes":
        score = score+10
        print(score)
    if Qn2_radioButton.get()=="yes":
        score = score+10
        print(score)
    if Qn3_radioButton.get()=="yes":
        score = score+10
        print(score)
    if Qn4_radioButton.get()=="yes":
        score = score+10
        print(score)
    if Qn5_radioButton.get()=="yes":
        score = score+100
        print(score)
        
    if score <= 10:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif  score > 10 and score <= 30: 
        messagebox.showinfo("Report","You might perhaps have to visit a doctor")
    else :
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
        
btn = Button(root, text= "click me", command= Heart_score)
btn.place(relx=0.5 ,rely=0.95 ,anchor= CENTER )

root.mainloop()
