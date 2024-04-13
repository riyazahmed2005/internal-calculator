import customtkinter as ctk
from tkinter import messagebox
w=ctk.CTk()
global ssa1,pt1,ssa2,sa1,fa1,ssa3var,pt2,ssa4var,sa2,fa2,namevar,rollvar
ssa1var=ctk.StringVar()
pt1=ctk.StringVar()
ssa2var=ctk.StringVar()
sa1=ctk.StringVar()
fa1=ctk.StringVar()
ssa3var=ctk.StringVar()
pt2=ctk.StringVar()
ssa4var=ctk.StringVar()
sa2=ctk.StringVar()
fa2=ctk.StringVar()
namevar=ctk.StringVar()
rollvar=ctk.StringVar()
def window():
    w.title('Internal calculator')
    w.geometry('1300x800+0+0')
    w.resizable(False,False)
    w._set_appearance_mode('Dark')
def calculate():
    n1=ssa1var.get()
    n2=ssa2var.get()
    n3=pt1.get()
    n4=sa1.get()
    n5=fa1.get()
    n6=ssa3var.get()
    n7=ssa4var.get()
    n8=pt2.get()
    n9=sa2.get()
    n10=fa2.get()
    n11=namevar.get()
    n12=rollvar.get()
    if(n1=="" or n2=="" or n3=="" or n4=="" or n5=="" or n6=="" or n7=="" or n8=="" or n9=="" or n10=="" or n11=="" or n12==""):
        messagebox.showerror('invalid','enter all details')
    elif(float(n1)<0 or float(n2)<0 or float(n3)<0 or float(n4)<0 or float(n5)<0 or float(n6)<0 or float(n7)<0 or float(n8)<0 or float(n9)<0 or float(n10)<0 ):
        messagebox.showerror('invalid','enter +ve numbers')
    elif(float(n1)>20 or float(n2)>20 or float(n3)>50 or float(n4)>100 or float(n5)>40 or float(n6)>20 or float(n7)>20 or float(n8)>50 or float(n9)>100 or float(n10)>40):
        messagebox.showerror('error','Enter the number in range')
    else:
        newssa1=(float(n1)/20)*1
        newpt1=(float(n3)/50)*2
        newssa2=(float(n2)/20)*1
        newsa1=(float(n4)/100)*8
        newfa1=(float(n5)/40)*8
        rel=newssa1+newpt1+newssa2+newsa1+newfa1
        newrel='{:.3f}'.format(rel)
        #result_out.configure(text=str(newrel))
        newssa3=(float(n6)/20)*1
        newpt2=(float(n8)/50)*2
        newssa4=(float(n7)/20)*1
        newsa2=(float(n9)/100)*8
        newfa2=(float(n10)/40)*8
        rel2=newssa3+newpt2+newssa4+newsa2+newfa2
        newrel2='{:.3f}'.format(rel2)
        TOT=rel+rel2
        newTOT='{:.2f}'.format(TOT)
        l1=str(newrel)
        l2=str(newrel2)
        result_out.configure(text=l1)
        result2_out.configure(text=l2)
        total_out.configure(text=str(newTOT))
        #result2_out.configure(text=str(newrel))
def design1():
    #heading
    global ssa1_entry,PT_entry,ssa2_entry,cia1_entry,fa1_entry,result_out,name_entry,roll_entry
    head=ctk.CTkLabel(w,text='Internal calculator',text_color='blue',font=('impact',40))
    head.place(x=490,y=30)
    #name lable
    name=ctk.CTkLabel(w,text='Name :',text_color='white',font=('microsoft yahi ui light',20,'bold'))
    name.place(x=100,y=140)
    #name entry
    name_entry=ctk.CTkEntry(w,border_width=1,width=200,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=namevar)
    name_entry.place(x=200,y=140)
     # rollnumber
    roll=ctk.CTkLabel(w,text='Roll :',text_color='white',font=('microsoft yahi ui light',20,'bold'))
    roll.place(x=490,y=140)
    # rollnumber entry
    roll_entry=ctk.CTkEntry(w,border_width=1,width=190,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=rollvar)
    roll_entry.place(x=590,y=140)
    #lable1
    ssa1=ctk.CTkLabel(w,text='SSA 1:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    ssa1.place(x=100,y=230)
    #entry
    ssa1_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=ssa1var)
    ssa1_entry.place(x=200,y=229)
    #lable1
    ssa1_out=ctk.CTkLabel(w,text='/ 20',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    ssa1_out.place(x=370,y=230)
    #lable2
    PT=ctk.CTkLabel(w,text='PT 1:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    PT.place(x=100,y=310)
    #entry 2
    PT_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=pt1)
    PT_entry.place(x=200,y=310)
    #lable2 
    PT_out=ctk.CTkLabel(w,text='/ 50',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    PT_out.place(x=370,y=310)
    #lable3
    ssa2=ctk.CTkLabel(w,text='SSA 2:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    ssa2.place(x=100,y=390)
    #entry 3
    ssa2_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=ssa2var)
    ssa2_entry.place(x=200,y=390)
    #lable 3
    ssa2_out=ctk.CTkLabel(w,text='/ 20',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    ssa2_out.place(x=370,y=390)
    #lable 4
    cia1=ctk.CTkLabel(w,text='SA 1:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    cia1.place(x=100,y=470)
    #entry 4
    cia1_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=sa1)
    cia1_entry.place(x=200,y=470)
    #lable 4
    cia1_out=ctk.CTkLabel(w,text='/ 100',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    cia1_out.place(x=370,y=470)
    # lable 5
    FA1=ctk.CTkLabel(w,text='FA 1:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    FA1.place(x=100,y=550)
    # entry 5
    fa1_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=fa1)
    fa1_entry.place(x=200,y=550)
    #lable 5
    fa1_out=ctk.CTkLabel(w,text='/ 40',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    fa1_out.place(x=370,y=550)
def design2():
    #heading
    global ssa3_entry,PT2_entry,ssa4_entry,cia2_entry,fa2_entry,result_out,result2_out,total_out
    #lable1
    ssa3=ctk.CTkLabel(w,text='SSA 3:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    ssa3.place(x=600,y=230)
    #entry1
    ssa3_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=ssa3var)
    ssa3_entry.place(x=700,y=230)
    #lable1
    ssa3_out=ctk.CTkLabel(w,text='/ 20',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    ssa3_out.place(x=870,y=230)
    #lable2
    PT2=ctk.CTkLabel(w,text='PT 2:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    PT2.place(x=600,y=310)
    # #entry 2
    PT2_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=pt2)
    PT2_entry.place(x=700,y=310)
    # #lable2 
    PT_out=ctk.CTkLabel(w,text='/ 50',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    PT_out.place(x=870,y=310)
    # #lable3
    ssa4=ctk.CTkLabel(w,text='SSA 4:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    ssa4.place(x=600,y=390)
    # #entry 3
    ssa4_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=ssa4var)
    ssa4_entry.place(x=700,y=390)
    # #lable 3
    ssa2_out=ctk.CTkLabel(w,text='/ 20',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    ssa2_out.place(x=870,y=390)
    # #lable 4
    cia2=ctk.CTkLabel(w,text='SA 2:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    cia2.place(x=600,y=470)
    # #entry 4
    cia2_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=sa2)
    cia2_entry.place(x=700,y=470)
    # #lable 4
    cia2_out=ctk.CTkLabel(w,text='/ 100',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    cia2_out.place(x=870,y=470)
    # # lable 5
    FA2=ctk.CTkLabel(w,text='FA 2:',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    FA2.place(x=600,y=550)
    # # entry 5
    fa2_entry=ctk.CTkEntry(w,border_width=1,width=140,height=30,font=('microsoft yahi ui light',16,'bold'),textvariable=fa2)
    fa2_entry.place(x=700,y=550)
    # #lable 5
    fa2_out=ctk.CTkLabel(w,text='/ 40',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    fa2_out.place(x=870,y=550)
    # #result
    result1=ctk.CTkLabel(w,text='CIA 1:',text_color='lightgreen',font=('microsoft yahi ui light',20,'bold'))
    result1.place(x=1000,y=230)
    #result entry
    result_out=ctk.CTkLabel(w,text="",text_color='white',font=('microsoft yahi ui light',20,'bold'),width=140,height=30)
    result_out.place(x=1100,y=230)
    # result 2
    result2=ctk.CTkLabel(w,text='CIA 2:',text_color='lightgreen',font=('microsoft yahi ui light',20,'bold'))
    result2.place(x=1000,y=330)
    #result entry
    result2_out=ctk.CTkLabel(w,text="",text_color='white',font=('microsoft yahi ui light',20,'bold'),width=140,height=30)
    result2_out.place(x=1100,y=330)
    #grand total
    total=ctk.CTkLabel(w,text="Total",text_color='white',font=('microsoft yahi ui light',20,'bold'),width=140,height=30)
    total.place(x=950,y=420)
    #grand total
    total_out=ctk.CTkLabel(w,text="",text_color='white',font=('microsoft yahi ui light',20,'bold'),width=140,height=30)
    total_out.place(x=1100,y=420)

    out_total=ctk.CTkLabel(w,text='/ 40',text_color='orange',font=('microsoft yahi ui light',20,'bold'))
    out_total.place(x=1200,y=420)
     # calculate button
    button=ctk.CTkButton(w,text='Calculate',text_color='white',fg_color='green',width=140,height=40,font=('microsoft yahi ui light',20,'bold'),hover=True,hover_color=('green','black'),command=calculate)
    button.place(x=1050,y=560)
    w.mainloop()
window()
design1()
design2()