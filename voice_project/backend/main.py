from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# =========================
# LOAD MENU
# =========================
with open("menu.json", "r") as f:
    menu = json.load(f)

# =========================
# INPUT MODEL
# =========================
class Order(BaseModel):
    text: str

# =========================
# HISTORY STORAGE
# =========================
order_history = []

# =========================
# HOME API
# =========================
@app.get("/")
def home():
    return {"message": "Backend is working"}

# =========================
# ORDER API
# =========================
@app.post("/order")
def process_order(order: Order):

    text = order.text.lower().strip()
    items_found = []

    # SMART DETECTION
    for category, items in menu.items():
        for item in items:
            if item.lower() in text or category.lower() in text:
                items_found.append(item)

    # SAVE HISTORY
    order_history.append({
        "input": text,
        "items": items_found
    })

    return {
        "input_text": text,
        "items_found": items_found,
        "count": len(items_found),
        "message": f"Order processed successfully"
    }

# =========================
# HISTORY API
# =========================
@app.get("/history")
def get_history():
    return order_history

# =========================
# REPORT API (WEEK 3)
# =========================
@app.get("/report")
def report():

    total_orders = len(order_history)

    all_items = []
    for order in order_history:
        all_items.extend(order["items"])

    return {
        "total_orders": total_orders,
        "total_items": len(all_items),
        "unique_items": list(set(all_items))
    }