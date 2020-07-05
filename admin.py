#! /usr/bin/python3.7
# Module request: pymysql, tkinter
# Author: buki
import main
import login
from tkinter import *
import tkinter
import pymysql
import random
import datetime


"""
---Admin GUI---
"""

class adminUI(object):
    """
    admin GUI
    """
    def __init__(self,tmp_id):
        """
        init function

        widget: button,label,notebook,frame,entry
        """
        # fetch id
        self.id = tmp_id

        self.root = Tk()
        # root -> set size
        self.root.geometry("900x800")
        # root -> set title
        self.root.title("Reader GUI")
        # root -> adjustment abandoned
        self.root.wm_resizable(False, False)

        # root -> create sign out button
        self.signout_button = Button(self.root,text='sign out',fg='blue',command=self.goto_login,font=('Helvetica', 20, 'bold'))
        # root -> apply sign out button
        self.signout_button.pack(anchor='nw', side='top',pady=0)

        # root -> create label for topic
        self.L1 = Label(self.root,text='  GDUFS Library System\n\n  Welcome %s admin!' % tmp_id,\
        font=('Helvetica', 25), width=40, justify=LEFT, relief=RIDGE,background='#6699ff')
        # root -> apply label for topic
        self.L1.pack(anchor='center',pady=40,fill=NONE)

        # root -> create notebook
        self.N1 = ttk.Notebook(self.root,height=200,width=400)
        
        # N1 -> create frame1
        self.frame1 = Frame(self.N1)

        # frame1 -> create topic1
        self.topic1 = Label(self.frame1,text='  Input isbn and reader ID to borrow.',width=40, justify=LEFT,font=('Helvetica', 25))
        # frame1 -> apply topic
        self.topic1.pack(anchor='center',pady=40,fill=NONE)

        # frame1 -> create frame11
        self.frame11 = Frame(self.frame1,width=200,height=20,bd=0)
        # frame1 -> apply frame11
        self.frame11.pack(side='top',pady=15)

        # frame11 -> create label11
        self.L11 = Label(self.frame11,text='    isbn: ',font=('Helvetica', 17))
        # frame11 -> apply label11
        self.L11.pack(side=LEFT,padx=5)

        # create temp varables
        self.isbn_content = StringVar(self.root)
        # frame11 -> create entry
        self.isbn = Entry(self.frame11,font=('Helvetica', 20),width=20,xscrollcommand=TRUE, bd=5,\
        textvariable=self.isbn_content)
        # frame11 -> apply entry
        self.isbn.pack(side=RIGHT,padx=2)

        # frame1 -> create frame12
        self.frame12 = Frame(self.frame1,width=200,height=20,bd=0)
        # frame1 -> apply create frame12
        self.frame12.pack(side='top',pady=15)

        # frame12 -> create label12
        self.L12 = Label(self.frame12,text='reader ID: ',font=('Helvetica', 17))
        # frame12 -> apply label12
        self.L12.pack(side=LEFT)

        # create temp variables
        self.reader_id_content=StringVar(self.root)
        # frame12 -> create entry
        self.reader_id = Entry(self.frame12,font=('Helvetica', 20),width=20,xscrollcommand=TRUE, bd=5,\
        textvariable=self.reader_id_content)
        # frame11 -> apply entry
        self.reader_id.pack(side=RIGHT,padx=2)

        # frame1 -> create button
        self.borrow_button = Button(self.frame1,text='Confirm',font=('Helveticas',15,'bold'),\
        command=self.borrow)
        # frame1 -> apply button
        self.borrow_button.pack(side=TOP,padx=30,pady=30)

        # N1 -> add frame1
        self.N1.add(self.frame1, text='Borrow')


        # N1 -> create frame2
        self.frame2 = Frame(self.N1)

        # frame2 -> create topic2
        self.topic2 = Label(self.frame2,text='  Input isbn and reader ID to return.',width=40, justify=LEFT,font=('Helvetica', 25))
        # frame2 -> apply topic2
        self.topic2.pack(anchor='center',pady=40,fill=NONE)

        # frame2 -> create frame21
        self.frame21 = Frame(self.frame2,width=200,height=20,bd=0)
        # frame2 -> apply frame21
        self.frame21.pack(side='top',pady=15)

        # frame21 -> create label21
        self.L21 = Label(self.frame21,text='    isbn: ',font=('Helvetica', 17))
        # frame21 -> apply label21
        self.L21.pack(side=LEFT,padx=5)

        # create temp varables
        self.isbn_content1 = StringVar(self.root)
        # frame11 -> create entry
        self.isbn1 = Entry(self.frame21,font=('Helvetica', 20),width=20,xscrollcommand=TRUE, bd=5,\
        textvariable=self.isbn_content1)
        # frame11 -> apply entry
        self.isbn1.pack(side=RIGHT,padx=2)

        # frame2 -> create frame22
        self.frame22 = Frame(self.frame2,width=200,height=20,bd=0)
        # frame2 -> apply create frame22
        self.frame22.pack(side='top',pady=15)

        # frame22 -> create label22
        self.L22 = Label(self.frame22,text='reader ID: ',font=('Helvetica', 17))
        # frame22 -> apply label22
        self.L22.pack(side=LEFT)

        # create temp variables
        self.reader_id_content1=StringVar(self.root)
        # frame22 -> create entry
        self.reader_id1 = Entry(self.frame22,font=('Helvetica', 20),width=20,xscrollcommand=TRUE, bd=5,\
        textvariable=self.reader_id_content1)
        # frame22 -> apply entry
        self.reader_id1.pack(side=RIGHT,padx=2)

        # frame2 -> create button
        self.borrow_button = Button(self.frame2,text='Confirm',font=('Helveticas',15,'bold'),\
        command=self.return_book)
        # frame1 -> apply button
        self.borrow_button.pack(side=TOP,padx=30,pady=30)

        # N1 -> add frame2
        self.N1.add(self.frame2, text='Return')

        # root -> apply N1
        self.N1.pack(expand=True,fill='both')
        # N1 -> set default frame
        self.N1.select(self.frame1)

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


    def borrow(self):
        """
        borrow book function
        """

        # fetch isbn
        self.tmp_isbn = self.isbn_content.get()
        # fetch reader ID
        self.tmp_reader_id = self.reader_id_content.get()

        # strip isbn
        self.tmp_isbn = self.tmp_isbn.strip()
        # strip reader ID
        self.tmp_reader_id = self.tmp_reader_id.strip()

        # check if isbn is empty
        if '' in [self.tmp_isbn, self.tmp_reader_id]:
            tkinter.messagebox.showinfo('Error', 'Please input your info!')
            return
        
        # try to connect to bookdb
        self.connect_database()

        # check if the reader has the previlige
        previlige_result = self.check_previlige()

        if previlige_result[0]>0:
            if not previlige_result[1]:
                tkinter.messagebox.showinfo('Error','The reader\'s in the blacklist!')
                self.db_connect.close()
                return
            else:
                sql = "select b_id from borrow where r_id='%s'" % self.tmp_reader_id
                sql1 = "select b_id from borrow where isbn='%s'" % self.tmp_isbn
                # execute the sql and fetch the result
                try:
                    self.cursor.execute(sql)
                    data = self.cursor.fetchall()
                    self.cursor.execute(sql1)
                    data1 = self.cursor.fetchall()
                # deal with sql operations error
                except (pymysql.InternalError, pymysql.ProgrammingError):
                    self.db_connect.close()
                    tkinter.messagebox.showinfo('Error', 'sql query error')
                    return
                # check if the reader has reached his max previlige
                if len(data) + 1 > previlige_result[0]:
                    self.db_connect.close()
                    tkinter.messagebox.showinfo('Error', 'Max previlige has been reached!')
                    return
                
                # check if the book has been borrowed
                if len(data1) != 0:
                    self.db_connect.close()
                    tkinter.messagebox.showinfo('Error', 'The book has been borrowed')
                    return
                
                # generate random borrow id
                b_id = str(random.getrandbits(16)).zfill(5)
                sql = "insert into borrow(b_id, isbn, r_id, borrow_time) values ('%s','%s','%s','%s')"\
                % (b_id, self.tmp_isbn, self.tmp_reader_id, str(datetime.datetime.now())[:10])
                # execute the sql and fetch the result
                try:
                    self.cursor.execute(sql)
                # deal with sql operations error
                except (pymysql.InternalError, pymysql.ProgrammingError):
                    tkinter.messagebox.showinfo('Error', 'sql query error')
                    self.db_connect.close()
                    return
                except pymysql.IntegrityError:
                    tkinter.messagebox.showinfo('Error','Book doesn\'t exist!')
                    self.db_connect.close()
                    return

                # commit the changes
                self.db_connect.commit()

                tkinter.messagebox.showinfo('Success','Successfully borrowed!')
                self.db_connect.close()
                return

    def check_previlige(self):
        """
        check reader previlige function
        """
        sql = "select max_previlige,previlige from reader where r_id='%s'" % self.tmp_reader_id
        # execute the sql and fetch the result
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()

        # deal with sql operations error
        except (pymysql.InternalError, pymysql.ProgrammingError):
            self.db_connect.close()
            tkinter.messagebox.showinfo('Error', 'sql query error')
            return -1, False

        # Invalid user
        if len(data) == 0:
            self.db_connect.close()
            tkinter.messagebox.showinfo('Error', 'Reader doesn\'t exists!')
            return -1, False
        else:
            return data[0]
    
    def return_book(self):  # check
        """
        return book function
        """
        # fetch isbn
        tmp_isbn = self.isbn_content1.get()
        # fetch reader id
        tmp_reader_id = self.reader_id_content1.get()

        # strip isbn and reader id
        tmp_isbn = tmp_isbn.strip()
        tmp_reader_id = tmp_reader_id.strip()

        if '' in [tmp_isbn, tmp_reader_id]:
            tkinter.messagebox.showinfo('Error','Please input your info!')
            return
        
        # try to connect to bookdb
        self.connect_database()

        # check whether reader exists
        sql  = "select * from reader where r_id='%s'" % tmp_reader_id
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        # deal with sql operations error
        except (pymysql.InternalError, pymysql.ProgrammingError):
            tkinter.messagebox.showinfo('Error', 'sql query error')
            self.db_connect.close()
            return
        
        if len(data) == 0:
            tkinter.messagebox.showinfo('Error','reader doesn\'t exist!')
            self.db_connect.close()
            return

        # check whether borrow exists
        sql  = "select * from borrow where isbn='%s' and r_id='%s'" % (tmp_isbn,tmp_reader_id)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        # deal with sql operations error
        except (pymysql.InternalError, pymysql.ProgrammingError):
            tkinter.messagebox.showinfo('Error', 'sql query error')
            self.db_connect.close()
            return
        
        if len(data) == 0:
            tkinter.messagebox.showinfo('Error','borrow doesn\'t exist!')
            self.db_connect.close()
            return

        # delete borrow infomation
        sql = "delete from borrow where isbn='%s'" % tmp_isbn
        try:
            self.cursor.execute(sql)
        # deal with sql operations error
        except pymysql.ProgrammingError:
            tkinter.messagebox.showinfo('Error', 'sql query error')
            self.db_connect.close()
            return
        
        # commit changes
        self.db_connect.commit()

        tkinter.messagebox.showinfo('Success', 'Successfully returned!')
        self.db_connect.close()
        return

    def connect_database(self):
        # try to connect to bookdb
        try:
            self.db_connect = pymysql.connect('localhost', 'admin_user',\
                'admin_just','bookdb')
            self.cursor = self.db_connect.cursor()
        # unable to connect the database
        except pymysql.OperationalError:
            tkinter.messagebox.showinfo('Error', 'Database connect error!')
            return

    def goto_login(self):
        """
        go to login GUI function
        """
        # destory admin GUI
        self.root.destroy()

        # enter login GUI
        login.init()

def init(global_id):
    adminUI(global_id)

      