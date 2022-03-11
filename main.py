from email.policy import HTTP
from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Gender, Role, Product, Cart


app = FastAPI()

db = {
    'user': [
        User(
            id = UUID("0422058c-efa8-4a1d-8fae-4229fb6abfe5"),
            first_name = "Jamila",
            last_name = "Ahmed",
            gender = Gender.female,
            roles = [Role.student],
            cart = None
        ),
        User(
            id = UUID("a8db539d-2303-4cda-b174-c7edd84435fd"),
            first_name = "Alex",
            last_name = "Jonesssss",
            gender = Gender.male,
            roles = [Role.admin, Role.user],
            cart = None
        ),
    ],
    'products': [
        Product(
            id = UUID("a8db539d-2203-4cda-b174-c7edd84435fd"),
            price = 10.2,
            name = "Pao de queijo"
        ),
        Product(
            id = UUID("a8db539d-2303-4cda-b174-c7edd14435fd"),
            price = 20.0,
            name = "Cafe de vinte conto"
        ),
        Product(
            id = UUID("a8db539d-2303-4cda-b174-c7edd83435fd"),
            price = 15,
            name = "Iogurte"
        ),
    ]
}


@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/carrinho/{carrinho_id}/")
def read_items(carrinho_id: str):
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db["user"].append(user)
    return {"id": user.id}

@app.post("/api/v1/cart/{user_id}/{product_name}")
async def addItems(user_id: str, product_name: str):
    selUser = None
    selProduct = None
    for user in db["user"]:
        if(user.id == UUID(user_id)):
            selUser = user
    if(user == None):
        return "Nenhum Usuario Encontrado."
    else:
        for product in db["products"]:
            if(product.name == product_name):
                selProduct = product
                
        if(selProduct == None):
            return "Nenhum Produto Encontrado"
        else:
            if(selUser.cart == None):
                newCart = Cart(
                    id = 1,
                    products = [selProduct]
                )
                selUser.cart = newCart
            else:
                selUser.cart.products.append(selProduct)

            return selUser

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db["user"]:
        if user.id == user_id:
            db["user"].remove(user)
            return 
    raise HTTPException (
        status_code = 404,
        detail = f"user with id: {user_id} does not exists"
    )