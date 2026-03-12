# FastAPI Product Inventory API

## Project Overview

This project is a simple Product Inventory API built using FastAPI.
It demonstrates basic REST API operations such as creating, reading, updating, and deleting products.
The API also includes additional features like inventory audit and bulk discount application.

This project was created as part of a FastAPI assignment to practice building backend APIs and working with HTTP methods.

---

## Technologies Used

* Python
* FastAPI
* Uvicorn

---

## Initial Dataset

The API starts with the following product data:

| ID | Name           | Price | Category    | In Stock |
| -- | -------------- | ----- | ----------- | -------- |
| 1  | Wireless Mouse | 499   | Electronics | True     |
| 2  | Notebook       | 99    | Stationery  | True     |
| 3  | USB Hub        | 799   | Electronics | False    |
| 4  | Pen Set        | 49    | Stationery  | True     |

---

## API Endpoints

### 1. Get All Products

GET /products

Returns the list of all products and the total count.

---

### 2. Get Product By ID

GET /products/{product_id}

Returns details of a specific product.

Example:
GET /products/1

---

### 3. Add Product

POST /products

Adds a new product to the inventory.

Example JSON body:

{
"name": "Laptop Stand",
"price": 1299,
"category": "Electronics",
"in_stock": true
}

---

### 4. Update Product

PUT /products/{product_id}

Updates product price or stock availability.

Example:
PUT /products/3?price=699&in_stock=true

---

### 5. Delete Product

DELETE /products/{product_id}

Deletes a product from the inventory.

Example:
DELETE /products/4

---

### 6. Product Audit

GET /products/audit

Returns an inventory summary including:

* Total number of products
* Count of in-stock products
* Names of out-of-stock products
* Total stock value
* Most expensive product

---

### 7. Bulk Discount (Bonus)

PUT /products/discount

Applies a discount to all products in a specific category.

Parameters:

* category
* discount_percent

Example:
PUT /products/discount?category=Electronics&discount_percent=10

---

## Running the Project

### Step 1 – Install dependencies

pip install fastapi uvicorn

---

### Step 2 – Run the server

uvicorn main:app --reload

---

### Step 3 – Open API documentation

Open the browser and go to:

http://127.0.0.1:8000/docs

This will open the Swagger UI where all API endpoints can be tested.

---

## Project Structure

fastapi_project
│
├── main.py
└── README.md

---

## Conclusion

This project demonstrates how to build a RESTful API using FastAPI with CRUD operations, error handling, and additional functionality like inventory auditing and bulk discount management.

