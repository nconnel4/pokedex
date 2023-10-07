from typing import Optional

import strawberry
from sqlalchemy import select

from app.core.db import Session
from app.pokemon import models
from app.pokemon.schemas import Pokemon


@strawberry.type
class PokemonQuery:
    @strawberry.field
    def pokemon(self, name: Optional[str] = None) -> list[Pokemon]:
        with Session() as session:
            if name is None:
                q = select(models.Pokemon)
                db_pokemon = session.execute(q).all()
            else:
                q = select(models.Pokemon).where(models.Pokemon.name.ilike(f"%{name}%"))
                db_pokemon = session.execute(q).all()
            return [Pokemon.marshal(pokemon[0]) for pokemon in db_pokemon]
