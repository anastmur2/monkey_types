from tkinter import *
from tkinter import ttk
import os
from ctypes import *
from pathlib import Path
import math

PAGE_SIZE = 15

def main():

    global lines, pages, curr_line, my_string_var, label

    cwd = os.getcwd()

    shared = Path(cwd) / "monkey.so"
    file = Path(cwd) / "isithamlet.txt"
    f = CDLL(shared)

    fp= open(file, 'r')
    
    lines = []
    for line in open(file):
        lines.append(line)

    root = Tk(className="Monkey")
    frm = ttk.Frame(root, padding=20)
    frm.grid(column=1, row=1)

    pages = math.ceil(len(lines) / PAGE_SIZE)

    curr_line = 0

    text = Text(root, wrap='word', state='disabled', width=100, height=30)

    my_string_var = StringVar()

    my_string_var.set("{} / ??".format(curr_line))

    # ttk.Label(frm, text="Hello World!").grid(column=1, row=0)
    label = ttk.Label(frm, textvariable=my_string_var)
    label.grid(column=1, row=2)
    ttk.Button(frm, text="<", command=lambda: update_text(True, text=text)).grid(column=0, row=1)
    ttk.Button(frm, text="Monkey, type!", command=lambda: retype(f, text)).grid(column=1, row=1)
    ttk.Button(frm, text=">", command=lambda: update_text(False, text=text)).grid(column=2, row=1)

    text.grid(column=1, row=0)

    root.mainloop()

def retype(f, text):
    global lines, pages, curr_line, my_string_var, label

    cwd = os.getcwd()

    file = Path(cwd) / "isithamlet.txt"

    fp= open(file, 'r')
    
    lines = []
    for line in open(file):
        lines.append(line)

    pages = math.ceil(len(lines) / PAGE_SIZE)

    curr_line = 1
    
    f.monkey_type()
    text.configure(state='normal')
    text.delete("1.0", "end")
    text.insert('end', "".join(lines[curr_line:curr_line+PAGE_SIZE]))
    text.update()
    text.configure(state='disabled')

    my_string_var.set("{} / {}".format(int(curr_line/PAGE_SIZE), pages))

def update_text(left, text: Text):
    global lines, pages, curr_line, my_string_var, label

    if(left and curr_line >= PAGE_SIZE ):
        curr_line -= PAGE_SIZE
    elif(not left and curr_line < ((pages - 1)*PAGE_SIZE)):
        curr_line += PAGE_SIZE
    
    print(curr_line)
    
    text.configure(state='normal')
    text.delete("1.0", "end")
    text.insert('end', "".join(lines[curr_line:curr_line+PAGE_SIZE]))
    text.update()
    text.configure(state='disabled')

    my_string_var.set("{} / {}".format(int(curr_line/PAGE_SIZE), pages))

if __name__ == "__main__":
   main()
