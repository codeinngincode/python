from tkinter import *
root=Tk()
root.title("yusanbanaci")
root.geometry("800x600")
label_1=Label(root,text="yusanaci series : ")
label_2=Label(root,text="yusanaci sum" )
label_spirl=Label(root)
enter_no = Entry(root)    

def teranci():
    inputno=int(enter_no.get())
    firstnum=0
    secnum=1
    sum=0
    sum2=0
    counter=1
    while(counter<=inputno):
        label_1["text"]+=str(sum)+" "
        label_2["text"]="yuanaci sum:"+str(sum2)
        counter=counter+1
        firstnum=secnum
        secnum=sum
        sum=firstnum+secnum
        sum2=sum2+sum
       
btn=Button(root,text="show yusanaci series",command=teranci)
btn.pack()
enter_no.pack()    
label_2.pack()
label_1.pack()


root.mainloop()