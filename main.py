from email.policy import HTTP
from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Gender, Product, Cart, UpdateUser, UpdateProduct


app = FastAPI()

db = {
    'user': [
        User(
            id = 1,
            first_name = "Jamila",
            last_name = "Ahmed",
            gender = Gender.female,
            Cart = None
        ),
        User(
            id = 2,
            first_name = "Alex",
            last_name = "Jones",
            gender = Gender.male,
            Cart = None
        ),
    ],
    'products': [
        Product(
            id = 2,
            price = 10.2,
            name = "Pao de queijo"
        ),
        Product(
            id = 1,
            price = 20.0,
            name = "Cafe de vinte conto"
        ),
        Product(
            id = 3,
            price = 15,
            name = "Iogurte"
        ),
    ]
}

# Get de todos os usuários do db
@app.get("/user", tags=["Users"], description="Retorna todos usuários que existem no dataset.")
async def fetch_users():
    return db["user"]

# Get de todos os produtos
@app.get("/product", tags=["Products"], description="Retorna todos os produtos que existem no dataset.")
async def fetch_products():
    return db["products"]

# Get de um usuário
@app.get("/user/{user_id}/",  tags=["Users"], description="Faz uma operação GET para retornar um usuário. Se ele não achar, retorna que o usuário não foi achado")
def read_items(user_id: int):
    vef = 0
    for u in db['user']:
        print(u.id)
        if u.id == user_id:
            vef = 0
            return u
        
        else:
            vef = 1
    
    if vef == 1:
        #raise HTTPException(status_code = 404, detail = "User not found")
        return "User not found"



# Get de um produto
@app.get("/product/{product_id}/",  tags=["Products"], description="Faz uma operação GET para retornar um produto. Se ele não achar, retorna que o item não foi achado.")
def read_items(carrinho_id: int):
    vef = 0
    for products in db['products']:
        print(products.id)
        if products.id == carrinho_id:
            vef = 0
            return products
        
        else:
            vef = 1
    
    if vef == 1:
        #raise HTTPException(status_code = 404, detail = "Item not found")
        return "Item not found"


# Get do Carrinho
@app.get("/cart/{user_Id}", tags=["Carts"], description="Faz uma operação GET para retornar um carrinho. Se ele não encontrar, retorna que não há nenhum usuário ou que não há nenhum produto no carrinho")
def getCart(user_id: int):
    selUser = None

    for user in db["user"]:
        if user.id == user_id:
            selUser = user
    if(selUser == None):
        return "Nenhum Usuario Encontrado."
    else:
        if(selUser.cart == None):
            return "O usuário não contem nenhum produto em seu carrinho"
        else:
            return selUser.cart

# Post de um usuário
@app.post("/user",  tags=["Users"], description="Cria um usuário novo no dataset.")
async def register_user(user: User):
    db["user"].append(user)
    return {"id": user.id}


@app.post("/cart/{user_id}/{product_name}", tags=["Carts"], description="Faz uma operação POST para adicionar um produto a um carrinho já cadastrado.")
async def addItems(user_id: int, product_name: str):
    selUser = None
    selProduct = None
    for user in db["user"]:
        if user.id == user_id:
            selUser = user
    if(selUser == None):
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
    
# Atualizar dados de um usuário
@app.put("/user/{user_id}",  tags=["Users"], description="Faz uma operação PUT para atualizar um usuário.")
async def put_user(user_id: int, user: UpdateUser):
    
    selUser = None

    for userDB in db["user"]:
        if userDB.id == user_id:
            selUser = userDB

    if user.id != None:
        selUser.id = user.id 
    if user.first_name != None:
        selUser.first_name = user.first_name
    if user.last_name != None:
        selUser.last_name = user.last_name
    if user.gender != None:
        selUser.gender = user.gender
    
    return selUser

# Atualizar dados de um produto
@app.put("/product/{product_id}", tags=["Products"], description="Atualiza o produto no dataset, busca o produto pelo Id de seu produto e recebe as informações a ser alteradas.")
async def put_product(product_id: int, product: UpdateProduct):
    
    selProduct = None

    for produtoDB in db["products"]:
        if produtoDB.id == product_id:
            selProduct = produtoDB

    if product.id != None:
        selProduct.id = product.id 
    if product.price != None:
        selProduct.price = product.price
    if product.name != None:
        selProduct.name = product.name

    return selProduct

#Delete Produto do Carrinho
@app.delete("/cart/{user_id}/{product_id}", tags=["Carts"], description="Faz uma operação de DELETE para apagar um produto de um carrinho. Se ele não achar um carrinho retorna que não há produtos neste carrinho e se não achar um produto no carrinho, retorna que não achou com aquele product_id")
async def deleteFromCart(user_id: int, product_id: int):
    selUser = None
    selProduct = None
    for user in db["user"]:
        if(user.id == user_id):
            selUser = user
    if(selUser == None):
        return "Nenhum Usuario Encontrado."
    else:
        if(selUser.cart == None):
                return "Não existe nenhum produto neste carrinho"
        
        else:
            for product in selUser.cart.products:
                if(product.id == product_id):
                    selProduct = product
                
            if(selProduct == None):
                return "Nenhum Produto Encontrado Neste Carrinho Com esse ID"
            
            else:
                for e in selUser.cart.products:
                    if(product_id == e.id):
                        selUser.cart.products.remove(e)

                return "Produto Apagado"



# Delete de um usuário
@app.delete("/user/{user_id}",  tags=["Users"], description="Faz uma operação DELETE para apagar um usuário. Se ele não achar o user_id, joga uma excessão 404.")
async def delete_user(user_id: int):
    for user in db["user"]:
        if user.id == user_id:
            db["user"].remove(user)
            return 
    raise HTTPException (
        status_code = 404,
        detail = f"user with id: {user_id} does not exists"
    )