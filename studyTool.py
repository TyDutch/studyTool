import tkinter as tk
from tkinter import ttk
from time import *
from sys import *

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1280x720')
        self.root.title('Study Tool')
        
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)
        
        self.label = ttk.Label(self.mainframe, text="Study Tool", font=("Arial", 18), background='white')
        self.label.pack(padx=20, pady=20)
        
        def update():
            time_string = strftime("%H:%M:%S %p")
            self.time.config(text=time_string)
            self.time.after(200,update)
        
        self.time = ttk.Label(self.mainframe, font=("Arial", 40), foreground="black", background='white')
        self.time.pack(padx=20, pady=10, before=self.label)
        
        update()
        
        self.root.mainloop()
        return
    
if __name__ == '__main__':
    App()