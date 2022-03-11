from email.policy import HTTP
from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Gender, Product, Cart


app = FastAPI()

db = {
    'user': [
        User(
            id = UUID("0422058c-efa8-4a1d-8fae-4229fb6abfe5"),
            first_name = "Jamila",
            last_name = "Ahmed",
            gender = Gender.female,
            Cart = None
        ),
        User(
            id = UUID("a8db539d-2303-4cda-b174-c7edd84435fd"),
            first_name = "Alex",
            last_name = "Jones",
            gender = Gender.male,
            Cart = None
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

# Get de todos os usuários do db
@app.get("/users")
async def fetch_users():
    return db["user"]


# Get de um usuário
@app.get("/user/{user_id}/")
def read_items(user_id: str):
    vef = 0
    for u in db['user']:
        print(u.id)
        if u.id == UUID(user_id):
            vef = 0
            return u
        
        else:
            vef = 1
    
    if vef == 1:
        raise HTTPException(status_code = 404, detail = "User not found")

# Get de um produto
@app.get("/carrinho/{carrinho_id}/")
def read_items(carrinho_id: str):
    vef = 0
    for products in db['products']:
        print(products.id)
        if products.id == UUID(carrinho_id):
            vef = 0
            return products
        
        else:
            vef = 1
    
    if vef == 1:
        raise HTTPException(status_code = 404, detail = "Item not found")

# Post de um usuário
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

# Delete de um usuário
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