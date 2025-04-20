# src/file_handler.py
import csv

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        """
        Reads the data from the CSV file and returns a list of products.
        """
        products = []
        try:
            with open(self.file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products.append(row)
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        return products

    def write_data(self, data):
        """
        Writes the product data back to the CSV file.
        """
        try:
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Quantity", "Price", "Category"])
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            print(f"Error writing to file: {e}")
