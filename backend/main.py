from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
import strawberry
from strawberry.fastapi import GraphQLRouter
from pydantic import BaseModel
from .graphqlschemas import Query
from .schemas import *
from .helpers import *
    
schema = strawberry.Schema(query=Query)

app = FastAPI()

# Authorization
@app.post("/token", include_in_schema=False)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    return get_token(form_data)

# Custom GraphQL request body model for Swagger documentation
class GraphQLRequest(BaseModel):
    query: str

async def get_context(user: Annotated[User, Depends(get_current_active_user)]):
    return {"user": user.username}

app.include_router(GraphQLRouter(schema, context_getter=get_context), prefix="/graphql", include_in_schema=True)

@app.get('/search/')
def search(term: str):
    filtered_items = {}
    return filtered_items

# Include body parameter in GraphQL post in Swagger
app.openapi()['paths']['/graphql']['post']['requestBody'] = {
                "content": {
                    "application/json": {
                        "schema": GraphQLRequest.model_json_schema(),
                        "example": {"query": "{items(limit: 10) {descGaNombreProducto1 descGaMarcaProducto descCategoriaProducto descCategoriaProdPrincipal}}"}
                                        }
                            }
                    }

# Remove GraphQL get request from Swagger
del app.openapi()['paths']['/graphql']['get']