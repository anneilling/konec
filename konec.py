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
        loo1.geometry("750x490")
        loo1.configure(bg="thistle")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo1,borderwidth=1,text="К какому классу\nотносится Змея?",font="Arial 20",bg="#c0b5ff",width=60,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo1,text="Пресмыкающиеся",height=10, width=14, font="Arial 20", fg="black", bg="mediumpurple" , variable=var,command=lomad2)
        r2=Radiobutton(loo1,text="Млекопитающие",height=10, width=15, font="Arial 20", fg="black", bg="slateblue" ,variable=var,command=ne_otvet)
        r3=Radiobutton(loo1,text="Земноводные",height=10, width=13, font="Arial 20", fg="black", bg="mediumslateblue" ,variable=var,command=ne_otvet)
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
       
    def lomad2():#второй вопрос по поводу животного
        loo1=Toplevel()
        loo1.geometry("750x490")
        loo1.configure(bg="thistle")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo1,borderwidth=1,text="Самая большая хищная рыба?",font="Arial 20",bg="#c0b5ff",width=60,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo1,text="Белая акула",height=10, width=14, font="Arial 20", fg="black", bg="mediumpurple" , variable=var,command=lomad3)
        r2=Radiobutton(loo1,text="Синий кит",height=10, width=15, font="Arial 20", fg="black", bg="slateblue" ,variable=var,command=ne_otvet)
        r3=Radiobutton(loo1,text="Косатка",height=10, width=13, font="Arial 20", fg="black", bg="mediumslateblue" ,variable=var,command=ne_otvet)
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
    def lomad3():#третий вопрос по поводу животного
        loo1=Toplevel()
        loo1.geometry("750x490")
        loo1.configure(bg="thistle")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo1,borderwidth=1,text="Какое млекопитающее умеет летать?",font="Arial 20",bg="#c0b5ff",width=60,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo1,text="Пингвин",height=10, width=14, font="Arial 20", fg="black", bg="mediumpurple" , variable=var,command=ne_otvet)
        r2=Radiobutton(loo1,text="Летучая мышь",height=10, width=15, font="Arial 20", fg="black", bg="slateblue" ,variable=var)#otvet
        r3=Radiobutton(loo1,text="Страус",height=10, width=13, font="Arial 20", fg="black", bg="mediumslateblue" ,variable=var,command=ne_otvet)
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
    def toit():#первый вопрос по поводу еды
        loo1=Toplevel()
        loo1.geometry("750x490")
        loo1.configure(bg="thistle")
        lbl=Label(loo1,borderwidth=1,text="К какому классу относится картошка?",font="Arial 20",width=60,height=10,relief="solid")
        lbl.pack()
        var=StringVar()
        var.set("Üks")
        r1=Radiobutton(loo1,text="Ягода",height=10, width=14, font="Arial 20", fg="black", bg="mediumpurple" , variable=var,command=ne_otvet)
        r2=Radiobutton(loo1,text="Фрукт",height=10, width=15, font="Arial 20", fg="black", bg="slateblue" ,variable=var,command=ne_otvet)
        r3=Radiobutton(loo1,text="Овощ",height=10, width=13, font="Arial 20", fg="black", bg="mediumslateblue" ,variable=var,command=toit2)
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
    def toit2():#второй вопрос по поводу еды
        loo1=Toplevel()
        loo1.geometry("750x490")
        loo1.configure(bg="thistle")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo1,borderwidth=1,text="Люди...",font="Arial 20",width=60,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo1,text="Травоядные",height=10, width=14, font="Arial 20", fg="black", bg="mediumpurple" , variable=var,command=ne_otvet)
        r2=Radiobutton(loo1,text="Всеядные",height=10, width=15, font="Arial 20", fg="black", bg="slateblue" ,variable=var,command=toit3)
        r3=Radiobutton(loo1,text="Плотоядные",height=10, width=13, font="Arial 20", fg="black", bg="mediumslateblue" ,variable=var,command=ne_otvet)
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
    def toit3():#третий вопрос по поводу еды
        loo4=Toplevel()
        loo4.geometry("750x490")
        loo4.configure(bg="thistle")
        var=StringVar()
        var.set("Üks")
        lbl=Label(loo4,borderwidth=1,text="В каком продукте питания\n больше всего витамина С?",font="Arial 20",width=60,height=10,relief="solid")
        lbl.pack()
        r1=Radiobutton(loo4,text="В лимонах",height=10, width=14, font="Arial 20", fg="black", bg="mediumpurple" , variable=var,value="toit",command=ne_otvet)
        r2=Radiobutton(loo4,text="В апельсинах",height=10, width=15, font="Arial 20", fg="black", bg="slateblue" ,variable=var,value="toit",command=ne_otvet)
        r3=Radiobutton(loo4,text="В сладком,\nболгарском\nперце",height=10, width=13, font="Arial 20", fg="black", bg="mediumslateblue" ,variable=var,command=otvet)
        r1.pack(side=LEFT)
        r3.pack(side=RIGHT)
        r2.pack(side=RIGHT)
    def otvet():
        okno=Toplevel()
        okno.grab_set()
        okno.geometry('500x300')
        shel=Label(okno,text=('Правильный ответ!'),height=20, width=20, font="Arial 20", fg="black", bg="red")
        shel.pack(side=TOP)
    def ne_otvet():
        okno=Toplevel()
        okno.grab_set()
        okno.geometry('500x300')
        shel=Label(okno,text=('Неправильный ответ!'),height=20, width=20, font="Arial 20", fg="black", bg="red")
        shel.pack(side=TOP)
    win=Toplevel()
    win.geometry("380x490")
    win.configure(bg="thistle")
    lbl=Label(win,borderwidth=1,text="Vali kategooria :^)\nPärast valimist arvake ära\n valitud kategooria tingimused",font="Arial 20",bg="thistle",width=40,height=10,relief="solid")
    lbl.pack()
    var=StringVar()
    var.set("Üks")
    r1=Radiobutton(win,text="Toit",height=10, width=10, font="Arial 20", fg="black", bg="orchid" , variable=var,value="Toit",command=toit)
    r2=Radiobutton(win,text="Loomad",height=10, width=10, font="Arial 20", fg="black", bg="plum" ,variable=var,value="Loomad",command=lomad)
    r1.pack(side=LEFT)
    r2.pack(side=RIGHT)

def open_win2():
    win2=Toplevel()
    win2.geometry("1400x490")
    win2.configure(bg="thistle")
    c=""
    def loe_failist():
        fail=open("File.txt",'r',encoding="utf-8-sig")
        mas=[] 
        for line in fail:
            mas.append(line.strip())
            v=line.strip().split(";") 
        fail.close()
        return mas
    mas=loe_failist()
    for a in mas:
        c+=a+"\n"
    b=Label(win2,text=(f"{c}"),height=100, width=100, font="Arial 20", fg="black", bg="lightgrey")
    b.pack()
def cmd1():
    print("Exit . . . ")
    aken.destroy() 
def cmd2():
    print("Toplevel")
    aken.command=open_win()
def cmd3():
    print("Toplevel")
    aken.command=open_win2()

okno(0,74,"V Ä L J U D A","Mediumorchid","white",cmd1)
okno(0,0,"V I K T O R I I N","Blueviolet","white", cmd2)
okno(0,37,"V A J U T A  N U P P U\n(special for Marina Oleinik c:)","Blueviolet","white", cmd3)

aken.mainloop()
