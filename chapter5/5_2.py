#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Tkinter

top = Tkinter.Tk()
quit_btn = Tkinter.Button(top, text='Hello World', command=top.quit)
quit_btn.pack()
Tkinter.mainloop()
