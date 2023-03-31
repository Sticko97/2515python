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


"""

url = "http://127.0.0.1:5000/"
class MyGUI:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Shop Database GUI")
        self.root.columnconfigure(0, weight=1)

        # Create Products section
        self.create_products_frame = tk.Frame(self.root)
        self.create_products_frame.grid(row=0, column=0, padx=10, pady=10)

        self.labelCP = tk.Label(self.create_products_frame, text="Create Products by entering Product Name,#,# in Boxes", font=("Arial", 12))
        self.labelCP.grid(row=0, column=1, padx=10, pady=10)

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
        self.updateButton = tk.Button(self.create_products_frame, text="Update Product", font=("Arial", 12), command=self.update_product)
        self.updateButton.grid(row=4, column=1, padx=6, pady=6)

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
        self.deleteButton.grid(row=2, column=0, padx=6, pady=6)
        
        # Products section
        self.products_frame = tk.Frame(self.root)
        self.products_frame.grid(row=5, column=0, padx=10, pady=10)

        #Button Events
        #Show Storage
        self.showButton = tk.Button(self.products_frame, text="Show Storage", font=("Arial", 12), command=self.show_storage)
        self.showButton.grid(row=0, column=0, padx=10, pady=10)

        self.clearButton = tk.Button(self.products_frame, text="clear", command=self.clear)
        self.clearButton.grid(row=0, column=1, padx=10, pady=10)
        
        self.orders=[]
        
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
            # Retrieve products from response
            products = response.json()

            # Create a new window which will be used to display storage
            self.storage_window = tk.Toplevel(self.root)
            self.storage_window.title("All Products")
            self.storage_window.columnconfigure(0, weight=1)
            self.storage_window.rowconfigure(0, weight=1)
            self.storage_window.rowconfigure(1, weight=1)

            product_frame = tk.Frame(self.storage_window)
            product_frame.grid(row=0, column=0)
            cust_order_frame = tk.Frame(self.storage_window)
            cust_order_frame.grid(row=1, column=0)

            # Create a label and a listbox to display the products
            label = tk.Label(product_frame, text="All Products", font=("Arial", 24))
            label.grid(row=0, column=0, pady=10)
            scrollbar = tk.Scrollbar(product_frame)
            scrollbar.grid(row=1, column=1)
            storage_listbox = tk.Listbox(product_frame, height=10, width=30, font=("Arial", 12), yscrollcommand=scrollbar.set)
            storage_listbox.grid(row=1, column=0)

            # Link the Scrollbar to the Listbox
            scrollbar.config(command=storage_listbox.yview)

            # Create Customer Order section
            self.customer_name_label = tk.Label(cust_order_frame, text="Customer Name", font=("Arial", 12))
            self.customer_name_label.grid(row=0, column=0, padx=10, pady=10)
            self.customer_name = tk.Entry(cust_order_frame, font=("Arial", 16))
            self.customer_name.grid(row=1, column=0, padx=10, pady=10)

            self.customer_address_label = tk.Label(cust_order_frame, text="Customer Address", font=("Arial", 12))
            self.customer_address_label.grid(row=0, column=1, padx=10, pady=10)
            self.customer_address = tk.Entry(cust_order_frame, font=("Arial", 16))
            self.customer_address.grid(row=1, column=1, padx=10, pady=10)

            self.producttestbox_label = tk.Label(cust_order_frame, text="Product", font=("Arial", 12))
            self.producttestbox_label.grid(row=0, column=2, padx=10, pady=10)
            self.producttestbox = tk.Listbox(cust_order_frame, selectmode="multiple", font=("Arial", 16))
            self.producttestbox.grid(row=1, column=2, padx=10, pady=10)

            product_quantity_label = tk.Label(cust_order_frame, text="Product Quantity:", font=("Arial", 12))
            product_quantity_label.grid(row=0, column=3, padx=10, pady=10)
            

            # Orders section ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            self.product_quantity_boxes = []
            for idx, product in enumerate(products):
                product_quantity_box = tk.Entry(cust_order_frame, font=("Arial", 12))
                product_quantity_box.grid(row=1, column=3+idx)
                self.product_quantity_boxes.append(product_quantity_box)

            self.createOrder = tk.Button(cust_order_frame, text="Create Order", command=self.create_order)
            self.createOrder.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
            
            self.viewOrder = tk.Button(cust_order_frame, text="View Orders", command=self.view_order)
            self.viewOrder.grid(row=2, column=1, padx=10, pady=10)
            
            for product in products:
                # Insert products into listbox
                storage_listbox.insert(tk.END, f"{product['name']}  ${product['price']}  Quantity: {product['quantity']}")
                # Add product name to product selection listbox
                self.producttestbox.insert(tk.END, product['name'])
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

        # Get the list of products and quantities from the GUI text boxes
        self.products_order = []
        for idx, product_name in enumerate(self.producttestbox.curselection()):
            product_name = self.producttestbox.get(product_name)
            product_quantity = int(self.product_quantity_boxes[idx].get().strip())
            self.products_order.append({"name": product_name, "quantity": product_quantity})

        # Create the data dictionary to send in the POST request
        data = {"customer_name": customer_name, "customer_address": customer_address, "products": self.products_order}

        # Send the POST request to the API endpoint
        url = "http://127.0.0.1:5000/api/order"
        response = requests.post(url, json=data)

        # Handle the response
        if response.status_code == 200:
            order = response.json()
            order_id = order['id']  # Get the 'id' from the response

            self.orders.append(order)

            # order window
            #TODO FIX THIS WINDOW
            self.order_window = tk.Toplevel()
            self.order_window.title("Order Created")
            self.order_listbox = tk.Listbox(self.order_window, height=50, width=50)
            self.order_listbox.pack()

            for product in self.products_order:
                # Retrieve the product details from the API
                url = f"http://127.0.0.1:5000/api/product/{product['name']}"
                response = requests.get(url)
                if response.status_code == 200:
                    product_data = response.json()
                    total_price = product_data['price'] * product['quantity']
                    # Insert product and total price into listbox
                    self.order_listbox.insert(tk.END, f"{product_data['name']}  Quantity: {product['quantity']}  Total Price: {total_price}")
                else:
                    messagebox.showerror("Error", f"Error retrieving product details: {response.text}")

            if order_id:
                messagebox.showinfo("Success", f"Order created with ID: {order_id}")
            else:
                messagebox.showwarning("Warning", "Order created but could not retrieve ID")
        else:
            messagebox.showerror("Error", f"Error creating order: {response.text}")
                
    def view_order(self):
        url = "http://127.0.0.1:5000/api/order"
        response = requests.get(url)

        if response.status_code == 200:
            orders = response.json()
            # print("Orders:", orders)

            # Create new window to display orders
            self.order_window = tk.Toplevel(self.root)
            self.order_window.title("All Orders")

            self.order_frame = tk.Frame(self.order_window)
            self.order_frame.pack()
            
            # Create a scrollbar for the listbox
            scrollbar = tk.Scrollbar(self.order_frame)


            # Create a listbox to display the orders
            self.order_listbox = tk.Listbox(self.order_frame, width=100, yscrollcommand=scrollbar.set)
            self.order_listbox.grid(row=0, column=1)

            # Link the scrollbar to the order_listbox
            scrollbar.config(command=self.order_listbox.yview)
            
            # Configure the grid weights
            self.order_frame.grid_rowconfigure(0, weight=1)
            self.order_frame.grid_columnconfigure(0, weight=1)
            

            # Populate the order_listbox with the order details
            for order in orders:
                self.order_listbox.insert(tk.END, f"Order ID: {order['order_id']}  Customer Name: {order['customer_name']}  Customer Address: {order['customer_address']}  Price: {order['price']}")
                for product in order['products']:
                    self.order_listbox.insert(tk.END, f"Product: {product['name']}  Quantity: {product['quantity']}  Price: {product['price']}")
                self.order_listbox.insert(tk.END, "")
            
            #update order with order id
            order_id_label = tk.Label(self.order_frame, text="Enter Order ID to Update")
            order_id_label.grid(row=4,column=0)
            self.order_id_entry = tk.Entry(self.order_frame)
            self.order_id_entry.grid(row=5,column=0)
            
            order_name_label = tk.Label(self.order_frame, text="Enter Product Name to Update")
            order_name_label.grid(row=4,column=1)
            self.order_product_name = tk.Entry(self.order_frame)
            self.order_product_name.grid(row=5,column=1)
            
            
            order_quantity_label = tk.Label(self.order_frame, text="Enter Product Quantity to Update")
            order_quantity_label.grid(row=4,column=2)
            self.order_product_quantity = tk.Entry(self.order_frame)
            self.order_product_quantity.grid(row=5,column=2)
            
            update_button = tk.Button(self.order_frame, text="Update", command=self.update_order)
            update_button.grid(row=7, column=1)

        else:
            messagebox.showerror("Error", f"Error retrieving orders from the database: {response.text}")
            
    def update_order(self):
        # Get the order ID from the entry box
        order_id = self.order_id_entry.get().strip()

        # Retrieve the order details from the API
        url = f"http://127.0.0.1:5000/api/order/{order_id}"
        response = requests.get(url)

        if response.status_code == 200:
            order = response.json()

            # Get the product name and new quantity from the entry boxes
            product_name = self.order_product_name.get().strip()
            new_quantity = int(self.order_product_quantity.get().strip())

            # Find the product in the order and update its quantity
            for product in order['products']:
                if product['name'] == product_name:
                    product['quantity'] = new_quantity

            # Send a PUT request to update the order with the new product quantity
            update_url = f"http://127.0.0.1:5000/api/order/{order_id}"
            response = requests.put(update_url, json=order)

            # Show a success message if the update was successful or an error message otherwise
            if response.status_code == 200:
                messagebox.showinfo("Success", f"Order {order_id} updated successfully.")
            else:
                messagebox.showerror("Error", f"Error updating order {order_id}: {response.text}")

        else:
            messagebox.showerror("Error", f"Error retrieving order {order_id}: {response.text}")
MyGUI()

    