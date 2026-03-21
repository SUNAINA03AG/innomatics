# FastAPI Product Inventory API

## Project Overview

This project is a simple **Product Inventory API** built using **FastAPI**.
It demonstrates basic REST API operations such as **Create, Read, Update, and Delete (CRUD)** for managing products.

The API also includes additional features like **product inventory audit** and **bulk discount for product categories**.

This project was created as part of a **FastAPI assignment** to practice backend API development.

---

## Technologies Used

* Python
* FastAPI
* Uvicorn

---

## Initial Product Data

The API starts with the following dataset:

| ID | Name           | Price | Category    | In Stock |
| -- | -------------- | ----- | ----------- | -------- |
| 1  | Wireless Mouse | 499   | Electronics | True     |
| 2  | Notebook       | 99    | Stationery  | True     |
| 3  | USB Hub        | 799   | Electronics | False    |
| 4  | Pen Set        | 49    | Stationery  | True     |

---

## API Endpoints

### 1. Get All Products

Endpoint:

GET /products

Description:
Returns all available products and the total number of products.

---

### 2. Add Product

Endpoint:

POST /products

Description:
Adds a new product to the inventory.

Example Request Body:

{
"name": "Keyboard",
"price": 899,
"category": "Electronics",
"in_stock": true
}

---

### 3. Product Audit

Endpoint:

GET /products/audit

Description:
Provides inventory statistics such as:

* Total number of products
* Number of products in stock
* Names of out-of-stock products
* Total stock value
* Most expensive product

---

### 4. Bulk Discount (Bonus)

Endpoint:

PUT /products/discount

Description:
Applies a discount percentage to all products in a given category.

Parameters:

category
discount_percent

Example:

category = Electronics
discount_percent = 10

---

### 5. Get Product by ID

Endpoint:

GET /products/{product_id}

Description:
Returns details of a specific product using its ID.

---

### 6. Update Product

Endpoint:

PUT /products/{product_id}

Description:
Updates the price or stock status of a product.

Example:

product_id = 1
price = 450
in_stock = true

---

### 7. Delete Product

Endpoint:

DELETE /products/{product_id}

Description:
Removes a product from the inventory.

---

## How to Run the Project

### 1. Install Dependencies

pip install fastapi uvicorn

### 2. Run the Server

uvicorn main:app --reload

### 3. Open API Documentation

Open the browser and go to:

http://127.0.0.1:8000/docs

Swagger UI will open where you can test all API endpoints.

---

## Conclusion

This project demonstrates how to build a simple backend API using FastAPI with CRUD operations and additional features such as product auditing and bulk discount functionality.

