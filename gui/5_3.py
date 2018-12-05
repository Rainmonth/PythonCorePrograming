#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tkinter as tk

top = tk.Tk()
hello_label = tk.Label(top, text='Hello World')
hello_label.pack()

quit_btn = tk.Button(top, text='Quit', command=top.quit, bg='red', fg='white')
quit_btn.pack(fill=tk.X, expand=1)
top.mainloop()
