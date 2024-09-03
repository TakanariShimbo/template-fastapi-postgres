from pydantic import BaseModel
from typing import List, Optional


class UserCreate(BaseModel):
    name: str


class User(BaseModel):
    id: int
    name: str
    items: List["Item"] = []

    class Config:
        from_attributes = True


class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None


class Item(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    owner_id: int

    class Config:
        from_attributes = True
