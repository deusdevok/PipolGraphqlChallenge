from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List
import csv

@strawberry.type
class Item:
    id_tie_fecha_valor: int
    id_cli_cliente: int
    desc_categoria_prod_principal: str

@strawberry.type
class Query:
    @strawberry.field
    def items(self) -> List[Item]:
        items_data = []
        # Read csv
        with open('Data example - Python Coding Challenge - GraphQL.csv', 'r', encoding="utf8") as f:
            reader = csv.reader(f)
            # Skip header
            next(reader)
            for line in reader:
                try:
                    items_data.append(Item(
                        id_tie_fecha_valor=int(line[0]),
                        id_cli_cliente=int(line[1]),
                        desc_categoria_prod_principal=line[22]
                    ))
                except:
                    pass

        return items_data
    
schema = strawberry.Schema(query=Query)

app = FastAPI()

@app.get('/')
def main():
    return {"message": "main site"}

app.include_router(GraphQLRouter(schema), prefix="/api")