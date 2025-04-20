# 🧾 Inventory Management System

> 📦 **Track It. Manage It. Own It.**

A sleek and powerful command-line-based Inventory Management System that helps you manage your product stock effortlessly. Whether you're running a boutique store or managing warehouse items — this system has your back with smooth operations and reliable storage using both CSV and JSON formats.

---

## 🔍 Features

* ➕ **Add Product** — Insert new stock details with ease.
* 📋 **View All Products** — Get a full list of what's in store.
* 🔎 **Search Product** — Search by name or ID in a flash.
* ✏️ **Update Product** — Modify any product info in a snap.
* ❌ **Delete Product** — Remove outdated or unavailable items.
* 📊 **Generate Report** — Get total value and low-stock alerts.
* 🧠 **Smart Storage** — Use either CSV or JSON file formats.

---

## 🗂️ Project Structure

inventory_management_system/
├── src/
│   ├── main.py            # 🔁 CLI interface logic
│   ├── product.py         # 🧱 Product class model
│   ├── inventory.py       # ⚙️ Inventory operations
│   └── file_handler.py    # 📄 CSV/JSON reading and writing
│
├── data/
│   ├── products.csv       # 📂 CSV-based storage
│   └── products.json      # 📂 JSON-based storage
│
└── README.md              # 📘 This documentation file

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

* Python 3.x installed
* Terminal / Command Prompt access

### 🚀 Installation

* git clone https://github.com/evars69/inventory_management_system.git
* cd inventory_management_system
* python -m src.main

No fancy libraries — all you need is native Python 💪.

---

## 🎮 Usage Guide

Once you run the program, you'll see:

---
--- Inventory Management System ---
1. Add Product
2. View All Products
3. Search Product
4. Update Product
5. Delete Product
6. Generate Report
7. Exit
---
Pick an option (1-7) and follow the prompts.
It’s smooth, fast, and beginner-friendly 🌱.

---

## 🧾 Supported Formats

### 📄 CSV

Stored in `data/products.csv`

Each entry:

ID,Name,Quantity,Price,Category
201,Laptop,10,35000,Electronics
202,Shirt,25,799,Fashion

### 🗃️ JSON

Stored in `data/products.json`

Each entry:

    [

    {

    "ID": "109",

    "Name": "Formal Shirt",

    "Quantity": 11,

    "Price": 1600,

    "Category": "Men"

    },

    {

    "ID": "110",

    "Name": "Face Wash",

    "Quantity": 18,

    "Price": 300,

    "Category": "Skincare"

    }

]

Both formats are managed through `file_handler.py`. You can switch easily based on your preference.

---

## 📈 Reporting Feature

* Calculates **Total Inventory Value**
* Lists **Low Stock Items** (quantity < 10)
* Helps you **restock smartly** 🧠

---

## 🤝 Contributing

Pull Requests are welcome!

If you want to fix bugs, add features, or improve the UI/UX — feel free to fork the repo, create a branch, and send in that PR 💌

---

## ⚖️ License

* Do whatever you want with it — just don't forget to give credit where due 😉

---

## 👩‍💻 Made with patience, Python, and power

> by Varsha 💜
