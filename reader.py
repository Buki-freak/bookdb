#! /usr/bin/python3.7
# Module request: pymysql, tkinter
# Author: buki
import login
from tkinter import *
import pymysql
import tkinter

"""
Reader GUI
"""

class readerUI(object):
    """
    Reader GUI
    """
    def __init__(self,tmp_id):
        """
        init function

        widget:
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
        self.L1 = Label(self.root,text='   GDUFS Library System\n\n   Welcome %s reader!' % tmp_id,\
        font=('Helvetica', 25), width=40, justify=LEFT, relief=RIDGE,background='#6699ff')
        # root -> apply label for topic
        self.L1.pack(anchor='center',pady=40,fill=NONE)

        """
        # root -> create scrollbar
        S1 = tkinter.Scrollbar(self.info)
        # root -> apply scrollbar
        S1.pack(side='right',fill='y')
        """

        # root -> create info blank
        self.info = Text(self.root,font=('Helvetica', 13), width=100, height=30,bg='#C0C0C0',bd=0)
        # root -> apply info blank
        self.info.pack(pady=15)

        self.fetch_info()

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
    

    def fetch_info(self):
        # try to connect to bookdb
        try:
            self.db_connect = pymysql.connect('localhost', 'common_user',\
                'common_just','bookdb')
            self.cursor = self.db_connect.cursor()
        # unable to connect the database
        except pymysql.OperationalError:
            self.info.insert('end', 'Database connect error!')
            return
        
        # execute the sql and fetch the result
        sql = "select borrow.isbn, book_name,book_type,author,publisher,price,borrow_time from borrow,book where borrow.isbn = book.isbn and borrow.r_id='%s' " %  self.id
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        # unable to connect the database
        except pymysql.OperationalError:
            self.info.insert('end', "Database error!")
            return

        # no borrow info
        if len(data) == 0:
            self.info.insert('end','You haven\'t borrow any book.')
            self.db_connect.close()
            return
        
        # show borrow info
        self.info.insert('end','borrow list:\n')
        for i in range(len(data)):
            self.info.insert('end',"\nisbn: %s" % data[i][0])
            self.info.insert('end',"\nbook name: <<%s>>" % data[i][1])
            self.info.insert('end',"\nbook type: %s" % data[i][2])
            self.info.insert('end',"\nauthor: %s" % data[i][3])
            self.info.insert('end',"\npublisher: %s" % data[i][4])
            self.info.insert('end',"\nprice: %s" % data[i][5])
            self.info.insert('end',"\nborrow time: %s\n" % data[i][6])
        self.db_connect.close()
        return
        

    def goto_login(self):
        """
        go to login function
        """
        # destroy reader GUI
        self.root.destroy()

        # enter login GUI
        login.init()

def init(global_id):
    readerUI(global_id)

