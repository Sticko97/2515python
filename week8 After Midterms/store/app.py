from pathlib import Path

from flask import Flask, jsonify, render_template, request

from database import db
from models import Product, Order, ProductsOrder

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
    
@app.route("/api/product", methods=["GET"])
def api_show_storage():
    products = Product.query.all()
    product_list = [product.to_dict() for product in products]
    return jsonify(product_list)

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

#GUI code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def get_all_products():
#     try:
#         products = Product.query.all()
#         return [product.to_dict() for product in products]
#     except Exception as e:
#         print(f"Error retrieving products from database {str(e)}")
#         return []
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == "__main__":
    app.run(debug=True)