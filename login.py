#! /usr/bin/python3.7
# Module request: pymysql, tkinter
# Author: buki
import main
import register
import reader
import admin
import pymysql
import tkinter.messagebox
from tkinter import ttk
from tkinter import *


"""
---Login GUI---
"""

class loginUI(object):
    """
    book system login GUI
    """
    def __init__(self):
        """
        init function

        widget: frame, button, label, entry, combobox
        """
        self.root = Tk()
        # root -> set size
        self.root.geometry("900x800")
        # root ->  set title
        self.root.title("Login GUI")
        # root -> adjustment abandoned
        self.root.wm_resizable(False, False)

        # root -> create back button
        self.back_button = Button(self.root, text='back', fg='blue', command=self.goto_main, font=('Helvetica', 20, 'bold'))
        # root -> apply back button
        self.back_button.pack(anchor='nw', side='top',pady=0)

        # root -> create label for topic
        self.L1 = Label(self.root,text='     GDUFS Library System\n\nInput your information to login',\
        font=('Helvetica', 25), width=40, justify=LEFT, relief=RIDGE,background='#6699ff')
        # root -> apply label for topic
        self.L1.pack(anchor='center',pady=40,fill=NONE)


        # root -> create frame1
        self.frame1 = Frame(self.root,height=20,width=200,bd=0)
        # root -> apply frame1
        self.frame1.pack(side='top',pady=10)

        # frame1 -> create label
        self.L2 = Label(self.frame1,text='      ID:',font=('Helvetica', 15))
        # frame1 -> apply label
        self.L2.pack(side=LEFT,padx=2)

        # create temp varables
        self.id_content = StringVar(self.root)
        # frame1 -> create entry for id on frame1
        self.id = Entry(self.frame1,font=('Helvetica', 20),width=20,xscrollcommand=TRUE, bd=5,\
        textvariable=self.id_content)
        # frame1 -> apply entry for id
        self.id.pack(side=RIGHT,padx=2)


        # root -> create frame2
        self.frame2 = Frame(self.root,height=20,width=200,bd=0)
        # root -> apply frame2
        self.frame2.pack(side='top',pady=10)

        # frame2 -> create label for password on frame2
        self.L3 = Label(self.frame2,text='Password:',font=('Helvetica', 15))
        # frame2 -> apply label for password
        self.L3.pack(side=LEFT,padx=2)

        # create temp varables
        self.passwd_content = StringVar(self.root)
        # frame2 -> create entry for password
        self.passwd = Entry(self.frame2,font=('Helvetica', 20),width=20,xscrollcommand=TRUE, bd=5,\
        textvariable=self.passwd_content,show='*')
        # frame2 -> apply entry for password
        self.passwd.pack(side=RIGHT,padx=2)


        # root -> create frame3
        self.frame3 = Frame(self.root,height=20,width=200,bd=0)
        # root -> apply frame3
        self.frame3.pack(side='top',pady=20)

        # frame3 -> create label
        self.L4 = Label(self.frame3,text='Login as: ',font=('Helvetica', 15))
        # frame3 -> apply label
        self.L4.pack(side=LEFT,padx=2)

        # frame3 -> create temp variable
        self.login_type_content = StringVar(self.root)
        # frame3 -> create combobox for login type
        self.login_type = ttk.Combobox(self.frame3,font=('Helvetica', 15), width=15, state='readonly', textvariable=self.login_type_content)
        # login_type ->  set value
        self.login_type['value'] = ('reader','admin')
        # login_type -> set default value
        self.login_type.current(0)
        # frame3 -> apply combobox
        self.login_type.pack(side=RIGHT)

        
        # root -> create frame4
        self.frame4 = Frame(self.root,height=20,width=200,bd=0)
        # root -> apply frame4
        self.frame4.pack(side='top',pady=20)

        # frame4 -> create button for login
        self.login_button = Button(self.frame4,text='Login',font=('Helveticas',15,'bold'),\
        command=self.check)
        # frame4 -> apply button for login
        self.login_button.pack(side=TOP,padx=30,pady=20)

        # frame4 -> create button for register
        self.register_button = Button(self.frame4,text='Rigister',font=('Helveticas',15,'bold'),\
        command=self.goto_register,fg='green')
        # frame4 -> apply button for register
        self.register_button.pack(side=BOTTOM,padx=20)


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

    def check(self):
        """
        check login function
        """
        # fetch login type
        tmp_login_type = self.login_type_content.get()

        # fetch id
        tmp_id = self.id_content.get()

        # fetch password
        tmp_passwd = self.passwd_content.get()

        # strip id and password
        tmp_id = tmp_id.strip()
        tmp_passwd = tmp_passwd.strip()

        # check if id or passwd is empty
        if '' in [tmp_id, tmp_passwd, tmp_login_type]:
            tkinter.messagebox.showinfo('Error', 'Please input your info!')
            return

        # try to connect to bookdb
        try:
            self.db_connect = pymysql.connect('localhost', 'common_user',\
                'common_just','bookdb')
            self.cursor = self.db_connect.cursor()
        # unable to connect the database
        except pymysql.OperationalError:
            tkinter.messagebox.showinfo('Error', 'Database connect error!')
            return
        
        # two login types
        if tmp_login_type == 'admin':
            sql = "select a_passwd from admin where a_id='%s'" % tmp_id
        elif tmp_login_type == 'reader':
            sql = "select r_passwd from reader where r_id='%s'" % tmp_id
        else:
            self.db_connect.close()
            tkinter.messagebox.showinfo('Error','Invalid login type')
            return

        # execute the sql and fetch the result
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        # deal with sql operations error
        except (pymysql.InternalError, pymysql.ProgrammingError):
            self.db_connect.close()
            tkinter.messagebox.showinfo('Error', 'sql query error')
            return
            
        # check if the password is right(password should be encrypted in practice)
        if len(data) == 0:
            self.db_connect.close()
            tkinter.messagebox.showinfo('Error', 'User doesn\'t exists!')
            return
        elif data[0][0] == tmp_passwd:
            self.db_connect.close()
            # go to according GUI
            if tmp_login_type == 'admin':
                # destory login GUI
                self.root.destroy()

                # enter admin GUI
                admin.init(tmp_id)
            else:
                # destory login GUI
                self.root.destroy()

                # enter reader GUI
                reader.init(tmp_id)
        # password is wrong  
        else:
            self.db_connect.close()
            tkinter.messagebox.showinfo('Error','Wrong password!')
            return

    def goto_register(self):
        """
        go to register GUI function
        """
        # destory login GUI
        self.root.destroy()

        # enter register GUI
        register.init()

    def goto_main(self):
        """
        go to main GUI function
        """
        # destroy login GUI
        self.root.destroy()

        # enter main GUI
        main.init()

def init():
    loginUI()

