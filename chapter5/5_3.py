#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Tkinter

top = Tkinter.Tk()
hello_label = Tkinter.Label(top, text='Hello World')
hello_label.pack()

quit_btn = Tkinter.Button(top, text='Quit', command=top.quit, bg='red', fg='white')
quit_btn.pack(fill=Tkinter.X, expand=1)
Tkinter.mainloop()
