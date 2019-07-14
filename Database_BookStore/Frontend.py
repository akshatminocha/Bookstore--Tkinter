from Backend import Database as db
from tkinter import *


d=db("Book.db")

#d.connection("Book.db")
def view_all():
    list.delete(0,END)
    for row in d.view_data():
        list.insert(END,row)
def search_entry():
    list.delete(0,END)
    for row in d.search_data(entry_1_val.get(),entry_2_val.get(),entry_3_val.get(),entry_4_val.get()):
        list.insert(END,row)
def add_entry():
    d.insert_data(entry_1_val.get(),entry_2_val.get(),entry_3_val.get(),entry_4_val.get())
    list.delete(0,END)
    list.insert(END,(entry_1_val.get(),entry_2_val.get(),entry_3_val.get(),entry_4_val.get()))
def get_selected_row(event):
    global selected_data
    index=list.curselection()[0]
    selected_data=list.get(index)
    entry_1.delete(0,END)
    entry_1.insert(END,selected_data[1])
    entry_2.delete(0,END)
    entry_2.insert(END,selected_data[2])
    entry_3.delete(0,END)
    entry_3.insert(END,selected_data[3])
    entry_4.delete(0,END)
    entry_4.insert(END,selected_data[4])
def delete_selected():
    id=selected_data[0]
    d.delete_data(id)
def update_selected():
    id=selected_data[0]
    d.update_data(id,entry_1_val.get(),entry_2_val.get(),entry_3_val.get(),entry_4_val.get())            
                    
#t=Text(root)
#t.grid(row=3,column=0)
root=Tk()
root.wm_title('BookStore')
root.configure(bg='lemon chiffon')

label_1=Label(root,text="Title",font='Times 14 bold',fg='SkyBlue4',bg='lemon chiffon')      
label_2=Label(root,text="Author",font='Times 14 bold',fg='SkyBlue4',bg='lemon chiffon')
label_1.grid(row=0,column=0)
label_2.grid(row=1,column=0)

entry_1_val=StringVar()
entry_1=Entry(root,bg='gray88',bd=2,relief='ridge',font='Ariel 12 bold',fg='gray36',selectbackground='gray6',textvariable=entry_1_val)
entry_2_val=StringVar()
entry_2=Entry(root,bg='gray88',bd=2,relief='ridge',font='Ariel 12 bold',fg='gray36',selectbackground='gray6',textvariable=entry_2_val)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

#s=Scrollbar(root)
        #self.a=t.Text(self.m,height=6,width=20)
#s.pack()

#t.pack(side=LEFT,fill=Y)
#s.config(command=t.yview)
#t.config(yscrollcommand=s.set)
        #self.a.grid(row=3,column=0,columnspan=2)

label_3=Label(root,text="Year",font='Times 14 bold',fg='SkyBlue4',bg='lemon chiffon')
label_4=Label(root,text="ISBN",font='Times 14 bold',fg='SkyBlue4',bg='lemon chiffon')
label_3.grid(row=0,column=3)
label_4.grid(row=1,column=3)

entry_3_val=StringVar()
entry_3=Entry(root,bg='gray88',bd=2,relief='ridge',font='Ariel 12 bold',fg='gray36',selectbackground='gray6',textvariable=entry_3_val)
entry_4_val=StringVar()
entry_4=Entry(root,bg='gray88',bd=2,relief='ridge',font='Ariel 12 bold',fg='gray36',selectbackground='gray6',textvariable=entry_4_val)
entry_3.grid(row=0,column=4)
entry_4.grid(row=1,column=4)

#entry=Entry(root)
#entry.grid(columnspan=3,padx=40,pady=20)

list=Listbox(root,height=8,width=40,bd=5,bg='bisque3',fg='saddle brown',font='Times 16 bold',selectbackground='indian red',selectborderwidth=2)
list.grid(row=2,column=0,rowspan=6,columnspan=2)
sb=Scrollbar(root)
sb.grid(row=2,column=2,rowspan=6)
list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)
list.bind('<<ListboxSelect>>',get_selected_row)

button1=Button(root,text="View all",height=1,width=16,bd=4,relief='raised',bg='cyan4',fg='PaleTurquoise1',font='Times 14 bold italic',cursor='dot',command=view_all)
button1.grid(row=2,column=4,sticky=E)
button2=Button(root,text="Search entry",height=1,width=16,bd=4,relief='raised',bg='PaleTurquoise1',fg='cyan4',font='Times 14 bold italic',cursor='dot',command=search_entry)
button2.grid(row=3,column=4,sticky=E)
button3=Button(root,text="Add entry",height=1,width=16,bd=4,relief='raised',bg='cyan4',fg='PaleTurquoise1',font='Times 14 bold italic',cursor='dot',command=add_entry)
button3.grid(row=4,column=4,sticky=E)
button4=Button(root,text="Update selected",height=1,width=16,bd=4,relief='raised',bg='PaleTurquoise1',fg='cyan4',font='Times 14 bold italic',cursor='dot',command=update_selected)
button4.grid(row=5,column=4,sticky=E)
button5=Button(root,text="Delete selected",height=1,width=16,bd=4,relief='raised',bg='cyan4',fg='PaleTurquoise1',font='Times 14 bold italic',cursor='dot',command=delete_selected)
button5.grid(row=6,column=4,sticky=E)


root.mainloop()