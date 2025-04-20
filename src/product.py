# src/product.py

class Product:
    def __init__(self, product_id, name, quantity, price, category):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def to_dict(self):
        """
        Convert the product attributes to a dictionary representation.
        Useful for saving data into CSV or any structured format.
        """
        return {
            "ID": self.product_id,
            "Name": self.name,
            "Quantity": self.quantity,
            "Price": self.price,
            "Category": self.category
        }

    def __str__(self):
        """
        Provide a string representation for easy printing of product details.
        """
        return f"ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Category: {self.category}"
