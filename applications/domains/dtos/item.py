from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(..., description='item\'s name')
    damage: int = Field(..., description='item\'s damage')
    capacity: int = Field(..., description='capacity of a item',
                          ge=1, le=50)
    repairable: bool = Field(..., description='can it be repaired')
