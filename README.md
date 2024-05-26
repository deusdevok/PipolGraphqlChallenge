# Pipol GraphQL Technical Challenge

## Authorization

* username: johndoe
* password: secret

To test in Postman, first login from the Swagger docs, and retrieve the JWT (Bearer) from the developer console. Use that token in Postman to make requests.

## Secrets

Create a `.env` file and place it at the same level as the Dockerfiles. Set the secret key in it:

`SECRET_KEY=thesecretkey`

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

Limit the number of records:
```
{
  items(limit: 10) {
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
}
```