#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tkinter as tk

top = tk.Tk()
quit_btn = tk.Button(top, text='Hello World', command=top.quit)
quit_btn.pack()
top.mainloop()
