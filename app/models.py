from pydantic import BaseModel
from typing import Dict, Optional


class Product(BaseModel):
    id: int
    description: str
    length: Optional[float] = None
    engine_type: Optional[str] = None
    price: Optional[float] = None


class PriceUpdateRequest(BaseModel):
    price: float


products: Dict[int, Product] = {
    1: Product(id=1, description="Small Car", length=3.5, engine_type="Petrol", price=10000),
    2: Product(id=2, description="Sedan", length=4.8, engine_type="Diesel", price=20000),
    3: Product(id=3, description="SUV", length=5.2, engine_type="Electric", price=30000),
    4: Product(id=4, description="Convertible", length=4.2, engine_type="Hybrid", price=25000),
    5: Product(id=5, description="Hatchback", length=3.9, engine_type="Petrol", price=15000),
    6: Product(id=6, description="Pickup Truck", length=5.5, engine_type="Diesel", price=35000)
}
