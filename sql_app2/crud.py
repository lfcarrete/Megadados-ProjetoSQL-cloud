from sqlalchemy.orm import Session
from sqlalchemy import String

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    #fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, first_name=user.first_name,
                          last_name=user.last_name, gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_items(db: Session, itemName: str):
    db_items = models.Item(produto=itemName)
    db.add(db_items)
    db.commit()
    db.refresh(db_items)
    return db_items


def get_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    item = db.query(models.Item).offset(skip).limit(limit).all()
    return item


def create_user_item(db: Session, item_id: int, user_id: int, quantidade: int):
    user = get_user(db, user_id)
    if(not user):
        return "Usario nao encontrado"
    item = get_item(db, item_id)
    if(not item):
        return "Produto nao encontrado"
    db_item = models.User_Item(
        produto_id=item_id, owner_id=user_id, quantidade=quantidade)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_carrinho_per_user(db: Session, user_id: int):

    if db.query(models.User_Item).filter(models.User_Item.owner_id == user_id).first() == None:
        return "Nenhum carrinho com este id"
    else:
        carrinho = db.query(models.User_Item).filter(models.User_Item.owner_id == user_id).all()
        if not carrinho:
            return "Carrinho esta vazio"
        else: 
            return carrinho


def delete_item_carrinho(db: Session, user_id: int, product_id: int):

    usuario = db.query(models.User).filter(models.User.id == user_id).first()

    prod = db.query(models.Item).filter(models.Item.id == product_id).first()

    # print("Entrou")

    if usuario == None:
        return "Nenhum usuário com este id"

    elif prod == None:
        return "Nenhum produto com este id"

    else:
        linhaUsuarioItem = db.query(models.User_Item).filter(
            models.User_Item.produto_id == product_id and models.User_Item.owner_id == user_id).first()

        db.delete(linhaUsuarioItem)
        db.commit()

        return "Deletado com sucesso"

def delete_item(db: Session, product_id: int):

    prod = db.query(models.Item).filter(models.Item.id == product_id).first()

    # print("Entrou")

    if prod == None:
        return "Nenhum produto com este id"

    else:
        linhaUsuarioItem = db.query(models.User_Item).filter(models.User_Item.produto_id == product_id).all()
        print(linhaUsuarioItem)
        for i in linhaUsuarioItem:
            db.delete(i)
            db.commit()
        db.delete(prod)
        db.commit()
        return "Deletado com sucesso"
