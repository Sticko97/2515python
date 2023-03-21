import tkinter as tk
from tkinter import messagebox
from database import db
import requests

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# engine = create_engine("sqlite:///store.db")

url = "http://127.0.0.1:5000/"
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
        #Navbar file names e.g file, new, insert
        self.menubar.add_cascade(menu=self.filemenu, label="Filez")
        
        #Adding text to the GUI
        self.label = tk.Label(self.root, text="Stanley Le A00961484", font=("Arial", 12))
        self.label.pack(padx=10, pady=10)
        
        #Textbox for Creating Products
        self.labelCP = tk.Label(self.root, text="Create Products", font=("Arial", 12))
        self.labelCP.pack(padx=10, pady=10)
        #Product Name
        self.label = tk.Label(self.root, text="Enter Product Name", font=("Arial", 12))
        self.label.pack(padx=10, pady=10)
        self.textbox_name = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox_name.pack(padx=10, pady=5)
        #Product Price
        self.label = tk.Label(self.root, text="Enter Product Price", font=("Arial", 12))
        self.label.pack(padx=10, pady=10)
        self.textbox_price = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox_price.pack(padx=10, pady=5)
        #Product Quantity
        self.label = tk.Label(self.root, text="Enter Product Quantity", font=("Arial", 12))
        self.label.pack(padx=10, pady=10)
        self.textbox_quantity = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox_quantity.pack(padx=10, pady=5)
        
        
        #Textbox for Deleting Products
        self.labelDP = tk.Label(self.root, text="Delete Product", font=("Arial", 12))
        self.labelDP.pack(padx=10, pady=10)
        self.deleteBox_name = tk.Text(self.root,height=1, font=("Arial", 16))
        self.deleteBox_name.pack()
        # self.deleteBox_name.insert("1.0", "Enter Product Name")
        # self.deleteBox_name.tag_configure("placeholder", foreground="black")
        # self.deleteBox_name.tag_remove("placeholder" "1.0", "end")
        
        
        #state of the textbox, need "variable=self.check_state"
        #Can turn this into a view type of element~~~
        #Check Button
        # self.check_state = tk.IntVar()
        # self.check = tk.Checkbutton(self.root, text="show messagebox", font=("Arial", 12), variable=self.check_state)
        # self.check.pack(padx=10,pady=10)
        
        #Button Events
        #Show Storage
        self.showButton = tk.Button(self.root, text="Show Storage", font=("Arial", 12), command=self.show_storage)
        self.showButton.pack(padx=10, pady=10)
        
        #Create Product
        self.createButton = tk.Button(self.root, text="Create Product", font=("Arial", 12), command=self.api_create_product)
        self.createButton.pack(padx=10, pady=10)
        
        #Clear button
        self.clearButton = tk.Button(self.root,text="clear", command=self.clear)
        self.clearButton.pack(padx=10, pady=10)
                
        
        #Delete Button
        self.deleteButton = tk.Button(self.root,text="Delete Product", command=self.delete_product)
        self.deleteButton.pack(padx=10, pady=10)
    
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    #Clear button to delete text in text boxes
    def clear(self):
        self.textbox_name.delete("1.0", tk.END)
        self.textbox_price.delete("1.0", tk.END)
        self.textbox_quantity.delete("1.0", tk.END)
    
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            
    #Function to show products from database
    def show_storage(self):
        # retrieve all products from the API endpoint
        url = "http://127.0.0.1:5000/api/product"
        response = requests.get(url)
        # print(response.content)
        if response.status_code == 200:
            #Retrieve products from response
            products = response.json()
            
            #Creates a new window which will be used to display storage
            storage_window = tk.Toplevel(self.root)
            storage_window.title("All Products")
            
            # Create a label and a listbox to display the products
            label = tk.Label(storage_window, text="All Products", font=("Arial", 24))
            label.pack(padx=10, pady=10)
            listbox = tk.Listbox(storage_window, height=25,width=50, font=("Arial", 12))
            listbox.pack()
            
            for product in products:
                # Insert products into listbox
                listbox.insert(tk.END, f"{product['name']}  ${product['price']}  Quantity: {product['quantity']}")
        else:
            messagebox.showerror("Error", f"Error retrieving products from the database: {response.text}")
    
    #Function to add products to the database
    def api_create_product(self):
        url = "http://127.0.0.1:5000/api/product"
        data = {
            "name": self.textbox_name.get("1.0", tk.END).strip(),
            "price": self.textbox_price.get("1.0", tk.END).strip(),
            "quantity": self.textbox_quantity.get("1.0", tk.END).strip()
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Item added to the database")
        else:
            messagebox.showerror("Error", f"Error adding item to the database: {response.text}")
    
    def api_update_product(self):
        pass
    
    # def delete_product(self):
    #     url = "http://127.0.0.1:5000/api/product/<string:name>"
    #     data = {
    #     "name": self.deleteBox_name.get("1.0", tk.END).strip()
    #     }
    #     response = requests.delete(url,json=data)
    #     print(response)
    #     if response.status_code == 200:
    #         messagebox.showinfo("Success", "Item deleted from database")
    #     else:
    #         messagebox.showerror("Error", f"Error deleting product from database: {response.text}")
    def delete_product(self):
        name = self.deleteBox_name.get("1.0", tk.END).strip()
        url = f"http://127.0.0.1:5000/api/product/{name}"
        response = requests.delete(url)
        if response.status_code == 200:
            messagebox.showinfo("Success", f"{name} deleted from database")
        else:
            messagebox.showerror("Error", f"Error deleting {name} from database: {response.text}")
        
MyGUI()

