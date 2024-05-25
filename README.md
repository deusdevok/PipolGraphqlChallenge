# Pipol GraphQL Technical Challenge

## GraphQL query examples

Get all records with specific fields:

```
{
  items {
    idTieFechaValor
    idCliCliente
    descCategoriaProdPrincipal
  }
}
```

Get records with all fields:

```
{
  items {
    idTieFechaValor
    idCliCliente
    idGaVista
    idGaTipoDispositivo
    idGaFuenteMedio
    descGaSkuProducto
    descGaCategoriaProducto
    fcAgregadoCarritoCant
    fcIngresoProductoMonto
    fcRetiradoCarritoCant
    fcDetalleProductoCant
    fcProductoCant
    descGaNombreProducto
    fcVisualizacionesPagCant
    flagPipol
    SASASA
    idGaProducto
    descGaNombreProducto1
    descGaSkuProducto1
    descGaMarcaProducto
    descGaCodProducto
    descCategoriaProducto
    descCategoriaProdPrincipal
  }
}
```

## Example in Swagger docs

In the POST request:

```
{
  "query": "{items(limit: 10) {descGaNombreProducto1 descGaMarcaProducto descCategoriaProducto descCategoriaProdPrincipal}}",
  "operationName": null,
  "variables": null
}
```