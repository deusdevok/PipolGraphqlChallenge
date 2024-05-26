![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![GraphQL](https://img.shields.io/badge/-GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)

# Pipol GraphQL Technical Challenge

## How to use this repository

* Clone the repository: `git clone https://github.com/deusdevok/PipolGraphqlChallenge.git`
* Create a `.env` file and place it at the same level as the Dockerfiles. Set the secret key value (the actual value has been sent via email) in it: `SECRET_KEY=thesecretkey`.
* Include the csv file inside the `backend` directory. The name of the csv must be `Data example - Python Coding Challenge - GraphQL.csv`.
* Create and run the Docker image: `docker compose up --build`.

## Authorization

In order to make requests, there is one dummy user who has access:

* username: johndoe
* password: secret

To test in Postman, first login from the Swagger docs, and retrieve the JWT (Bearer) from the developer console. Use that token in Postman to make requests.
