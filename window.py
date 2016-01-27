
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
__author__ = 'Geon'

import Tkinter
import os

from reto_taric.constants import APP_TITLE, BUTTON_SEARCH_TEXT
from taric_books import isbn_manager


class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'reto_taric.settings'
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter your book name here.")

        button = Tkinter.Button(self,text=BUTTON_SEARCH_TEXT, command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2, sticky='EW')
        self.labelVariable.set(u"Hello !")

        list_result_window = Tkinter.Tk()
        self.list_results = Tkinter.Listbox(list_result_window)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        # Show book search
        result = isbn_manager.search_by_author(self.entryVariable.get())
        self.populate_list(result)
        self.labelVariable.set(" (You clicked the button)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self, event):
        result = isbn_manager.search_by_author(self.entryVariable.get())
        self.populate_list(result)
        self.labelVariable.set(" (You pressed ENTER)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def populate_list(self, list):
        self.list_results.delete(0, Tkinter.END)
        for item in list:
            self.list_results.insert(Tkinter.END, item)
        self.list_results.pack()



if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title(APP_TITLE)
    app.mainloop()

# def DrawList():
#         plist = ['Liz','Tom','Chi']
#
#         for item in plist:
#                 listbox.insert(END,item);
#
#
# root = Tk()                     #This creates a window, but it won't show up
#
# listbox = Listbox(root)
# button = Button(root,text = "press me",command = DrawList)
#
# button.pack()
# listbox.pack()                  #this tells the listbox to come out
# root.mainloop()                 #This command will tell the window come out
