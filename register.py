#! /usr/bin/python3.7
# Module request: pymysql, tkinter
# Author: buki
import login
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import pymysql
import random

"""
---Register GUI
"""

class registerUI(object):
    """
    book system register GUI
    """
    def __init__(self):
        """
        init function

        widget: button, label, frame, entry
        """
        self.root = Tk()
        # root -> set size
        self.root.geometry("900x800")
        # root -> set title
        self.root.title("Register GUI")
        # root -> adjustment abandoned
        self.root.wm_resizable(False,False)

        # root -> create back button
        self.back_button = Button(self.root,text='back',fg='blue',command=self.goto_login,font=('Helvetica', 20, 'bold'))
        # root -> apply back button
        self.back_button.pack(anchor='nw',side='top',pady=0)

        # root -> create label for topic
        self.L1 = Label(self.root,text='       GDUFS Library System\n\nInput your information to register',\
        font=('Helvetica', 25), width=40, justify=LEFT, relief=RIDGE,background='#6699ff')
        # root -> apply label for topic
        self.L1.pack(anchor='center',pady=40,fill=NONE)


        # root -> create frame1
        self.frame1 = Frame(self.root,height=20,width=200,bd=0)
        # root -> apply frame1
        self.frame1.pack(side='top',pady=10)

        # frame1 -> create label
        self.L2 = Label(self.frame1,text='Your name:',font=('Helvetica', 15))
        # frame1 -> apply label
        self.L2.pack(side=LEFT,padx=5)

        # create temp varables
        self.name_content = StringVar(self.root)
        # frame1 -> create entry
        self.name = Entry(self.frame1,font=('Helvetica', 20),width=20,xscrollcommand=TRUE, bd=5,\
        textvariable=self.name_content)
        # frame1 -> apply entry
        self.name.pack(side=RIGHT,padx=5)


        # root -> create frame2
        self.frame2 = Frame(self.root,height=20,width=200,bd=0)
        # root -> apply frame2
        self.frame2.pack(side='top',pady=10)

        # frame2 -> create label
        self.L3 = Label(self.frame2,text='Password: ',font=('Helvetica', 15))
        # frame2 -> apply label
        self.L3.pack(side=LEFT,padx=5)

        # create temp varables
        self.passwd_content = StringVar(self.root)
        # frame2 -> create entry
        self.passwd = Entry(self.frame2,font=('Helvetica', 20),width=20,xscrollcommand=TRUE, bd=5,\
        textvariable=self.passwd_content)
        # frame2 -> apply entry
        self.passwd.pack(side=RIGHT,padx=5)


        # root -> create frame4
        self.frame3 = Frame(self.root, height=20,width=200,bd=0)
        # root -> apply frame4
        self.frame3.pack(side='top',pady=10)

        # frame4 -> create label
        self.L4 = Label(self.frame3,text='Your gender:',font=('Helvetica', 15))
        # frame4 -> apply label
        self.L4.pack(side=LEFT,padx=5)

        # create temp varables
        self.sex_content = StringVar(self.root)
        # frame4 -> create combobox
        self.sex = ttk.Combobox(self.frame3,font=('Helvetica', 15), width=5, state='readonly', textvariable=self.sex_content)
        # sex -> set value
        self.sex['value'] = ('M','F')
        # frame4 -> apply combobox
        self.sex.pack(side=RIGHT)


        # root -> create submit button
        self.submit_button = Button(self.root,text='Submit',font=('Helveticas',15,'bold'),\
        command=self.register)
        # root -> apply submit button
        self.submit_button.pack(pady=20)

        # root -> create quit button
        self.root.QUIT = Button(self.root,text='quit',fg='red',command=self.root.quit, font=('Helvetica', 20,'bold'))
        # root -> apply quit button
        self.root.QUIT.pack(anchor='ne',side='bottom',pady=0)

        # run GUI
        self.root.mainloop()

        # pass the error if it exists
        try:
            self.root.destroy()
        except:
            pass

    def register(self):
        """
        register function
        """
        # fetch reader name
        tmp_name = self.name_content.get()

        # fetch reader password
        tmp_passwd = self.passwd_content.get()

        # fetch reader gender
        tmp_sex = self.sex_content.get()

        # strip the name and password
        tmp_name = tmp_name.strip()
        tmp_passwd = tmp_passwd.strip()

        # check if name or password is empty
        if '' in [tmp_name, tmp_passwd,tmp_sex]:
            tkinter.messagebox.showinfo('Error', 'Please input your info!')
            return
        
        # try to connect to bookdb
        try:
            self.db_connect = pymysql.connect('localhost', 'common_user',\
            'common_just','bookdb')
            self.cursor=self.db_connect.cursor()
        # unable to connect the database
        except pymysql.OperationalError:
            tkinter.messagebox.showinfo('Error', 'Database connect error!')
            return

        # check if id is repeated
        sql = "select r_id from reader"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        # deal with sql operation error
        except (pymysql.InternalError,pymysql.ProgrammingError):
            self.db_connect.close()
            tkinter.messagebox.showinfo('Error', 'sql query error')
            return
        
        # fetch result from data
        id_list = []
        for i in range(len(data)):
            id_list.append(data[i][0])
        
        # generate random id
        while True:
            tmp_id = str(random.getrandbits(16)).zfill(5)
            # check
            if tmp_id not in id_list:
                break
        
        # insert the reader info
        sql = "insert into reader values ('%s','%s','%s','%s',3,TRUE)" % (tmp_id, tmp_passwd, tmp_name,tmp_sex)
        try:
            self.cursor.execute(sql)
            # commit your changes here!!!!
            self.db_connect.commit()
        # deal with sql operations error
        except (pymysql.InternalError, pymysql.ProgrammingError):
            self.db_connect.close()
            tkinter.messagebox.showinfo('Error', 'sql query error')
            return

        # register success
        tkinter.messagebox.showinfo('Success','Successfully register!\nYour ID is : %s' % tmp_id)
        self.db_connect.close()

        # go to login GUI
        self.goto_login()
        
    def goto_login(self):
        """
        go to login function
        """
        # destory register GUI
        self.root.destroy()

        # enter login GUI
        login.init()

def init():
    registerUI()

