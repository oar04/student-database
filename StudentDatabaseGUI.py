from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
##import tkinter.font
##import tkinter.messagebox
#from hyperlink import URL
##from tkinter import *
import studDB



#        *************************************
#        **************FUNCTIONS**************
#        *************************************


def viewAll():
    records = studDB.View()
    print(records)
    clearTree()
    for row in records:
        tv.insert("", 0, values=row)

    msgData="Viewing Student Record"
    msgFrame = LabelFrame(win, text='Message Panel:')
    msgFrame.configure(background='Pink')   
    msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8, )
    msg = Label(msgFrame,text=(msgData), fg='red')
    msg.grid(row=0, column=0, padx=8)
        

def Delete():
    selected_item = tv.selection()[0]
    id = studID_field.get()
    studDB.Delete(id)
    tv.delete(selected_item)

    msgData="Selected Student Has Been Deleted"
    msgFrame = LabelFrame(win, text='Message Panel:')   
    msgFrame.configure(background='Pink')
    msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8, )
    msg = Label(msgFrame,text=(msgData), fg='red')
    msg.grid(row=0, column=0, padx=8)


    

def Update():
    if len(studName_field.get() and studSurname_field.get() and studgrade_field.get() and studImgLoc_field.get()) == 0:

        msgData="Please Fill All \n Fields In The Form \n To Update This \nStudent's Details"
        msgFrame = LabelFrame(win, text='Message Panel:')   
        msgFrame.configure(background='Pink')
        msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8, )
        msg = Label(msgFrame,text=(msgData), fg='red')
        msg.grid(row=0, column=0, padx=8)

    else:
        
        id = studID_field.get()
        name = studName_field.get()
        mark = studgrade_field.get()
        img = studImgLoc_field.get()
        grade = studgrade_field.get()
        Surname = studSurname_field.get()
        status = studStatus_field.get()
        print(id, name, Surname, grade, img)
        studDB.Update(id, name, Surname, grade, img, status)

        msgData="Student Record Has Been Updated"
        msgFrame = LabelFrame(win, text='Message Panel:')   
        msgFrame.configure(background='Pink')
        msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8, )
        msg = Label(msgFrame,text=(msgData), fg='red')
        msg.grid(row=0, column=0, padx=8)    

def Add():
    if len(studName_field.get() and studSurname_field.get() and studgrade_field.get() and studImgLoc_field.get()) == 0:
        msgData="Please Fill \nAll Fields In The \nForm To Submit A \nNew Student"
        msgFrame = LabelFrame(win, text='Message Panel:')   
        msgFrame.configure(background='Pink')
        msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8, )
        msg = Label(msgFrame,text=(msgData), fg='red')
        msg.grid(row=0, column=0, padx=8)

        studDB.Delete(name)

        

    else:
        name = studName_field.get()
        Surname = studSurname_field.get()
        grade = studgrade_field.get()
        img = studImgLoc_field.get()
        print(name)
        studDB.Add(name, Surname, grade, img)

        msgData="New Record Added"
        msgFrame = LabelFrame(win, text='Message Panel:')   
        msgFrame.configure(background='Pink')
        msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8, )
        msg = Label(msgFrame,text=(msgData), fg='red')
        msg.grid(row=0, column=0, padx=8)

    
def InsertData():

    studID_field.delete(0,END)
    studID_field.insert(END,12345)
    studName_field.delete(0,END)
    studName_field.insert(END,"Osman")
    studgrade_field.delete(0,END)
    studgrade_field.insert(END,95)
    studSurname_field.delete(0,END)
    studSurname_field.insert(END,"Abdulrazak")
    studImgLoc_field.delete(0,END)
    studImgLoc_field.insert(END,'face.png')
    studStatus_field.delete(0,END)
    studStatus_field.insert(END,1)

    msgData="Inserting Test Data"
    msgFrame = LabelFrame(win, text='Message Panel:')   
    msgFrame.configure(background='Pink')
    msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8)
    msg = Label(msgFrame,text=(msgData), fg='red')
    msg.grid(row=0, column=0, padx=8)

def select_item():
    pass

def insertTree():
    for row in list:
        tv.insert("", 0, values=row)
        #tv.insert('',END,values=row)

def clearTree():
    x = tv.get_children()

    for item in x:
        tv.delete(item)

    msgData="Clearing Display Panel"
    msgFrame = LabelFrame(win, text='Message Panel:')
    msgFrame.configure(background='Pink')   
    msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8)
    msg = Label(msgFrame,text=(msgData), fg='red')
    msg.grid(row=0, column=0, padx=8)

    
def clearPanel():
    studID_field.delete(0,END)
    studName_field.delete(0,END)
    studgrade_field.delete(0,END)
    studSurname_field.delete(0,END)
    studImgLoc_field.delete(0,END)
    studStatus_field.delete(0,END)

    msgData="Clearing Student Panel Form"
    msgFrame = LabelFrame(win, text='Message Panel:')
    msgFrame.configure(background='Pink')   
    msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8)
    msg = Label(msgFrame,text=(msgData), fg='red')
    msg.grid(row=0, column=0, padx=8)

def Quit():
    global win
    win.destroy()

def select_item(event):
    row = tv.item(tv.selection())
    print("row",type(row),row)
    item = tv.selection()[0]
    print ('item clicked ', item)
    print (tv.item(item)['values'][0])
    studID_field.delete(0,END)
    studName_field.delete(0,END)
    studgrade_field.delete(0,END)
    studSurname_field.delete(0,END)
    studImgLoc_field.delete(0,END)
    studStatus_field.delete(0,END)

    studID_field.insert(END,row['values'][0])
    studName_field.insert(END,row['values'][1])
    studgrade_field.insert(END,row['values'][3])
    studSurname_field.insert(END,row['values'][2])
    studImgLoc_field.insert(END,row['values'][4])
    studStatus_field.insert(END,row['values'][5])

    row4=tv.selection()
    row = tv.item(tv.selection())
    print("row: ", row, "type: ", type(row))
    print("pic location: "+row['values'][4])
    pic = row['values'][4]
    img = ImageTk.PhotoImage(Image.open(pic))
    print("img information: ", img)
    imglabel = Label(studFrame, image=img).grid(row=7, column=1, sticky=W)
    imgLabel.configure(image = img)
    imgLabel.image = img

    msgData="Viewing Student Record"
    msgFrame = LabelFrame(win, text='Message Panel:')
    msgFrame.configure(background='Pink')   
    msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8)
    msg = Label(msgFrame,text=(msgData), fg='red')
    msg.grid(row=0, column=0, padx=8)
        

def Search():
    id = studID_field.get()
    name = studName_field.get()
    mark = studgrade_field.get()
    img = studImgLoc_field.get()
    grade = studgrade_field.get()
    Surname = studSurname_field.get()
    status = studStatus_field.get()
    print(id, name, Surname, grade, img, status)
    records=studDB.Search(id, name)
    print(records)
    clearTree()
    for row in records:
        tv.insert("",0,values=row)

    msgData="Displaying Search Result"
    msgFrame = LabelFrame(win, text='Message Panel:')
    msgFrame.configure(background='Pink')   
    msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8)
    msg = Label(msgFrame,text=(msgData), fg='red')
    msg.grid(row=0, column=0, padx=8)
    


    
#        *************************************
#        ********Setting Up The Window********
#        *************************************



                 

win = Tk()
win.title("Student Database Application")
win.geometry("570x570")
win.configure(background = 'lightgrey')
##win.iconbitmap('C:\Users\oabdu\OneDrive\Desktop\Student Database\face.png')
##tkinter.messagebox.showinfo("message box", "By Pressing OK \
##You Agree To Abide By General Data Protection Regulation Laws \nMore Information\
##Can Be Found Here: \n https://eugdpr.org/")


#        *************************************
#        ****ENTERING/VIEWING STUDENT DATA****
#        *************************************

studFrame = LabelFrame(win, text='Student Panel')
studFrame.configure(background='LightBlue2')
studFrame.grid(row = 0, column = 0, sticky = NSEW, padx = 8, pady = 8)


studID = Label(studFrame, text = 'ID: ')
studID.grid(row = 0, column = 0)
studID_text = StringVar()
studID_field = Entry(studFrame, textvariable = studID_text)
studID_field.grid(row = 0, column = 1)

studName = Label(studFrame, text = 'First Name: ')
studName.grid(row=1, column=0, pady=3)
studName_text = StringVar()
studName_field = Entry(studFrame, textvariable = studName_text)
studName_field.grid(row = 1, column = 1, padx = 5, pady = 2)

studgrade = Label(studFrame, text='Mark: ')
studgrade.grid(row=3, column=0, pady=3)
studgrade_num = IntVar()
studgrade_field = Entry(studFrame, textvariable=studgrade_num)
studgrade_num.set('')
studgrade_field.grid(row=3, column=1, padx=5, pady=2)

studSurname = Label(studFrame, text = 'Surname: ')
studSurname.grid(row=2, column=0, pady=3)
studSurname_text = StringVar()
studSurname_field = Entry(studFrame, textvariable = studSurname_text)
studSurname_field.grid(row = 2, column = 1, padx = 5, pady = 2)

studImgLoc = Label(studFrame, text = 'stud ImgLoc: ')
studImgLoc.grid(row=5, column=0, pady=3)
studImgLoc_text = StringVar()
studImgLoc_field = Entry(studFrame, textvariable = studImgLoc_text)
studImgLoc_field.grid(row = 5, column = 1, padx = 5, pady = 2)


#Setting it up and viewing the default image
default = ("face2.png")
img = ImageTk.PhotoImage(Image.open(default))
imglabel = Label(studFrame, image=img).grid(row=7, column=1, sticky=W)

studStatus = Label(studFrame, text = 'stud Status: ')
studStatus.grid(row=4, column=0, pady=3)
studStatus_text = StringVar()
studStatus_field = Entry(studFrame, textvariable = studStatus_text)
studStatus_field.grid(row = 4, column = 1, padx = 5, pady = 2)

btnFrame = LabelFrame(win)
btnFrame.configure(background='White')
btnFrame.grid(row=0, column=3, sticky=W,padx=8,pady=8)

#        *************************************
#        ***************BUTTONS***************
#        *************************************

viewIcon=PhotoImage(file="view.png")
deleteIcon=PhotoImage(file="delete.png")
updateIcon=PhotoImage(file="update.png")
addIcon=PhotoImage(file="add.png")
insertIcon=PhotoImage(file="insert.png")
quitIcon=PhotoImage(file="quit.png")
searchIcon=PhotoImage(file="search.png")
clearIcon=PhotoImage(file="clear.png")

b1=Button(btnFrame,text="View all",width=12, command=viewAll)
b1.config(image=viewIcon,width="38",height="38")
b1['border']='0'
b1.grid(row=0, column=0)

b2=Button(btnFrame,text="Delete",width=12, command=Delete)
b2.config(image=deleteIcon,width="38",height="38")
b2['border']='0'
b2.grid(row=2, column=0)

b3=Button(btnFrame,text="Update",width=12, command=Update)
b3.config(image=updateIcon,width="38",height="38")
b3['border']='0'
b3.grid(row=3, column=0)

b4=Button(btnFrame,text="Add",width=12, command=Add)
b4.config(image=addIcon,width="38",height="38")
b4['border']='0'
b4.grid(row=4, column=0)

b5=Button(btnFrame,text="Insert",width=12, command=InsertData)
b5.config(image=insertIcon,width="38",height="38")
b5['border']='0'
b5.grid(row=5, column=0)

b6=Button(studFrame,text="Search",width=12, command=Search)
b6.config(image=searchIcon,width="20",height="20")
b6['border']='0'
b6.grid(row=0, column=2)

b7=Button(btnFrame,text="Quit",width=12, command=Quit)
b7.config(image=quitIcon,width="38",height="38")
b7['border']='0'
b7.grid(row=7, column=0)

b8=Button(studFrame,text="clearPanel",width=12, command=clearPanel)
b8.config(image=clearIcon,width="30",height="30")
b8['border']='0'
b8.grid(row=7, column=2, sticky = N)

b8=Button(win,text="clearTree",width=12, command=clearTree)
b8.config(image=clearIcon,width="30",height="30")
b8['border']='0'
b8.grid(row=1, column=1, sticky = N)


dispFrame = LabelFrame(win, text='Displaypanel:')
dispFrame.configure(background='Green')
dispFrame.grid(row=1, column=0, sticky=N,padx=8)

tv = ttk.Treeview(dispFrame, height=10,columns=3)
tv.grid(row=1, column=1, columnspan=2)
tv["columns"] = ["stud ID", "stud Name", "studSurname", "grade", "ImageLoc"]
tv["show"] = "headings"

tv.heading("stud ID", text="ID")
tv.column("stud ID", anchor='center', width=70)

tv.heading("stud Name", text="First Name")
tv.column("stud Name", anchor='center', width=100)

tv.heading("studSurname", text="Surname")
tv.column("studSurname", anchor="center", width=70)

tv.heading("grade", text='Mark')
tv.column("grade", anchor='center', width=70)

tv.heading("ImageLoc", text='Image')
tv.column("ImageLoc", anchor='center', width=70)

tv.bind('<ButtonRelease-1>')
sb1 = Scrollbar(dispFrame, command = tv.yview, orient=VERTICAL)
sb1.grid(row = 0, column = 7, rowspan = 2, sticky = 'ns')
tv.configure(yscrollcommand=sb1.set)

#tv.bind('<ButtonRelease-1>', show_pic)
tv.bind('<ButtonRelease-1>', select_item)
tv.bind('<Return>', select_item)

#      ********Message Box********



msgData="No action taken"
msgFrame = LabelFrame(win, text='Message Panel:')
msgFrame.configure(background='Pink')
msgFrame.grid(row=1, column=3, sticky=NSEW,padx=8)
msg = Label(msgFrame,text=(msgData), fg='red')
msg.grid(row=0, column=0, padx=8, )

                 
win.mainloop()
