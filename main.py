from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
import strawberry
from strawberry.fastapi import GraphQLRouter
from pydantic import BaseModel
from graphqlschemas import Query
from schemas import *
from helpers import *
    
schema = strawberry.Schema(query=Query)

app = FastAPI()

@app.get('/')
def main():
    return {"message": "main site"}

# Authorization
@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    return get_token(form_data)

@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]

# Custom GraphQL request body model for Swagger documentation
class GraphQLRequest(BaseModel):
    query: str

async def get_context(user: Annotated[User, Depends(get_current_active_user)]):
    return {"user": user.username}

app.include_router(GraphQLRouter(schema, context_getter=get_context), prefix="/api", include_in_schema=True)

@app.get('/search/')
def search(term: str):
    filtered_items = {}
    return filtered_items

# Include body parameter in GraphQL post in Swagger
app.openapi()['paths']['/api']['post']['requestBody'] = {
                "content": {
                    "application/json": {
                        "schema": GraphQLRequest.model_json_schema(),
                        "example": {"query": "{items(limit: 10) {descGaNombreProducto1 descGaMarcaProducto descCategoriaProducto descCategoriaProdPrincipal}}"}
                                        }
                            }
                    }

# Remove GraphQL get request from Swagger
del app.openapi()['paths']['/api']['get']