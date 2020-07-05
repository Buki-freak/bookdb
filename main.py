#! /usr/bin/python3.7
# Module request: pymysql, tkinter, PIL
# Author: buki
import query, login
from tkinter import *
from PIL import Image, ImageTk

"""
---Main GUI---
"""

class mainUI(object):
    """
    Library system GUI
    """
    def __init__(self):
        """
        init function

        widget: button, label, image
        """
        self.root = Tk()
        # root -> set size
        self.root.geometry("900x800")
        # root -> set title
        self.root.title("GDUFS Library System")
        # root -> adjustment abandoned
        self.root.wm_resizable(False, False)

        # root -> create label
        self.L1 = Label(self.root, text='  GDUFS Library System\n\nChoose ot login or query',width=40,\
        font=('Helvetica', 25), justify=LEFT, relief=RIDGE, background='#6699ff')
        # root -> apply label
        self.L1.pack(anchor=S, pady=20, fill=NONE)

        # root -> create image
        bg_img = Image.open('./gdufs.jpg')
        bg_img = ImageTk.PhotoImage(bg_img)
        bg_img_label = Label(self.root, image=bg_img, height=200, width=800)
        # root -> apply image
        bg_img_label.pack(side=TOP, fill=NONE, padx=0, pady=50)

        # root -> create button1 for query
        self.query_button = Button(self.root, font=('Helveticas', 15, 'bold'), \
        text='go to query', fg='#669905',command=self.goto_query)
        # root -> apply button1
        self.query_button.pack(anchor='s', padx=20)

        # root -> create button2 for login
        self.login_button = Button(self.root, font=('Helveticas', 15, 'bold'),\
        text='go to login', fg='#cc00ff', command=self.goto_login)
        # root -> apply button2
        self.login_button.pack(anchor='s', padx=20, pady=20)

        # root -> create quit button
        self.root.QUIT = Button(self.root, text='quit', fg='red', command=self.root.quit, font=('Helvetica', 20,'bold'))
        # root -> apply quit button
        self.root.QUIT.pack(side="bottom",anchor="ne")
        
        # run GUI
        self.root.mainloop()
        
        # pass the error if it exists
        try:
            self.root.destroy()
        except:
            pass

    def goto_query(self):
        """
        Go to query function
        """
        # destory main GUI
        self.root.destroy()

        # enter query GUI
        query.init()

    def goto_login(self):
        """
        Go to login function
        """
        # destory main GUI
        self.root.destroy()

        # enter login GUI
        login.init()


def init():
    mainUI()


if __name__ == "__main__":
    init()