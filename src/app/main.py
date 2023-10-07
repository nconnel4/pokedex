import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.pokemon.query import PokemonQuery


@strawberry.type
class Query(PokemonQuery):
    pass


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter[object, object](schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
async def ping() -> dict[str, str]:
    return {"message": "pong!"}
