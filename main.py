from email.policy import HTTP
from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Gender, Role, Product


app = FastAPI()

# db: List[User] = [
#     User(
#         id = UUID("0422058c-efa8-4a1d-8fae-4229fb6abfe5"),
#         first_name = "Jamila",
#         last_name = "Ahmed",
#         gender = Gender.female,
#         roles = [Role.student]
#     ),
#     User(
#         id = UUID("a8db539d-2303-4cda-b174-c7edd84435fd"),
#         first_name = "Alex",
#         last_name = "Jones",
#         gender = Gender.male,
#         roles = [Role.admin, Role.user]
#     )
# ]

# db2:   List[Product] = [
#     Product(
#         id = UUID("SE93QE"),
#         price = 10.2,
#         name = "Pao de queijo"
#     ),
#     Product(
#         id = UUID("fgvdthgbrt"),
#         price = 20.0,
#         name = "Cafe de vinte conto"
#     ),
#     Product(
#         id = UUID("vvbdgfbdteg"),
#         price = 15,
#         name = "Iogurte"
#     ), 

#     ]
    


#     List[Product] = [
#         Product(
#             id = UUID("SE93QE"),
#             price = 10.2,
#             name = "Pao de queijo"
#         ),
#         Product(
#             id = UUID("fgvdthgbrt"),
#             price = 20.0,
#             name = "Cafe de vinte conto"
#         ),
#         Product(
#             id = UUID("vvbdgfbdteg"),
#             price = 15,
#             name = "Iogurte"
#         ), 

#     ]

# db2:    List[Product] = [
#         Product(
#             id = UUID("SE93QE"),
#             price = 10.2,
#             name = "Pao de queijo"
#         ),
#         Product(
#             id = UUID("fgvdthgbrt"),
#             price = 20.0,
#             name = "Cafe de vinte conto"
#         ),
#         Product(
#             id = UUID("vvbdgfbdteg"),
#             price = 15,
#             name = "Iogurte"
#         ), 

#     ]

db = {
    'user': [
        User(
            id = UUID("0422058c-efa8-4a1d-8fae-4229fb6abfe5"),
            first_name = "Jamila",
            last_name = "Ahmed",
            gender = Gender.female,
            roles = [Role.student],
            Cart = []
        ),
        User(
            id = UUID("a8db539d-2303-4cda-b174-c7edd84435fd"),
            first_name = "Alex",
            last_name = "Jonesssss",
            gender = Gender.male,
            roles = [Role.admin, Role.user],
            Cart = []
        ),
    ],
    'products': [
        Product(
            id = UUID("SE93QE"),
            price = 10.2,
            name = "Pao de queijo"
        ),
        Product(
            id = UUID("fgvdthgbrt"),
            price = 20.0,
            name = "Cafe de vinte conto"
        ),
        Product(
            id = UUID("vvbdgfbdteg"),
            price = 15,
            name = "Iogurte"
        ),
    ]
}
#     User(
#         id = UUID("0422058c-efa8-4a1d-8fae-4229fb6abfe5"),
#         first_name = "Jamila",
#         last_name = "Ahmed",
#         gender = Gender.female,
#         roles = [Role.student]
#     ),
#     User(
#         id = UUID("a8db539d-2303-4cda-b174-c7edd84435fd"),
#         first_name = "Alex",
#         last_name = "Jones",
#         gender = Gender.male,
#         roles = [Role.admin, Role.user]
#     ),
#     Product(
#         id = UUID("SE93QE"),
#         price = 10.2,
#         name = "Pao de queijo"
#     ),
#     Product(
#         id = UUID("fgvdthgbrt"),
#         price = 20.0,
#         name = "Cafe de vinte conto"
#     ),
#     Product(
#         id = UUID("vvbdgfbdteg"),
#         price = 15,
#         name = "Iogurte"
#     ), 

# ]
   

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