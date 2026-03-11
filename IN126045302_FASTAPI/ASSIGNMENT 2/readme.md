# FastAPI Product Management API

This is a simple FastAPI project that manages products, feedback, and bulk orders.  
It also allows filtering products and viewing product summaries.

Student ID: IN126045302  
Repository Name: innomatics  

--------------------------------------------------

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

--------------------------------------------------

## How to Run the Project

1 Install FastAPI and Uvicorn

pip install fastapi uvicorn

2 Run the server

uvicorn main:app --reload

3 Open in browser

http://127.0.0.1:8000

--------------------------------------------------

## API Endpoints

### 1 Filter Products

GET /products/filter

You can filter products using:
- minimum price
- maximum price
- category

Example:

/products/filter?min_price=100  
/products/filter?category=Electronics

--------------------------------------------------

### 2 Get Product Price

GET /products/{product_id}/price

Example:

/products/1/price

This shows the price of a specific product.

--------------------------------------------------

### 3 Customer Feedback

POST /feedback

Customers can submit feedback for a product.

Example JSON:

{
  "customer_name": "Ravi",
  "product_id": 1,
  "rating": 5,
  "comment": "Very good product"
}

--------------------------------------------------

### 4 Product Summary

GET /products/summary

Shows:
- total products
- in stock products
- out of stock products
- most expensive product
- cheapest product
- categories

--------------------------------------------------

### 5 Bulk Order System

POST /orders/bulk

Companies can place bulk orders for multiple products.

Example JSON:

{
  "company_name": "ABC Company",
  "contact_email": "abc@email.com",
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 2,
    "quantity": 5
    }
  ]
}

The system will return:
- confirmed orders
- failed orders
- total order amount

--------------------------------------------------

## API Documentation

FastAPI automatically provides API documentation.

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc
