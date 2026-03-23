from fastapi import FastAPI, Query

app = FastAPI()

# -----------------------------
# Sample Product Data
# -----------------------------
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics"},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery"},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics"},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery"},
]

# -----------------------------
# Orders Data
# -----------------------------
orders = []

# -----------------------------
# POST: Create Order
# -----------------------------
@app.post("/orders")
def create_order(customer_name: str):
    order = {
        "order_id": len(orders) + 1,
        "customer_name": customer_name
    }
    orders.append(order)
    return {"message": "Order created", "order": order}


# =========================================================
# Q1 — Search Endpoint (ALREADY BUILT)
# =========================================================
@app.get("/products/search")
def search_products(keyword: str = Query(...)):
    result = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not result:
        return {"message": f"No products found for: {keyword}"}

    return {
        "keyword": keyword,
        "total_found": len(result),
        "products": result
    }


# =========================================================
# Q2 — Sort Endpoint (ALREADY BUILT)
# =========================================================
@app.get("/products/sort")
def sort_products(
    sort_by: str = Query("price"),
    order: str = Query("asc")
):
    if sort_by not in ["price", "name"]:
        return {"error": "sort_by must be 'price' or 'name'"}

    reverse = (order == "desc")

    result = sorted(products, key=lambda p: p[sort_by], reverse=reverse)

    return {
        "sort_by": sort_by,
        "order": order,
        "products": result
    }


# =========================================================
# Q3 — Pagination (ALREADY BUILT)
# =========================================================
@app.get("/products/page")
def paginate_products(
    page: int = Query(1),
    limit: int = Query(2)
):
    start = (page - 1) * limit
    end = start + limit

    total = len(products)

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": -(-total // limit),
        "products": products[start:end]
    }


# =========================================================
# Q4 — Search Orders (NEW CODE)
# =========================================================
@app.get("/orders/search")
def search_orders(customer_name: str = Query(...)):
    result = [
        o for o in orders
        if customer_name.lower() in o["customer_name"].lower()
    ]

    if not result:
        return {"message": f"No orders found for: {customer_name}"}

    return {
        "customer_name": customer_name,
        "total_found": len(result),
        "orders": result
    }


# =========================================================
# Q5 — Sort by Category + Price (NEW CODE)
# =========================================================
@app.get("/products/sort-by-category")
def sort_by_category():
    result = sorted(products, key=lambda p: (p["category"], p["price"]))

    return {
        "products": result,
        "total": len(result)
    }


# =========================================================
# Q6 — Browse (Search + Sort + Pagination) (NEW CODE)
# =========================================================
@app.get("/products/browse")
def browse_products(
    keyword: str = Query(None),
    sort_by: str = Query("price"),
    order: str = Query("asc"),
    page: int = Query(1),
    limit: int = Query(4)
):
    result = products

    # Step 1: Search
    if keyword:
        result = [
            p for p in result
            if keyword.lower() in p["name"].lower()
        ]

    # Step 2: Sort
    if sort_by in ["price", "name"]:
        result = sorted(
            result,
            key=lambda p: p[sort_by],
            reverse=(order == "desc")
        )

    # Step 3: Pagination
    total = len(result)
    start = (page - 1) * limit
    paged = result[start:start + limit]

    return {
        "keyword": keyword,
        "sort_by": sort_by,
        "order": order,
        "page": page,
        "limit": limit,
        "total_found": total,
        "total_pages": -(-total // limit),
        "products": paged
    }


# =========================================================
# ⭐ BONUS — Orders Pagination
# =========================================================
@app.get("/orders/page")
def paginate_orders(
    page: int = Query(1),
    limit: int = Query(3)
):
    start = (page - 1) * limit

    return {
        "page": page,
        "limit": limit,
        "total": len(orders),
        "total_pages": -(-len(orders) // limit),
        "orders": orders[start:start + limit]
    }


# =========================================================
# LAST — Product by ID (KEEP AT END)
# =========================================================
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
    return {"message": "Product not found"}