import tkinter as tk
from tkinter import *
from tkinter import messagebox
from database import db
import requests

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# engine = create_engine("sqlite:///store.db")

"""TODO 
uncomment on_closing functions when project finished
turn text into entry and update functions when doing so


"""

url = "http://127.0.0.1:5000/"
class MyGUI:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        self.root.title("Shop Database GUI")

        # Create Products section
        self.create_products_frame = tk.Frame(self.root)
        self.create_products_frame.grid(row=0, column=0, padx=10, pady=10)

        self.labelCP = tk.Label(self.create_products_frame, text="Create Products by entering Product Name,#,# in Boxes", font=("Arial", 12))
        self.labelCP.grid(row=0, column=0, padx=10, pady=10)

        self.label_name = tk.Label(self.create_products_frame, text="Enter Product Name", font=("Arial", 12))
        self.label_name.grid(row=1, column=0, padx=10, pady=10)
        self.textbox_name = tk.Entry(self.create_products_frame, font=("Arial", 16))
        self.textbox_name.grid(row=1, column=1)

        self.label_price = tk.Label(self.create_products_frame, text="Enter Product Price", font=("Arial", 12))
        self.label_price.grid(row=2, column=0, padx=6, pady=6)
        self.textbox_price = tk.Entry(self.create_products_frame, font=("Arial", 16))
        self.textbox_price.grid(row=2, column=1, padx=6, pady=5)

        self.label_quantity = tk.Label(self.create_products_frame, text="Enter Product Quantity", font=("Arial", 12))
        self.label_quantity.grid(row=3, column=0, padx=6, pady=6)
        self.textbox_quantity = tk.Entry(self.create_products_frame, font=("Arial", 16))
        self.textbox_quantity.grid(row=3, column=1, padx=6, pady=5)

        self.createButton = tk.Button(self.create_products_frame, text="Create Product", font=("Arial", 12), command=self.create_product)
        self.createButton.grid(row=4, column=0, padx=6, pady=6)

        # Update Product Button
        self.updateButton = tk.Button(self.root, text="Update Product", font=("Arial", 12), command=self.update_product)
        self.updateButton.grid(row=5, column=5, padx=6, pady=6)

        # Delete Product section
        self.delete_products_frame = tk.Frame(self.root)
        self.delete_products_frame.grid(row=4, column=0, padx=6, pady=6)

        self.label_delete = tk.Label(self.delete_products_frame, text="Delete Products by entering Product Name in Box", font=("Arial", 12))
        self.label_delete.grid(row=0, column=0, padx=6, pady=6)

        self.deleteBox_name = tk.Text(self.delete_products_frame, height=1, font=("Arial", 16))
        self.deleteBox_name.insert("1.0", "Enter Product Name")
        self.deleteBox_name.tag_configure("placeholder", foreground="black")
        self.deleteBox_name.tag_remove("placeholder" "1.0", "end")
        self.deleteBox_name.grid(row=1, column=0, padx=6, pady=5)
        
        self.deleteButton = tk.Button(self.delete_products_frame, text="Delete Product", command=self.delete_product)
        self.deleteButton.grid(row=1, column=1, padx=6, pady=6)
        
        # Products section
        self.products_frame = tk.Frame(self.root)
        self.products_frame.grid(row=5, column=0, padx=10, pady=10)

        #Button Events
        #Show Storage
        self.showButton = tk.Button(self.products_frame, text="Show Storage", font=("Arial", 12), command=self.show_storage)
        self.showButton.grid(row=0, column=0, padx=10, pady=10)

        self.clearButton = tk.Button(self.products_frame, text="clear", command=self.clear)
        self.clearButton.grid(row=0, column=1, padx=10, pady=10)

        self.createOrder = tk.Button(self.products_frame, text="Create Order", command=self.create_order)
        self.createOrder.grid(row=0, column=2, padx=10, pady=10)

        self.customer_name_label = tk.Label(self.products_frame, text="Customer Name", font=("Arial", 12))
        self.customer_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.customer_name = tk.Entry(self.products_frame, font=("Arial", 16))
        self.customer_name.grid(row=1, column=1, padx=10, pady=10)

        self.customer_address_label = tk.Label(self.products_frame, text="Customer Address", font=("Arial", 12))
        self.customer_address_label.grid(row=2, column=0, padx=10, pady=10)
        self.customer_address = tk.Entry(self.products_frame, font=("Arial", 16))
        self.customer_address.grid(row=2, column=1, padx=10, pady=10)

        self.producttestbox_label = tk.Label(self.products_frame, text="Product", font=("Arial", 12))
        self.producttestbox_label.grid(row=3, column=0, padx=10, pady=10)
        self.producttestbox = tk.Entry(self.products_frame,font=("Arial", 16))
        self.producttestbox.grid(row=3, column=1, padx=10, pady=10)
        
        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    #Clear button to delete text in text boxes
    def clear(self):
        self.textbox_name.delete(0, tk.END)
        self.textbox_price.delete(0, tk.END)
        self.textbox_quantity.delete(0, tk.END)
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
            "name": self.textbox_name.get().strip(),
            "price": self.textbox_price.get().strip(),
            "quantity": self.textbox_quantity.get().strip()
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Item added to the database")
        else:
            messagebox.showerror("Error", f"Error adding item to the database: {response.text}")
    
    def update_product(self):
        name = self.textbox_name.get().strip()
        url = f"http://127.0.0.1:5000/api/product/{name}"
        data = {
            "name": self.textbox_name.get().strip(),
            "price": self.textbox_price.get().strip(),
            "quantity": self.textbox_quantity.get().strip()
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

