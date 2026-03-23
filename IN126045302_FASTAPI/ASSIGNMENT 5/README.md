# FastAPI Search, Sort & Pagination – Assignment 5

## Project Overview

This project implements a simple **Product and Order API using FastAPI**.

The API provides core functionalities like searching products, sorting results, and paginating data. It also includes combined operations and order-related features.

This assignment demonstrates how real-world APIs handle filtering, sorting, and large datasets efficiently.

---

## Technologies Used

* Python
* FastAPI
* Uvicorn

---

## Features Implemented

* Search products using keywords (case-insensitive)
* Sort products by price and name
* Paginate product list
* Search orders by customer name
* Sort products by category and price
* Combine search, sort, and pagination in one endpoint
* Paginate orders list (Bonus)

---

## How to Run the Project

### 1. Install Required Packages

pip install fastapi uvicorn

### 2. Run the Server

uvicorn main:app --reload

### 3. Open API Documentation

Open the browser and go to:

http://127.0.0.1:8000/docs

Swagger UI will appear where all API endpoints can be tested.

---

## API Endpoints

| Method | Endpoint                   | Description                         |
| ------ | -------------------------- | ----------------------------------- |
| GET    | /products/search           | Search products by keyword          |
| GET    | /products/sort             | Sort products                       |
| GET    | /products/page             | Paginate products                   |
| GET    | /orders/search             | Search orders by customer name      |
| GET    | /products/sort-by-category | Sort by category then price         |
| GET    | /products/browse           | Search + Sort + Pagination combined |
| GET    | /orders/page               | Paginate orders (Bonus)             |

---

## Assignment Tasks Completed

### Q1 – Search Products

Tested product search using /products/search with different keywords.  
Verified case-insensitive behavior and handled no-result scenarios.

---

### Q2 – Sort Products

Tested sorting using /products/sort with different combinations:
- Price (ascending & descending)
- Name (A–Z)
- Handled invalid sorting field error

---

### Q3 – Pagination

Used /products/page to navigate product data:
- Verified multiple pages
- Handled empty page scenario
- Tested different limits

---

### Q4 – Search Orders

Implemented /orders/search to find orders by customer name.  
Verified case-insensitive search and no-result handling.

---

### Q5 – Sort by Category Then Price

Implemented /products/sort-by-category:
- Sorted products by category (A–Z)
- Sorted within category by price (ascending)

---

### Q6 – Combined Search, Sort & Pagination

Built /products/browse endpoint:
- Applied filtering using keyword
- Applied sorting
- Applied pagination
- Verified all combinations

---

### Bonus – Orders Pagination

Implemented /orders/page:
- Paginated orders list
- Verified correct page navigation and total pages

---

## Project Structure

YOUR_UNIQUE_INTERNID_FASTAPI
└── ASSIGNMENT 4
    ├── main.py
    ├── Q1_Output.png
    ├── Q2_Output.png
    ├── Q3_Output.png
    ├── Q4_Output.png
    ├── Q5_Output.png
    ├── Q6_Output.png
    ├── Bonus_Output.png
    └── README.md

---

## Conclusion

This assignment demonstrates the implementation of real-world API features like search, sorting, and pagination using FastAPI. It also shows how multiple operations can be efficiently combined into a single endpoint.
