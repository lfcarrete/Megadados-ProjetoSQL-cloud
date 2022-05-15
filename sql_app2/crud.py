from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate): 
    #fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, first_name = user.first_name, last_name = user.last_name, gender = user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_carrinho_per_user(db: Session, user_id: int):
    
    if db.query(models.Carrinho).filter(models.Carrinho.id_user == user_id).first() == None:
        return "Nenhum carrinho com este id"
    else:
        return db.query(models.Carrinho).filter(models.Carrinho.id_user == user_id).first()
    
def delete_item_carrinho(db: Session, user_id: int, product_id: int):
    
    lista_prod = []
    
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    
    prod = db.query(models.Item).filter(models.Item.id == product_id).first()
    
    #print("Entrou")
    
    if usuario == None:
        return "Nenhum usuário com este id"
    
    elif prod == None:
        return "Nenhum produto com este id"
    
    else:
        i = 0
        for e in usuario.items:
            lista_prod.append(str(e.id))
            print(lista_prod)
            #print(e)
            if e.id == product_id:
              #  print(lista_prod[0])
                usuario.items.remove(e)
                #print(usuario.items)
                db.commit()
            else:
                lista_prod.append(e)
            i+=1
        return usuario
    
    
    