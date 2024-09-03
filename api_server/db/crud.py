from sqlalchemy.orm import Session

from . import models, schemas


"""
USER
"""


def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


"""
ITEM
"""


def create_item(db: Session, item: schemas.ItemCreate, user_id: int):
    new_item = models.Item(**item.model_dump(), owner_id=user_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_items_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Item).filter(models.Item.owner_id == user_id).offset(skip).limit(limit).all()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()
