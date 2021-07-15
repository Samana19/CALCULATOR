from tkinter import*

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()

root=Tk()

#assigning title and icon
root.title('My calculator')
root.geometry("600x900")
root.iconbitmap('Calculator.ico')

#setting the entry screen
scvalue=StringVar()
scvalue.set("")

screen=Entry(root,width=50,fg="black", bg="white",borderwidth=20, text=scvalue, font=" Helvetica 40 bold")
screen.pack(padx=70, pady=10)

#Frames and buttons

frame=Frame(root,highlightbackground="grey", highlightthickness=5,bg="black")

button=Button(frame,text='C',bg='gray67',fg='black' ,font="Helvetica 32",padx=13,pady=5)
button.pack(side=LEFT,padx=9,pady=10)
button.bind("<Button-1>",click)


button=Button(frame,text='**',bg='gray67',fg='black' ,font="Helvetica 32",padx=12,pady=5)
button.pack(side=LEFT,padx=9,pady=10)
button.bind("<Button-1>",click)

button=Button(frame,text='%',bg='gray67',fg='black' ,font="Helvetica 32",padx=12,pady=5)
button.pack(side=LEFT,padx=9,pady=10)
button.bind("<Button-1>",click)

button=Button(frame,text='/',bg='DarkGoldenrod1',fg='white' ,font="Helvetica 32",padx=22,pady=5)
button.pack(side=LEFT,padx=9,pady=10)
button.bind("<Button-1>",click)

frame.pack()

frame=Frame(root,highlightbackground="grey", highlightthickness=5,bg="black")

button=Button(frame,text='7',bg='gray25',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='8',bg='gray25',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='9',bg='gray25',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='*',bg='DarkGoldenrod1',fg='white' ,font="Helvetica 35",padx=15,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)


frame.pack()

frame=Frame(root,highlightbackground="grey", highlightthickness=5,bg="black")

button=Button(frame,text='4',bg='gray25',fg='white' ,font="Helvetica 35",padx=13,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='5',bg='gray25',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='6',bg='gray25',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='-',bg='DarkGoldenrod1',fg='white' ,font="Helvetica 35",padx=13.25,pady=5)
button.pack(side=LEFT,padx=14,pady=18)
button.bind("<Button-1>",click)

frame.pack()

frame=Frame(root,highlightbackground="grey", highlightthickness=5,bg="black")

button=Button(frame,text='1',bg='gray25',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='2',bg='gray25',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='3',bg='gray25',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='+',bg='DarkGoldenrod1',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=11,pady=16)
button.bind("<Button-1>",click)

frame.pack()
frame=Frame(root,highlightbackground="grey", highlightthickness=5,bg="black")

button=Button(frame,text='0',bg='gray25',fg='white' ,font="Helvetica 35",padx=66,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='.',bg='gray25',fg='white' ,font="Helvetica 35",padx=20,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

button=Button(frame,text='=',bg='DarkGoldenrod1',fg='white' ,font="Helvetica 35",padx=12,pady=5)
button.pack(side=LEFT,padx=12,pady=18)
button.bind("<Button-1>",click)

frame.pack()


root.config(bg="black") #window background color
root.mainloop()
