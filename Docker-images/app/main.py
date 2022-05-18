from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import String
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/items/{itemName}", response_model=schemas.Item)
def create_item(itemName: str, db: Session = Depends(get_db)):
    item = crud.create_items(db=db, itemName=itemName)
    return item


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@app.post("/users/{user_id}/items/")
def create_item_for_user(
    User_Item: schemas.User_Item, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item_id=User_Item.produto_id, user_id=User_Item.owner_id, quantidade = User_Item.quantidade)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
         raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_item

@app.delete("/users/{user_id}/items/")
def delete_item(user_id: int, item_id: int, db: Session = Depends(get_db)):
    deleting = crud.delete_item_carrinho(db, user_id = user_id, product_id = item_id)
    return deleting

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleting = crud.delete_item(db, product_id = item_id)
    return deleting

@app.get("/userItems/")
def read_items(user_id : int, db: Session = Depends(get_db)):
    items = crud.get_carrinho_per_user(db, user_id)
    return items