from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import webbrowser
rule = Tk()
rule.minsize(650,650)
rule.maxsize(650,650)
rule.configure(background="gray87")
open_img = ImageTk.PhotoImage(Image.open ("open_file.png"))
save_img = ImageTk.PhotoImage(Image.open ("save_file.png"))
run_img = ImageTk.PhotoImage(Image.open ("run.png"))
lbl_file_name = Label(rule, text="File name")
lbl_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(rule)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)
my_text= Text(rule,height=35,width=80,bg = "slate gray", fg="white")
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)
rule.mainloop()
name = ""
# Define clearInputFeild() function
def openfoil ( ) :
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    text_file=filedialog.askopenfilename(title="open text file",filetypes=(("text file","*.txt"),))
    print(text_file)
    name=os.path.basename(text_file)
    formatedname=name.split('.')[0]
    input_file_name.insert(END, formatedname)
    rule.title(formatedname)
    text_file=open(name,'r')
    paragragh=text_file.read()
    my_text.insert(END,paragragh)
    text_file.close()

# Define clearTextarea() function

def savefoil ( ) :
    
    foilname=input_file_name.get()
    foil=open(foilname+".txt","w")
    data=my_text.get(1.0,END)
    print(data)
    foil.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("update","success")
    
def run_html_foil():
    global name
    webbrowser.open(name)





open_btn=Button(rule,image=open_img,text="OpenFile", command=openfoil)
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)
save_btn=Button(rule, image=save_img,text="Save File", command=savefoil)
save_btn.place(relx=0.11,rely=0.03,anchor= CENTER)
run_btn=Button(rule,image=run_img,text="Exit File", command=run_html_foil)
run_btn.place(relx=0.17,rely=0.03,anchor= CENTER)
rule.mainloop()
