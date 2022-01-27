from tkinter import *
aken=Tk()
aken.geometry("300x200")
aken.configure(bg="white")
aken.title("Viktoriin")
def okno(x,y,text,bcolor,fcolor,cmd):
    def on_enter(e):
        mybutton["background"]=bcolor
        mybutton["foreground"]=fcolor
    def on_leave(e):
        mybutton["background"]=fcolor
        mybutton["foreground"]=bcolor
    mybutton=Button(aken,width=42, height=2,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=cmd,)
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=x,y=y)
       
def open_win():
    def lomad():#первый вопрос по поводу животного
        loo1=Toplevel()
        loo1.geometry("580x490")
        loo1.configure(bg="#056f73")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo1,borderwidth=1,text="змея",font="Arial 20",width=40,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo1,text="ОТВЕТ1",height=10, width=10, font="Arial 20", fg="black", bg="#a69f9f" , variable=var,value="Loomad",command=lomad2)
        r2=Radiobutton(loo1,text="ОТВЕТ2",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="Loomad")
        r3=Radiobutton(loo1,text="ОТВЕТ3",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="Loomad")
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
       
    def lomad2():#второй вопрос по поводу животного
        loo1=Toplevel()
        loo1.geometry("580x490")
        loo1.configure(bg="#056f73")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo1,borderwidth=1,text="кот",font="Arial 20",width=40,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo1,text="ОТВЕТ1",height=10, width=10, font="Arial 20", fg="black", bg="#a69f9f" , variable=var,value="Loomad",command=lomad3)
        r2=Radiobutton(loo1,text="ОТВЕТ2",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="Loomad")
        r3=Radiobutton(loo1,text="ОТВЕТ3",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="Loomad")
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
    def lomad3():#третий вопрос по поводу животного
        loo1=Toplevel()
        loo1.geometry("580x490")
        loo1.configure(bg="#056f73")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo1,borderwidth=1,text="собака",font="Arial 20",width=40,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo1,text="ОТВЕТ1",height=10, width=10, font="Arial 20", fg="black", bg="#a69f9f" , variable=var,value="Loomad")
        r2=Radiobutton(loo1,text="ОТВЕТ2",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="Loomad")
        r3=Radiobutton(loo1,text="ОТВЕТ3",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="Loomad")
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)

    def toit():#первый вопрос по поводу еды
        loo1=Toplevel()
        loo1.geometry("580x490")
        loo1.configure(bg="#056f73")
        lbl=Label(loo1,borderwidth=1,text="бургер",font="Arial 20",width=40,height=10,relief="solid")
        lbl.pack()
        var=StringVar()
        var.set("Üks")
        r1=Radiobutton(loo1,text="ОТВЕТ1",height=10, width=10, font="Arial 20", fg="black", bg="#a69f9f" , variable=var,value="toit")
        r2=Radiobutton(loo1,text="ОТВЕТ2",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="toit")
        r3=Radiobutton(loo1,text="ОТВЕТ3",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="toit",command=toit2)
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
    def toit2():#второй вопрос по поводу еды
        loo1=Toplevel()
        loo1.geometry("580x490")
        loo1.configure(bg="#056f73")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo1,borderwidth=1,text="голова тимура",font="Arial 20",width=40,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo1,text="ОТВЕТ1.1",height=10, width=10, font="Arial 20", fg="black", bg="#a69f9f" , variable=var,value="toit")
        r2=Radiobutton(loo1,text="ОТВЕТ2.2",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="toit",command=toit3)
        r3=Radiobutton(loo1,text="ОТВЕТ3.3",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="toit")
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
    def toit3():#третий вопрос по поводу еды
        loo4=Toplevel()
        loo4.geometry("580x490")
        loo4.configure(bg="#056f73")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo4,borderwidth=1,text="суши",font="Arial 20",width=40,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo4,text="ОТВЕТ1.11",height=10, width=10, font="Arial 20", fg="black", bg="#a69f9f" , variable=var,value="toit")
        r2=Radiobutton(loo4,text="ОТВЕТ2.22",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="toit")
        r3=Radiobutton(loo4,text="ОТВЕТ33.33",height=10, width=10, font="Arial 20", fg="black", bg="#730303" ,variable=var,value="toit")
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
    win=Toplevel()
    win.geometry("380x490")
    win.configure(bg="#056f73")
    lbl=Label(win,borderwidth=1,text="Vali kategooria :^)\nPärast valimist arvake ära\n valitud kategooria tingimused",font="Arial 20",bg="thistle",width=40,height=10,relief="solid")
    lbl.pack()
    var=StringVar()
    var.set("Üks")
    r1=Radiobutton(win,text="Toit",height=10, width=10, font="Arial 20", fg="black", bg="orchid" , variable=var,value="Toit",command=toit)
    r2=Radiobutton(win,text="Loomad",height=10, width=10, font="Arial 20", fg="black", bg="plum" ,variable=var,value="Loomad",command=lomad)
    r1.pack(side=LEFT)
    r2.pack(side=RIGHT)
def cmd1():
    print("Exit . . . ")
    aken.destroy()
def cmd2():
    print("Toplevel")
    aken.command=open_win()


okno(0,0,"V I K T O R I I N","Blueviolet","white", cmd2)
okno(0,37,"V Ä L J U D A","Mediumorchid","white",cmd1)


aken.mainloop()
