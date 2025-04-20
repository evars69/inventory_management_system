# src/main.py
from src.inventory import Inventory
from src.product import Product

def main():
    # Initialize Inventory
    inventory = Inventory('data/products.csv')

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Generate Report")
        print("7. Exit")

        # Taking user choice
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:  # Add Product
            product_id = input("Product ID: ")
            name = input("Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            category = input("Category: ")
            product = Product(product_id, name, quantity, price, category)
            inventory.add_product(product)
            print(f"Product {name} added successfully!")

        elif choice == 2:  # View All Products
            inventory.view_all()

        elif choice == 3:  # Search Product
            key = input("Enter product name or ID to search: ")
            results = inventory.search(key)
            if results:
                for product in results:
                    print(product)
            else:
                print("No products found matching your search.")

        elif choice == 4:  # Update Product
            product_id = input("Enter Product ID to update: ")
            updated_data = {}
            updated_data["Name"] = input("New Name (leave blank to keep existing): ") or None
            updated_data["Quantity"] = input("New Quantity (leave blank to keep existing): ") or None
            updated_data["Price"] = input("New Price (leave blank to keep existing): ") or None
            updated_data["Category"] = input("New Category (leave blank to keep existing): ") or None

            # Filter out None values
            updated_data = {k: v for k, v in updated_data.items() if v is not None}

            if inventory.update_product(product_id, updated_data):
                print("Product updated successfully.")
            else:
                print("Product not found.")

        elif choice == 5:  # Delete Product
            product_id = input("Enter Product ID to delete: ")
            if inventory.delete_product(product_id):
                print(f"Product {product_id} deleted successfully.")
            else:
                print("Product not found.")

        elif choice == 6:  # Generate Report
            inventory.generate_report()

        elif choice == 7:  # Exit
            print("Exiting the system.")
            break  # Exit the loop

        else:
            print("Invalid choice. Please choose a valid option (1-7).")

if __name__ == "__main__":
    main()
