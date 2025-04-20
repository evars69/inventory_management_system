# src/inventory.py
from src.file_handler import FileHandler

class Inventory:
    def __init__(self, file_path):
        self.file_handler = FileHandler(file_path)
        # If no products are loaded, add a sample product for testing
        self.products = self.file_handler.read_data() or [{"ID": "001", "Name": "Sample Product", "Quantity": 10, "Price": 50, "Category": "Miscellaneous"}]

    def add_product(self, product):
        self.products.append(product.to_dict())
        self.file_handler.write_data(self.products)

    def view_all(self):
        """
        Prints all products in the inventory.
        """
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(f"ID: {product['ID']}, Name: {product['Name']}, Quantity: {product['Quantity']}, Price: {product['Price']}, Category: {product['Category']}")

    def search(self, key):
        """
        Search products by name or ID.
        """
        return [p for p in self.products if key.lower() in p["Name"].lower() or key == p["ID"]]

    def update_product(self, product_id, updated_data):
        """
        Update product details based on the product ID.
        """
        for product in self.products:
            if product["ID"] == product_id:
                product.update(updated_data)
                self.file_handler.write_data(self.products)
                return True
        return False

    def delete_product(self, product_id):
        """
        Delete a product based on its ID.
        """
        new_list = [p for p in self.products if p["ID"] != product_id]
        if len(new_list) != len(self.products):
            self.products = new_list
            self.file_handler.write_data(self.products)
            return True
        return False

    def total_inventory_value(self):
        """
        Calculate and return the total value of all products in the inventory.
        """
        return sum(int(p["Quantity"]) * float(p["Price"]) for p in self.products)

    def low_stock_items(self, threshold=10):
        """
        Get a list of products that are below the low stock threshold.
        """
        return [p for p in self.products if int(p["Quantity"]) < threshold]

    def generate_report(self):
        """
        Generate a report of total inventory value and low-stock items.
        """
        total_value = self.total_inventory_value()
        print(f"Total Inventory Value: {total_value}")

        low_stock = self.low_stock_items()
        print("\nLow Stock Items (Quantity < 10):")
        if low_stock:
            for product in low_stock:
                print(f"ID: {product['ID']}, Name: {product['Name']}, Quantity: {product['Quantity']}, Price: {product['Price']}")
        else:
            print("No low stock items.")
