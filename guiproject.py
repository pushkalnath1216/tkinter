from tkinter import *
window=Tk()
window.title('MY PYTHON PROJECT')


lbl=Label(window,text='LIBRARY MANAGEMENT',font=('ARIAL BLACK',25))
lbl.grid(column=2,row=0)

lbl1=Label(window,text='STUDENT INFO')
lbl1.grid(column=0,row=1)

lbl1=Label(window,text='BOOK INFO')
lbl1.grid(column=3,row=1)

lbl2=Label(window,text='NAME')
lbl2.grid(column=0,row=2)
txt2=Entry(window,width=15)
txt2.grid(column=1,row=2)

lbl3=Label(window,text='REG.NO')
lbl3.grid(column=0,row=3)
txt3=Entry(window,width=15)
txt3.grid(column=1,row=3)

lbl4=Label(window,text='DEPARTMENT')
lbl4.grid(column=0,row=4)
txt4=Entry(window,width=15)
txt4.grid(column=1,row=4)

lbl5=Label(window,text='YEAR')
lbl5.grid(column=0,row=5)
txt5=Entry(window,width=15)
txt5.grid(column=1,row=5)

lbl6=Label(window,text='LIBRARY ROLL')
lbl6.grid(column=0,row=6)
txt6=Entry(window,width=15)
txt6.grid(column=1,row=6)

lbl7=Label(window,text='DUES')
lbl7.grid(column=0,row=7)
txt7=Entry(window,width=15)
txt7.grid(column=1,row=7)

lbl8=Label(window,text='BOOK NAME')
lbl8.grid(column=2,row=2)
txt8=Entry(window,width=15)
txt8.grid(column=3,row=2)

lbl9=Label(window,text='PUBLISHER')
lbl9.grid(column=2,row=3)
txt9=Entry(window,width=15)
txt9.grid(column=3,row=3)

lbl10=Label(window,text='EDITION')
lbl10.grid(column=2,row=4)
txt10=Entry(window,width=15)
txt10.grid(column=3,row=4)

lbl11=Label(window,text='DEPARTMENT')
lbl11.grid(column=2,row=5)
txt11=Entry(window,width=15)
txt11.grid(column=3,row=5)

lbl12=Label(window,text='ISSUE DATE')
lbl12.grid(column=2,row=6)
txt12=Entry(window,width=15)
txt12.grid(column=3,row=6)

lbl13=Label(window,text='RETURN DATE')
lbl13.grid(column=2,row=7)
txt13=Entry(window,width=15)
txt13.grid(column=3,row=7)


def clicked():
    res2=txt2.get()
    res3=txt3.get()
    res4=txt4.get()
    res5=txt5.get()
    res6=txt6.get()
    res7=txt7.get()
    label2=Label(window,text=res2).grid(column=0,row=11)
    label3=Label(window,text=res3).grid(column=0,row=12)
    label4=Label(window,text=res4).grid(column=0,row=13)
    label5=Label(window,text=res5).grid(column=0,row=14)
    label6=Label(window,text=res6).grid(column=0,row=15)
    label7=Label(window,text=res7).grid(column=0,row=16)

    res8=txt8.get()
    res9=txt9.get()
    res10=txt10.get()
    res11=txt11.get()
    res12=txt12.get()
    res13=txt13.get()
    label8=Label(window,text=res8).grid(column=3,row=11)
    label9=Label(window,text=res9).grid(column=3,row=12)
    label10=Label(window,text=res10).grid(column=3,row=13)
    label11=Label(window,text=res11).grid(column=3,row=14)
    label12=Label(window,text=res12).grid(column=3,row=15)
    label13=Label(window,text=res13).grid(column=3,row=16)
    
    
    
    Lbl=Label(window,text='hello')
    Lbl.grid(column=2,row=9)
    Lbl.configure(text='submitted')
BTN=Button(window,text='SUBMIT',command=clicked)
BTN.grid(column=2,row=9)
def clicked():
    lBl3=Label(window,text='hello')
    lBl3.grid(column=3,row=9)
    lBl3.configure(text='Nothing to do with this...Enter other entries')
BTN1=Button(window,text='CANCEL',command=clicked)
BTN1.grid(column=2,row=10)


window.mainloop()
