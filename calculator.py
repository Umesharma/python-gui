from cgitb import text
from cmath import e
from logging import exception
from multiprocessing.sharedctypes import Value
import string
from tkinter import*
from tkinter import font
from turtle import left
root =Tk()
root.geometry("365x390")
root.title("calculator")
root.wm_iconbitmap("1.ico")

def click(event):
   global scval
   text=event.widget.cget("text")
   print(text)
   if text=="=":
       if scval.get().isdigit():
           Value=int(scval.get())

       else:
           try :
                value=eval(screen.get())  
           except Exception as e:
               print(e)
               scval.set("ERROR")
               screen.update()

       scval.set(value)
       screen.update()
        
   elif text=="c":
       scval.set("")
       screen.update()

   else:
       scval.set(screen.get()+text)
       screen.update()
 

def click1(event):
    text=event.widget.cget("text")
    text=("*")
    scval.set(screen.get()+text)
    screen.update()

scval=StringVar()
scval.set("")
screen=Entry(root,textvar=scval,font="lucida 45 bold")  #monospaced font for limit
screen.pack(anchor=NW)

f=Frame(root,bg="black")

b1=Button(f,text="7",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b1.pack(side=LEFT,padx=15,pady=10)
b1.bind("<Button-1>",click )


b2=Button(f,text="8",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b2.pack(side=LEFT,padx=15,pady=10)
b2.bind("<Button-1>",click )


b3=Button(f,text="9",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b3.pack(side=LEFT,padx=15,pady=10)
b3.bind("<Button-1>",click )

b4=Button(f,text="c",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b4.pack(side=LEFT,padx=15,pady=10)
b4.bind("<Button-1>",click )
f.pack(anchor=NW,padx=5)

   #second row
f=Frame(root,bg="black")

b5=Button(f,text="4",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b5.pack(side=LEFT,padx=15,pady=10)
b5.bind("<Button-1>",click )


b6=Button(f,text="5",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b6.pack(side=LEFT,padx=15,pady=10)
b6.bind("<Button-1>",click )


b7=Button(f,text="6",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b7.pack(side=LEFT,padx=15,pady=10)
b7.bind("<Button-1>",click )

b8=Button(f,text="-",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b8.pack(side=LEFT,padx=15,pady=10)
b8.bind("<Button-1>",click )

f.pack(anchor=NW,padx=5)

#third row 
f=Frame(root,bg="black")

b9=Button(f,text="1",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b9.pack(side=LEFT,padx=15,pady=10)
b9.bind("<Button-1>",click )

b10=Button(f,text="2",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b10.pack(side=LEFT,padx=15,pady=10)
b10.bind("<Button-1>",click)

b11=Button(f,text="3",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b11.pack(side=LEFT,padx=15,pady=10)
b11.bind("<Button-1>",click)

b12=Button(f,text="+",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b12.pack(side=LEFT,padx=15,pady=10)
b12.bind("<Button-1>",click )

f.pack(anchor=NW,padx=5)

#third row 
f=Frame(root,bg="black")

b13=Button(f,text=".",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b13.pack(side=LEFT,padx=15,pady=10)
b13.bind("<Button-1>",click )

b14=Button(f,text="0",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b14.pack(side=LEFT,padx=15,pady=10)
b14.bind("<Button-1>",click )

b15=Button(f,text="x",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b15.pack(side=LEFT,padx=15,pady=10)
b15.bind("<Button-1>",click1 )

b16=Button(f,text="=",fg="black",height=1,width=3,bg="#B6B6B4",font="lucida 17 bold",pady=5,padx=4,relief=RAISED)
b16.pack(side=LEFT,padx=15,pady=10)
b16.bind("<Button-1>",click)

f.pack(anchor=NW,padx=5)
 
root.mainloop()