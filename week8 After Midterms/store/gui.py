import tkinter as tk
from tkinter import messagebox
from flask import Flask, jsonify, render_template, request
from database import db
from app import app
import requests
import json
from models import Product, Order, ProductsOrder
from pathlib import Path

"""TODO Checkbutton into a view order type of element
"""
url = "http://127.0.0.1:5000/"

def home():
    data = Product.query.all()
    return render_template("index.html", products=data)

class MyGUI:
    
    def __init__(self):
        #initialize tk
        self.root = tk.Tk()
        #Set title for GUI
        self.root.title("Shop Database GUI")
        
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
        #clear button
        self.clearbtn = tk.Button(self.root,text="clear", command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)
                
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

"""
#create or connect to a database
conn = db.create_all("store.db")
#create a cursor
cursor = db.conn.cursor()
#commit changes
conn.commit()
#close connection
conn.close()
"""