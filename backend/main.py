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

@app.get(
        '/search/', 
        summary="Search items by name/description",
        description='''
In order to search using NLP, I can think of a couple of options:

* Have the data in the CSV saved in a PostgreSQL database and use tsvectors. This way, each string column gets vectorized and queries can be made in an efficient manner.
* Using an API like openai and ask it to search the items that best match a given query.
''')
def search(term: str):
    return {"items": f"filtered by {term}"}


app.openapi()['paths']['/graphql']['post']['summary'] = "GraphQL query endpoint"
app.openapi()['paths']['/graphql']['post']['description'] = """
Columns:

* id_tie_fecha_valor: int | None = None
* id_cli_cliente: int
* id_ga_vista: float
* id_ga_tipo_dispositivo: float
* id_ga_fuente_medio: float
* desc_ga_sku_producto: str
* desc_ga_categoria_producto: str
* fc_agregado_carrito_cant: int
* fc_ingreso_producto_monto: float
* fc_retirado_carrito_cant: int | None = None
* fc_detalle_producto_cant: int
* fc_producto_cant: int
* desc_ga_nombre_producto: str
* fc_visualizaciones_pag_cant: int | None = None
* flag_pipol: int | None = None
* SASASA: str
* id_ga_producto: float | None = None
* desc_ga_nombre_producto_1: str
* desc_ga_sku_producto_1: str
* desc_ga_marca_producto: str
* desc_ga_cod_producto: str
* desc_categoria_producto: str
* desc_categoria_prod_principal: str
"""

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