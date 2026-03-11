from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# -----------------------------
# Sample product database
# -----------------------------
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 500, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 100, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Cable", "price": 200, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen", "price": 50, "category": "Stationery", "in_stock": True}
]

feedback_list = []
orders = []


# =====================================================
# QUESTION 1
# Filter products by price or category
# =====================================================

@app.get("/products/filter")
def filter_products(min_price: int = None, max_price: int = None, category: str = None):

    result = products

    if min_price:
        result = [p for p in result if p["price"] >= min_price]

    if max_price:
        result = [p for p in result if p["price"] <= max_price]

    if category:
        result = [p for p in result if p["category"].lower() == category.lower()]

    return result


# =====================================================
# QUESTION 2
# Get price of a specific product
# =====================================================

@app.get("/products/{product_id}/price")
def get_price(product_id: int):

    for p in products:
        if p["id"] == product_id:
            return {
                "product": p["name"],
                "price": p["price"]
            }

    return {"error": "Product not found"}


# =====================================================
# QUESTION 3
# Customer Feedback System
# =====================================================

class Feedback(BaseModel):
    customer_name: str = Field(min_length=2)
    product_id: int = Field(gt=0)
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None


@app.post("/feedback")
def add_feedback(data: Feedback):

    feedback_list.append(data)

    return {
        "message": "Feedback submitted",
        "total_feedback": len(feedback_list),
        "data": data
    }


# =====================================================
# QUESTION 4
# Product Summary Dashboard
# =====================================================

@app.get("/products/summary")
def product_summary():

    total = len(products)

    in_stock = len([p for p in products if p["in_stock"]])
    out_stock = total - in_stock

    most_expensive = max(products, key=lambda x: x["price"])
    cheapest = min(products, key=lambda x: x["price"])

    categories = list(set([p["category"] for p in products]))

    return {
        "total_products": total,
        "in_stock": in_stock,
        "out_of_stock": out_stock,
        "most_expensive": most_expensive,
        "cheapest": cheapest,
        "categories": categories
    }


# =====================================================
# QUESTION 5
# Bulk Order System
# =====================================================

class OrderItem(BaseModel):
    product_id: int
    quantity: int


class BulkOrder(BaseModel):
    company_name: str
    contact_email: str
    items: List[OrderItem]


@app.post("/orders/bulk")
def bulk_order(order: BulkOrder):

    confirmed = []
    failed = []
    total = 0

    for item in order.items:

        product = None

        for p in products:
            if p["id"] == item.product_id:
                product = p

        if not product:
            failed.append({"product_id": item.product_id, "reason": "Product not found"})
            continue

        if not product["in_stock"]:
            failed.append({"product_id": item.product_id, "reason": "Out of stock"})
            continue

        subtotal = product["price"] * item.quantity
        total += subtotal

        confirmed.append({
            "product": product["name"],
            "quantity": item.quantity,
            "subtotal": subtotal
        })

    return {
        "company": order.company_name,
        "confirmed_orders": confirmed,
        "failed_orders": failed,
        "total_amount": total
    }