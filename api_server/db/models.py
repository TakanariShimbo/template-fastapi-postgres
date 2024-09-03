from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.engine import Engine

from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)

    items: Mapped[list["Item"]] = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), index=True)

    owner: Mapped["User"] = relationship("User", back_populates="items")


def init_db_if_not_exits(engine: Engine):
    Base.metadata.create_all(bind=engine)
