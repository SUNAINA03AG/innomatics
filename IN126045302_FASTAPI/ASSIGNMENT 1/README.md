# FastAPI Product API

This is a simple FastAPI project that manages a small list of products.  
It provides different API endpoints to view, filter, and search products.

Student ID: IN126045302  
Assignment: FastAPI Assignment 1  
Repository: innomatics

--------------------------------------------------

## Technologies Used
- Python
- FastAPI
- Uvicorn

--------------------------------------------------

## How to Run the Project

1. Install FastAPI and Uvicorn

pip install fastapi uvicorn

2. Run the server

uvicorn main:app --reload

3. Open in browser

http://127.0.0.1:8000

--------------------------------------------------

## API Endpoints

1. Get All Products

GET /products

Shows all products and total number of products.

--------------------------------------------------

2. Get Products by Category

GET /products/category/{category_name}

Example:

/products/category/Electronics

Shows products from a specific category.

------------------------------------------
3. Get In-Stock Products

GET /products/instock

Shows only products that are available in stock.

--------------------------------------------------

4. Store Summary

GET /store/summary

Shows store details like:
- total products
- in stock products
- out of stock products
- categories

--------------------------------------------------

5. Search Products

GET /products/search/{keyword}

Example:

/products/search/mouse

Search products using a keyword in the product name.

--------------------------------------------------

6. Product Deals

GET /products/deals

Shows:
- cheapest product
- most expensive product

--------------------------------------------------

## API Documentation

FastAPI automatically provides documentation.

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc
