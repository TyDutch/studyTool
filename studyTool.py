#App Imports
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from time import *
from sys import *

#App Start
class App():
    def __init__(self):
        #App Parameters
        self.root = tb.Window(themename="darkly")
        self.root.geometry('600x600')
        self.root.title('Study Tool')
        
        #App Frame
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)
        
        #Update Clock Function
        def update():
            time_string = strftime("%H:%M:%S %p")
            self.time.config(text=time_string)
            self.time.after(200,update)    
        
        #Clock Label
        self.time = tk.Label(self.mainframe, font=("Arial", 40), foreground="black", background="white")
        self.time.pack(padx=20, pady=2)
        
        update()
        
        #To-Do Label
        self.label = tk.Label(self.mainframe, text="To-Do", font=("Arial", 18), foreground='black', background="white")
        self.label.pack(padx=10, pady=5)
        
        #Get Data Function
        def getData():
            global list_data
            list_data = []
            try:
                with open("save.txt", "r", encoding="utf-8") as file:
                    for f in file:
                        self.listBox.insert(tk.END, f.strip())
                        list_data.append(f.strip())
                        print(list_data)
            except:
                pass
        
        #Function that Adds Items to Listbox        
        def addItem(event=1):
            global list_data
            if content.get() != "":
                self.listBox.insert(tk.END, content.get())
                list_data.append(content.get())
                content.set("")
        
        #Set our input into a string        
        content = tk.StringVar()
        
        #Entry Textbox   
        self.textbox = ttk.Entry(self.mainframe, textvariable=content, font="Arial")
        self.textbox.pack()
        
        #List Box
        self.listBox = tk.Listbox(self.mainframe, font="Arial", selectmode="multiple")
        self.listBox.pack(padx=20, pady=10)
        
        #Submit Button
        self.button = ttk.Button(self.mainframe, text="Submit", command=addItem)
        self.button.pack(padx=20, pady=5, before=self.listBox)
        
        #Delete Selected Entries Function
        def deleteEntry():
            try:
                selected = self.listBox.get(self.listBox.curselection())
                self.listBox.delete(self.listBox.curselection())
                list_data.pop(list_data.index(selected))
                self.listBox.selection_set(0)
                self.listBox.activate(0)
                self.listBox.event_generate("<<ListboxSelect>>")
                print(self.listBox.curselection())
            except:
                pass
        
        #Delete Button
        self.deleteButton = ttk.Button(self.mainframe, text="Delete Entry", command=deleteEntry)
        self.deleteButton.pack(padx=20, pady=5)
        
        #Delete All Entries Function
        def deleteAllEntries():
            global list_data
            self.listBox.delete(0, tk.END)
            list_data = []
        
        #Delete All Entries Button
        self.deleteAllButton = ttk.Button(self.mainframe ,text="Delete All", command=deleteAllEntries)
        self.deleteAllButton.pack(padx=20)
        
        #Quit and Save Function
        def quitAndSave():
            with open("save.txt", "w", encoding="utf-8") as file:
                for d in list_data:
                    file.write(d + "\n")
                self.root.destroy()
            
        
        #Quit and Save Button
        self.qbutton = ttk.Button(self.mainframe, text="Quit", command=quitAndSave)
        self.qbutton.pack(padx=20, pady=5)
        
        getData()
        self.root.mainloop()
        return
    
if __name__ == '__main__':
    App()