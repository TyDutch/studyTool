import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from time import *
from sys import *

class App():
    def __init__(self):
        self.root = tb.Window(themename="darkly")
        self.root.geometry('1280x720')
        self.root.title('Study Tool')
        
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)
        
        self.label = tk.Label(self.mainframe, text="Study Tool", font=("Arial", 18), foreground='black', background="white")
        self.label.pack(padx=20, pady=20)
        
        def update():
            time_string = strftime("%H:%M:%S %p")
            self.time.config(text=time_string)
            self.time.after(200,update)
        
        self.time = tk.Label(self.mainframe, font=("Arial", 40), foreground="black", background="white")
        self.time.pack(padx=20, pady=10, before=self.label)
        
        update()
        
        self.textbox = tk.Entry(self.mainframe, font="Arial",)
        self.textbox.pack()
        
        
        self.button = ttk.Button(self.mainframe, text="Submit",)
        self.button.pack(padx=20, pady=5)
        
        
        self.root.mainloop()
        return
    
if __name__ == '__main__':
    App()