import tkinter
from tkinter import *
from tkinter import Frame
from time import *

window=Tk()
window.title("TO-DO LİST")
window.geometry("700x500")
window.resizable(False,False)

#left frame
frame=Frame(window,width=240,height=500,bg="lightblue")
frame.place(x=0,y=0)

#task frame
frame1=Frame(window,bd=3,width=350,height=350,bg="lightblue")
frame1.place(x=285,y=150)

#CLOCK
def clock():
    text=strftime("%H:%M:%S")
    llabel.config(text=text)
    llabel.after(1000,clock)

#labels place
llabel=Label(frame,font=("ds-digital",20),background="lightpink",foreground="white")
llabel.place(x=0,y=0)
clock()

task_list=[]


def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks= taskfile.readlines()

        for task in tasks:
            #is empty?
            if task!="\n":
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open("tasklist.txt","w")
        file.close()

#adding task
def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    #searching for a ?\n
    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

#deleting tasks
def deleteTask():
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")

        listbox.delete(ANCHOR)

#cross of tasks
def cross_off_item():
    listbox.itemconfig(
        listbox.curselection(),
        fg="#dedede"  )
    listbox.select_clear(0,END)

#unceoss item
def uncross_item():
    listbox.itemconfig(
        listbox.curselection(),
        fg="white")
    listbox.select_clear(0, END)

#heading
heading=Label(window,text="ALL TASK",font="arial 30 bold",fg="white",bg="lightblue")
heading.place(x=380,y=50)

#task panel
task=StringVar()
task_entry= Entry(frame, width=100,font="arial 20",fg="lightpink",bd=0)
task_entry.place(x=0,y=150)
task_entry.focus()

#add button
btnadd=Button(frame,text="Add",font="arial 16 bold",width=15,bg="lightpink",fg="#fff",bd=0,command=addTask)
btnadd.place(x=20,y=225)

#delete button
btndelete=Button(frame,text="Delete",font="arial 16 bold",width=15,bg="lightpink",fg="#fff",bd=0,command=deleteTask)
btndelete.place(x=20,y=275)

#cross of button
cross_off_button=Button(frame,text="Cross Off",font="arial 16 bold",width=15,bg="lightpink",fg="#fff",bd=0,command=cross_off_item)
cross_off_button.place(x=20,y=325)

#uncross button
uncross_button=Button(frame,text="Uncross",font="arial 16 bold",width=15,bg="lightpink",fg="#fff",bd=0,command=uncross_item)
uncross_button.place(x=20,y=375)

#exit button
btn_exit= tkinter.Button(window,text="Exit",font="arial 16 bold",fg="white",bg="lightpink",bd=0,command=exit)
btn_exit.place(x=645,y=0)

#listbox
listbox=Listbox(frame1,font=("arial",12),width=40,height=16,bg="lightpink",fg="white",cursor="hand2",selectbackground="lightpink")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar= Scrollbar(frame1,bg="lightblue")
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
mainloop()


