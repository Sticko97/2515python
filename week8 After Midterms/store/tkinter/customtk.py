import customtkinter
import sqlite3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x500")

def login():
    print("HEllo world")
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Arial",24))
label.pack(pady=12, padx=10)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2= customtkinter.CTkEntry(master=frame, placeholder_text="Password")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Rembr me")
checkbox.pack(pady=12,padx=10)

root.mainloop()

"""
import tkinter as tk
from tkinter import messagebox
from database import db
import requests

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# engine = create_engine("sqlite:///store.db")

"""TODO uncomment on_closing functions when project finished
"""

url = "http://127.0.0.1:5000/"
class MyGUI:
    
    def __init__(self):
        #initialize tk
        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        #Set title for GUI
        self.root.title("Shop Database GUI")
        self.buttonframe = tk.Frame(self.root)
        
        #Textbox for Creating Products
        self.labelCP = tk.Label(self.root, text="Create Products by entering Product Name,#,# in Boxs", font=("Arial", 12))
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
        
        #Create Product Button
        self.createButton = tk.Button(self.root, text="Create Product", font=("Arial", 12), command=self.create_product)
        self.createButton.pack(padx=10, pady=10)
        
        #Update Product Button
        self.updateButton = tk.Button(self.root, text="Update Product", font=("Arial", 12), command=self.update_product)
        self.updateButton.pack(padx=10, pady=10)
        
        #Textbox for Deleting Products
        #Delete Button
        self.deleteBox_name = tk.Text(self.root,height=1, font=("Arial", 16))
        self.deleteBox_name.insert("1.0", "Enter Product Name")
        self.deleteBox_name.tag_configure("placeholder", foreground="black")
        self.deleteBox_name.tag_remove("placeholder" "1.0", "end")
        self.deleteBox_name.pack()
        self.deleteButton = tk.Button(self.root,text="Delete Product", command=self.delete_product)
        self.deleteButton.pack(padx=10, pady=10)
        
        
        
        #state of the textbox, need "variable=self.check_state"
        #Can turn this into a view type of element~~~
        #Check Button
        # self.check_state = tk.IntVar()
        # self.check = tk.Checkbutton(self.root, text="show messagebox", font=("Arial", 12), variable=self.check_state)
        # self.check.pack(padx=10,pady=10)
        
        
        #Button Events
        #Show Storage
        # self.showButton = tk.Button(self.root, text="Show Storage", font=("Arial", 12), command=self.show_storage)
        # self.showButton.pack(padx=10, pady=10)
        showButton = tk.Button(self.buttonframe, text="View All Products", font=("Arial", 18),command=self.show_storage)
        showButton.grid(row=0,column=0,sticky=tk.W+tk.E)
        self.buttonframe.pack()
        
        
        #Clear button
        self.clearButton = tk.Button(self.root,text="clear", command=self.clear)
        self.clearButton.pack(padx=10, pady=10)
        
        self.createOrder = tk.Button(self.root,text="Create Order", command=self.create_order)
        self.createOrder.pack(padx=10, pady=10)
        self.customer_name = tk.Entry(self.root, font=("Arial", 16))
        self.customer_name.pack(padx=10, pady=10)
        self.customer_address = tk.Entry(self.root, font=("Arial", 16))
        self.customer_address.pack(padx=10, pady=10)
        self.producttestbox = tk.Entry(self.root,font=("Arial", 16))
        self.producttestbox.pack(padx=10, pady=10)

        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.buttonframe.pack()
        self.root.mainloop()
    
    #Clear button to delete text in text boxes
    def clear(self):
        self.textbox_name.delete("1.0", tk.END)
        self.textbox_price.delete("1.0", tk.END)
        self.textbox_quantity.delete("1.0", tk.END)
        self.deleteBox_name.delete("1.0", tk.END)
        
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # def on_closing(self):
    #     if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #         self.root.destroy()
            
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
    def create_product(self):
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
    
    def update_product(self):
        name = self.textbox_name.get("1.0", tk.END).strip()
        url = f"http://127.0.0.1:5000/api/product/{name}"
        data = {
            "name": self.textbox_name.get("1.0", tk.END).strip(),
            "price": self.textbox_price.get("1.0", tk.END).strip(),
            "quantity": self.textbox_quantity.get("1.0", tk.END).strip()
        }
        response = requests.put(url, json=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", f"{name} updated in Storage")
        else:
            messagebox.showerror("Error", f"Error updating {name}: {response.text}")            
    
    def delete_product(self):
        name = self.deleteBox_name.get("1.0", tk.END).strip()
        url = f"http://127.0.0.1:5000/api/product/{name}"
        response = requests.delete(url)
        if response.status_code == 200:
            messagebox.showinfo("Success", f"{name} deleted from database")
        else:
            messagebox.showerror("Error", f"Error deleting {name} from database: {response.text}")
            
    def create_order(self):
        # Get the customer name and address from the GUI text boxes
        customer_name = self.customer_name.get().strip()
        customer_address = self.customer_address.get().strip()

        # Get the list of products from the GUI text box
        products_str = self.producttestbox.get().strip()
        products = []

        # Parse the product list and create a dictionary for each product with its name and quantity
        for line in products_str.split("\n"):
            if line.strip():
                name, quantity = line.split(",")
                products.append({"name": name.strip(), "quantity": int(quantity.strip())})

        # Create the data dictionary to send in the POST request
        data = {"customer_name": customer_name, "customer_address": customer_address, "products": products}

        # Send the POST request to the API endpoint
        url = "http://127.0.0.1:5000/api/order"
        response = requests.post(url, json=data)

        # Handle the response
        if response.status_code == 200:
            order = response.json()
            messagebox.showinfo("Success", f"Order created with ID: {order['id']}")
        else:
            messagebox.showerror("Error", f"Error creating order: {response.text}")
        
MyGUI()


    """