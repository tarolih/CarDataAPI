from fastapi import FastAPI, HTTPException, Path, Body
from pydantic import BaseModel
from app.models import products, Product

app = FastAPI()


class PriceUpdateRequest(BaseModel):
    price: float


@app.get("/get_products")
def get_products():
    # Taking only the first three items
    three_products = list(products.items())[:3]
    return {prod_id: {"description": prod.description} for prod_id, prod in three_products}


@app.get("/get_products/{product_id}")
def get_product_details(product_id: int):
    product = products.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/set_price/{product_id}", response_model=Product)
def set_price(product_id: int = Path(...), request: PriceUpdateRequest = Body(...)):
    product = products.get(product_id)
    if product:
        product.price = request.price
        return product
    raise HTTPException(status_code=404, detail="Product not found")
