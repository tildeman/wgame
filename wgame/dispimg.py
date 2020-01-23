import tkinter
import _tkinter
import time
def display(imgdir,cans,hint,rnum='__test__'):
    global res,r
    res=None
    r=None
    t=tkinter.Tk()
    lim=time.time()+16
    n=tkinter.IntVar()
    rn=tkinter.Label(t,text='Round: '+str(rnum),font=('Arial Black',20))
    rn.grid(row=0,column=0,sticky=tkinter.W)
    tl=tkinter.Label(t,textvariable=n,font=('Arial Black',20))
    tl.grid(row=0,column=1)
    i=tkinter.PhotoImage(file=imgdir)
    l=tkinter.Label(t,image=i)
    sv=tkinter.StringVar()
    hl=tkinter.Label(t,font=('Arial Black',20),textvariable=sv)
    hl.grid(row=1,columnspan=2)
    l.image=i
    l.grid(row=2,column=0,columnspan=2)
    box=tkinter.Entry(t,font=('Arial Black',20))
    box.grid(column=0,row=3,sticky=tkinter.W)
    def dest():
        global res,r
        res=box.get()
        r=res.lower()==cans
        if r:
            box.config(fg='#008000')
        else:
            box.config(fg='#ff0000')
            sv.set(hint)
        t.update()
        time.sleep(1)
        box.config(fg='#000000')
        if r:t.destroy()
    def fdest():
        s.config(state=tkinter.DISABLED)
        box.config(state=tkinter.DISABLED)
        rn.config(text='Time\'s up!',fg='#ff0000')
        t.update()
    s=tkinter.Button(t,command=dest,text='OK',font=('Arial Black',20),padx=0,pady=0)
    s.grid(column=1,row=3)
    n.set(15)
    while n.get()!=0:
        n.set(int(lim-time.time()))
        try:
            t.update()
        except _tkinter.TclError:
            return int(bool(r))
    fdest()
    t.mainloop()
if __name__=='__main__':
    print(display('__test__\\cow.gif','cow',':|'))
