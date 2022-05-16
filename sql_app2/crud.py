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
    
    print("\n")
    oii = get_users(db, skip=0, limit=100)
    print(oii)
    print("\n")

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

def put_user(db: Session, user: schemas.UpdateUser, user_id : int):

    # get the existing data
    #db_user = db.query(schemas.User).filter(schemas.User.id == user.id).one_or_none()
    db_user = get_users(db, skip=0, limit=100)

    selUser = None

    for userDB in db_user:
        if userDB.id == user_id:
            selUser = userDB

    if user.id != None:
        selUser.id = user.id
    if user.email != None:
        selUser.price = user.email
    if user.first_name != None:
        selUser.first_name = user.first_name
    if user.last_name != None:
        selUser.last_name = user.last_name
    if user.gender != None:
        selUser.gender = user.gender

    return selUser
    # if db_user is None:
    #     return None

    # # Update model class variable from requested fields 
    # for var, value in vars(user).items():
    #     setattr(db_user, var, value) if value else None

    # #db_user.modified = modified_now
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user

    #selUser=db.query(models.User).filter(models.User.id==user_id).first()

    # user_to_update.name=user.name
    # user_to_update.price=user.price
    # user_to_update.description=user.description
    # user_to_update.on_offer=user.on_offer

    #selUser = None

    # for userDB in db[models.User]:
    #     if userDB.id == user_id:
    #         selUser = userDB

    # if user.id != None:
    #     selUser.id = user.id 
    # if user.first_name != None:
    #     selUser.first_name = user.first_name
    # if user.last_name != None:
    #     selUser.last_name = user.last_name
    # if user.gender != None:
    #     selUser.gender = user.gender



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
        for e in usuario.items:
            if db.query(models.Item).filter(models.Item.id == product_id).first() != None:
                usuario.items.remove(e)
            else:
                lista_prod.append(e)
        return usuario
    
    
    