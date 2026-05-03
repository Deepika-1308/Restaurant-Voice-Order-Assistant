from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is working"}

# input format
class Order(BaseModel):
    text: str

# order logic
@app.post("/order")
def process_order(order: Order):
    text = order.text.lower().strip()

    items = []

    if "pizza" in text:
        items.append("pizza")

    if "burger" in text:
        items.append("burger")

    if "coke" in text:
        items.append("coke")

    return {
        "cleaned_text": text,
        "items": items,
        "message": f"Items added: {items}"
    }