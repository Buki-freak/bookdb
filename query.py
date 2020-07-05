#! /usr/bin/python3.7
# -*- coding: utf-8 -*-
# Module request: pymysql, tkinter
# Author: buki
import pymysql
from tkinter import ttk
from tkinter import *
import main

"""
---Query GUI---
"""
class db_queryUI(object):
    """
    book system query GUI
    """
    def __init__(self):
        """
        init function
        
        widget: frame, button, label, text, combobox
        """
        self.root = Tk()
        # root -> set size
        self.root.geometry("900x800")
        # root -> set title
        self.root.title("Book query GUI")
        # root -> adjustment abandoned
        self.root.wm_resizable(False, False)

        # root -> create back button
        self.back_button = Button(self.root, text='back', fg='blue', command=self.goto_main, font=('Helvetica', 20, 'bold'))
        # root -> apply back button
        self.back_button.pack(anchor='nw', side='top',pady=0)

        # root -> create label
        self.L1 = Label(self.root, text='       GDUFS Library System\n\nInput your search type and content',\
        font=('Helvetica', 25),width=40, justify=LEFT, relief=RIDGE, background='#6699ff')
        # root -> apply label
        self.L1.pack(anchor=S, pady=40, fill=NONE)

        # root -> create frame1
        self.frame1 = Frame(self.root,height=200,width=500,relief=RIDGE)
        # root -> apply frame1
        self.frame1.pack(fill=NONE, expand=False)

        # frame1 -> create temp variable
        self.search_type_content = StringVar(self.root)
        # frame1 -> create combobox
        self.search_type = ttk.Combobox(self.frame1, font=('Helvetica', 13), width=10, state='readonly', textvariable=self.search_type_content)
        # search_type -> set value
        self.search_type['value']=('isbn', 'book name', 'book type')
        # search_type -> set default value
        self.search_type.current(0)
        # frame1 -> apply combobox
        self.search_type.pack(anchor='w')

        # frame1 -> create temp variable
        self.search_text_content = StringVar(self.root)
        # frame1 -> create search blank
        self.search_text = Entry(self.frame1, font=('Helvetica', 18), width=60, xscrollcommand=TRUE, bd=5, textvariable=self.search_text_content)
        # frame1 -> apply search blank
        self.search_text.pack(pady=10)

        # root -> create frame2
        self.frame2 = Frame(self.root, height=50, width=500, relief=RIDGE)
        # root -> apply frame2
        self.frame2.pack(fill=NONE, expand=False)

        # frame2 -> create search button
        self.search_button = Button(self.frame2, font=('Helveticas', 15), fg='black', text='search', command=self.query)
        # frame2 -> apply search button
        self.search_button.pack(pady=20)

        # frame2 -> create result blank
        self.result_blank = Text(self.frame2, font=('Helvetica', 13), width=100, height=25)
        # frame2 -> apply result blank
        self.result_blank.pack(pady=15)

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

    def query(self):
        """
        book query function
        """
        # clear the result blank
        self.result_blank.delete(1.0, 'end')

        # fetch search type
        tmp_type = self.search_type_content.get()

        # fetch search text
        tmp_text = self.search_text_content.get().strip()

        # strip the search text
        tmp_text = tmp_text.strip()

        # clear the search blank
        self.search_text.delete(0, 'end')

        # if search text content is empty
        if tmp_text == '':
            self.result_blank.insert('end', "Please input your search content!")
            return

        # different search type
        if tmp_type == 'isbn':
            sql = "select * from book where isbn='%s'" % (tmp_text)
        elif tmp_type == 'book name':
            sql = "select distinct * from book where book_name='%s'" % (tmp_text)
        elif tmp_type == 'book type':
            sql="select distinct book_name from book where book_type='%s'" % (tmp_text)
        else:
            # deal with invalid search type
            self.result_blank.insert('end', "Invalid search type!")
            return

        # try to connect to bookdb
        try:
            self.db_connect = pymysql.connect('localhost', 'common_user',\
                'common_just', 'bookdb')
            self.cursor = self.db_connect.cursor()
        # unable to connect the database
        except pymysql.OperationalError:
            self.result_blank.insert('end', "Database error!")
            return

        # execute the sql and fetch the result
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        # deal with sql operations error
        except (pymysql.InternalError, pymysql.ProgrammingError):
            self.result_blank.insert('end', 'sql error!')
            self.db_connect.close()
            return

        # check if data is empty
        if data == ():
            self.result_blank.insert('end', 'No satisfying result!')
        else:
            # isbn and book name situations
            if tmp_type in ['isbn', 'book name']:
                for line in data:
                    self.result_blank.insert('end', 'isbn: '+str(line[0])+'\n')
                    self.result_blank.insert('end', 'book name: '+'<<'+str(line[1])+'>>'+'\n')
                    self.result_blank.insert('end', 'book type: '+str(line[2])+'\n')
                    self.result_blank.insert('end', 'author: '+str(line[3])+'\n')
                    self.result_blank.insert('end', 'publisher: '+str(line[4])+'\n')
                    self.result_blank.insert('end', 'price: '+ str(line[5])+'\n')
                    self.result_blank.insert('end', 'publish year: '+str(line[6])+'\n')
            # book type situations
            if tmp_type == 'book type':
                    for line in data:
                        self.result_blank.insert('end', '<<'+str(line[0])+'>>'+'\n')
        self.db_connect.close()
        return

    def goto_main(self):
        """
        go to main GUI function
        """
        # destroy query GUI
        self.root.destroy()
        
        # enter main GUI
        main.init()


def init():
    db_queryUI()