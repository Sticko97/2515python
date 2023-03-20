from pathlib import Path

from flask import Flask, jsonify, render_template, request

from database import db
from models import Product, Order, ProductsOrder

import tkinter as tk
from tkinter import messagebox

url = "http://127.0.0.1:5000/"


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)


@app.route("/")
def home():
    data = Product.query.all()
    return render_template("index.html", products=data)



@app.route("/api/product", methods=["POST"])
def api_create_product():
    data = request.json
    # Check all data is provided
    for key in ("name", "price", "quantity"):
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400
    try:
        price = float(data["price"])
        quantity = int(data["quantity"])
        # Make sure they are positive
        if price < 0 or quantity < 0:
            raise ValueError
    except ValueError:
        return (
            "Invalid values: price must be a positive float and quantity a positive integer",
            400,
        )

    product = Product(
        name=data["name"],
        price=price,
        quantity=quantity,
    )
    db.session.add(product)
    db.session.commit()
    return "Item added to the database"

@app.route("/api/product/<string:name>", methods=["GET"])
def api_get_product(name):
    product = Product.query.filter_by(name=name.lower()).first()
    if product is not None:
        product = db.session.get(Product, name.lower())
        product_json = product.to_dict()
        return jsonify(product_json)
    else:
        return jsonify({'error': 'Product not found'}), 404

@app.route("/api/product/<string:name>", methods=["DELETE"])
def api_delete_product(name):
    product = Product.query.filter_by(name=name.lower()).first()
    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully.'}), 200
    # if the product does not exist, return an error message
    else:
        return jsonify({'error': 'Product not found.'}), 404
        
    
@app.route("/api/product/<string:name>", methods=["PUT"])
def api_update_product(name):
    product = Product.query.filter_by(name=name.lower()).first()
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid data received'}), 404
    try:
        new_price = float(data.get('price'))
        new_quantity = int(data.get('quantity'))
    except ValueError:
        return jsonify({'error': 'Invalid data type for price or quantity'}), 400
    if new_price < 0 or new_quantity < 0:
        return jsonify({'error': 'Price or quantity cannot be negative'}), 400

    product.price = new_price
    product.quantity = new_quantity
    db.session.commit()
    return jsonify({'message': f'Product {product.name} updated successfully.'})

@app.route('/api/order/<int:order_id>', methods=['GET'])
def api_get_order(order_id):
    # Query the database to get the order with the specified ID
    order = Order.query.filter_by(id=order_id).first()

    # If no order was found, return a 404 error
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    # Convert the order to a dictionary using the to_dict method
    order_dict = order.to_dict()

    # Return the order dictionary as a JSON response
    return jsonify(order_dict)

@app.route('/api/order', methods=['POST'])
def api_create_order():
    json_data = request.json
    
    # Create a new Order instance with the customer name and address from the JSON
    new_order = Order(name=json_data['customer_name'], address=json_data['customer_address'])

    # Loop through the products in the JSON and add them to the new order
    for product_data in json_data['products']:
        # Get the product instance from the database based on the name in the JSON
        product = Product.query.filter_by(name=product_data['name']).first()

        # If the product doesn't exist, return a 400 error
        if product is None:
            return jsonify({'error': 'Product not found'}), 400

        # Create a new ProductsOrder instance with the product, quantity, and new order
        new_product_order = ProductsOrder(product=product, quantity=product_data['quantity'], order=new_order)

        # Add the new ProductsOrder instance to the new order's list of products
        new_order.products.append(new_product_order)

    # Add the new order to the database
    db.session.add(new_order)
    db.session.commit()

    # Return the JSON representation of the new order
    return jsonify(new_order.to_dict())

@app.route('/api/order/<int:order_id>', methods=['PUT'])
def api_process_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify(error="Order not found"), 404

    data = request.json
    if not data or 'process' not in data:
        return jsonify(error="Invalid payload"), 400

    if data['process'] and not order.completed:
        order.completed = True
        db.session.add()
        db.session.commit()

    return jsonify(order.to_dict())

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

if __name__ == "__main__":
    MyGUI() 
    app.run(debug=True)