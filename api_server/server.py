from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from db import models, schemas, crud, engine, get_db


"""
INIT DB
"""
models.init_db_if_not_exits(engine=engine)


app = FastAPI()


"""
USER ENDPOINTS
"""


@app.post("/users/create-new-user/", response_model=schemas.User)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db=db, user=user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="User already registered")


@app.get("/users/get-user-by-id/{user_id}", response_model=schemas.User)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/get-user-by-name/{name}", response_model=schemas.User)
def get_user_by_name(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db=db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/list-all-users/", response_model=list[schemas.User])
def list_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


"""
ITEM ENDPOINTS
"""


@app.post("/users/{user_id}/items/create-item-for-user/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_item(db=db, item=item, user_id=user_id)


@app.get("/items/get-item-by-id/{item_id}", response_model=schemas.Item)
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.get("/users/{user_id}/items/list-items-by-user/", response_model=list[schemas.Item])
def list_items_by_user(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items_by_user(db=db, user_id=user_id, skip=skip, limit=limit)
    return items


@app.get("/items/list-all-items/", response_model=list[schemas.Item])
def list_all_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db=db, skip=skip, limit=limit)
    return items
