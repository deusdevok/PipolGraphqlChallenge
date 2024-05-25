from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List
import csv
from typing import Optional

@strawberry.type
class Item:
    id_tie_fecha_valor: int | None = None
    id_cli_cliente: int
    id_ga_vista: float
    id_ga_tipo_dispositivo: float
    id_ga_fuente_medio: float
    desc_ga_sku_producto: str
    desc_ga_categoria_producto: str
    fc_agregado_carrito_cant: int
    fc_ingreso_producto_monto: float
    fc_retirado_carrito_cant: int | None = None
    fc_detalle_producto_cant: int
    fc_producto_cant: int
    desc_ga_nombre_producto: str
    fc_visualizaciones_pag_cant: int | None = None
    flag_pipol: int | None = None
    SASASA: str
    id_ga_producto: float | None = None
    desc_ga_nombre_producto_1: str
    desc_ga_sku_producto_1: str
    desc_ga_marca_producto: str
    desc_ga_cod_producto: str
    desc_categoria_producto: str
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
                        id_tie_fecha_valor=int(line[0]) if line[0].isdigit() else None,
                        id_cli_cliente=int(line[1]),
                        id_ga_vista=float(line[2]),
                        id_ga_tipo_dispositivo= float(line[3]),
                        id_ga_fuente_medio= float(line[4]),
                        desc_ga_sku_producto= line[5],
                        desc_ga_categoria_producto= line[6],
                        fc_agregado_carrito_cant= int(line[7]),
                        fc_ingreso_producto_monto= float(line[8]),
                        fc_retirado_carrito_cant= int(line[9]) if line[9].isdigit() else None,
                        fc_detalle_producto_cant= int(line[10]),
                        fc_producto_cant= int(line[11]),
                        desc_ga_nombre_producto= line[12],
                        fc_visualizaciones_pag_cant= int(line[13]) if line[13].isdigit() else None,
                        flag_pipol= int(line[14]) if line[14].isdigit() else None,
                        SASASA= line[15],
                        id_ga_producto= float(line[16]) if line[16] else None,
                        desc_ga_nombre_producto_1= line[17],
                        desc_ga_sku_producto_1= line[18],
                        desc_ga_marca_producto= line[19],
                        desc_ga_cod_producto= line[20],
                        desc_categoria_producto= line[21],
                        desc_categoria_prod_principal=line[22]
                    ))
                    
                except Exception as e:
                    print(f'Error in line {line}: {e}')
                    break

        return items_data
    
schema = strawberry.Schema(query=Query)

app = FastAPI()

@app.get('/')
def main():
    return {"message": "main site"}

app.include_router(GraphQLRouter(schema), prefix="/api")