from database import db


class Product(db.Model):
    name = db.Column(db.String, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    def to_dict(self):
        return {
            "name": self.name, 
            "price":self.price,
            "quantity":self.quantity
            }

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True) #unique # for order
    name = db.Column(db.String, nullable=False) #Customer name from order e.g. Tim
    address = db.Column(db.String, nullable=False)#Customer address from order e.g. Vancouver
    completed = db.Column(db.Boolean, default=False)#True means order has been processed
    products = db.relationship('ProductsOrder', back_populates='order')
    def to_dict(self):
        products_list = []
        total_price = 0
        
        for product_order in self.products:
            product_dict = {
                "name": product_order.product_name,
                "quantity": product_order.quantity,
                "price": product_order.quantity * product_order.product.price
            }
            products_list.append(product_dict)
            total_price += product_dict["price"]
            
        return {
            "customer_address": self.address,
            "customer_name": self.name,
            "products": products_list,
            "price": total_price
        }
    def process(self):
        # Check if order has already been processed
        if self.completed is False:
            # Check if there is enough inventory to fulfill the order
            for product_order in self.products:
                if product_order.product.quantity < product_order.quantity:
                    # Adjust the order to the maximum quantity available
                    product_order.quantity = product_order.product.quantity
                # Update the store inventory
                product_order.product.quantity -= product_order.quantity
        # Mark the order as completed
            self.completed = True
            db.session.commit()
        return 
    
class ProductsOrder(db.Model): 
    # Product foreign key is name 
    product_name = db.Column(db.ForeignKey("product.name"), primary_key=True)  # Order foreign key is ID 
    order_id = db.Column(db.ForeignKey("order.id"), primary_key=True)  # This is how many items we want 
    quantity = db.Column(db.Integer, nullable=False) 
    # Relationships and backreferences for SQL Alchemy 
    product = db.relationship('Product') 
    order = db.relationship('Order', back_populates='products')
    
    # def to_dict(self):
    #     return {
    #         "product_name": self.product_name,
    #         "quantity": self.quantity
    #     }
    