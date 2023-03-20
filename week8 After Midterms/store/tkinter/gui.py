import tkinter as tk
from tkinter import messagebox
import sqlite3
"""TODO Checkbutton into a view order type of element
"""

class MyGUI:
    
    def __init__(self):
        
        self.root = tk.Tk()
        
        #navbar, things like file menu
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.on_closing)
        self.filemenu.add_command(label="View", command=self.on_closing)
        self.filemenu.add_separator()
        self.root.config(menu=self.menubar)
        
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="this", command=self.show_message)
        
        self.menubar.add_cascade(menu=self.filemenu, label="Filez")
        self.menubar.add_cascade(menu=self.actionmenu, label="Actionz")
        
        #Adding text to the GUI
        self.label = tk.Label(self.root, text="Your message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)
        #Textbox
        self.textbox = tk.Text(self.root,height=3 ,font=("Arial", 16))
        self.textbox.pack(padx=10)
        
        #state of the textbox, need "variable=self.check_state"
        #Can turn this into a view type of element~~~
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="show messagebox", font=("Arial", 18), variable=self.check_state)
        self.check.pack(padx=10,pady=10)
        
        #buttons
        self.button = tk.Button(self.root, text="show message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        self.clearbtn = tk.Button(self.root,text="clear", command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)
        

        # self.buttonframe = tk.Frame(self.root)
        # self.buttonframe.columnconfigure(0, weight=1)
        # self.buttonframe.columnconfigure(1, weight=1)
        # self.buttonframe.columnconfigure(2, weight=1)

        # btn1 = tk.Button(self.buttonframe, text="View All Products", font=("Arial", 18))
        # btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
        # btn2 = tk.Button(self.buttonframe, text="Add a Product", font=("Arial", 18))
        # btn2.grid(row=0,column=1,sticky=tk.W+tk.E)
        # btn3 = tk.Button(self.buttonframe, text="Update a Product", font=("Arial", 18))
        # btn3.grid(row=0,column=2,sticky=tk.W+tk.E)
        # btn3 = tk.Button(self.buttonframe, text="Delete Product", font=("Arial", 18))
        # btn3.grid(row=0,column=3,sticky=tk.W+tk.E)
        # btn4 = tk.Button(self.buttonframe, text="Create an Order", font=("Arial", 18))
        # btn4.grid(row=1,column=0,sticky=tk.W+tk.E)
        # btn5 = tk.Button(self.buttonframe, text="View an Order", font=("Arial", 18))
        # btn5.grid(row=1,column=1,sticky=tk.W+tk.E)
        # btn6 = tk.Button(self.buttonframe, text="Delete an Order", font=("Arial", 18))
        # btn6.grid(row=1,column=2,sticky=tk.W+tk.E)
        # btn7 = tk.Button(self.buttonframe, text="Process an Order", font=("Arial", 18))
        # btn7.grid(row=1,column=3,sticky=tk.W+tk.E)
        # btn8 = tk.Button(self.buttonframe, text="View Pending Orders", font=("Arial", 18))
        # btn8.grid(row=2,column=0,sticky=tk.W+tk.E)
        # btn9 = tk.Button(self.buttonframe, text="View Processed Orders", font=("Arial", 18))
        # btn9.grid(row=2,column=1,sticky=tk.W+tk.E)
        # btn10 = tk.Button(self.buttonframe, text="View Products out of stock", font=("Arial", 18))
        # btn10.grid(row=2,column=2,sticky=tk.W+tk.E)
        # btn11 = tk.Button(self.buttonframe, text="Find Customer Order", font=("Arial", 18))
        # btn11.grid(row=2,column=3,sticky=tk.W+tk.E)
        # btn12 = tk.Button(self.buttonframe, text="View an Order", font=("Arial", 18))
        # btn12.grid(row=3,column=0,sticky=tk.W+tk.E)
        # self.buttonframe.pack()
        
        

        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    #make it so it displays orders?
    def show_message(self):
        if self.check_state.get() == 0:
            #index "1.0" is the start of the string
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))
    
    def clear(self):
        self.textbox.delete("1.0", tk.END)
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
MyGUI()