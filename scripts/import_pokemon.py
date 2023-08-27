# flake8: noqa
import csv
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, "../src")
sys.path.append(APP_DIR)

from sqlalchemy import delete, select

from app.core.db import Session
from app.pokemon.models import Pokemon, PokemonType
from app.types.models import Type


def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(PokemonType))
            session.execute(delete(Pokemon))

    with Session() as session:
        with session.begin():
            with open("scripts/pokemon.csv") as f:
                pokemon_reader = csv.DictReader(f)
                all_types: dict[str, Type] = {}

                for pokemon in pokemon_reader:
                    type = all_types.get(pokemon["type1"])

                    p = Pokemon(
                        id=pokemon["id"],
                        name=pokemon["name"],
                        height=pokemon["height"],
                        weight=pokemon["weight"],
                    )

                    type = all_types.get(pokemon["type1"])
                    if type is None:
                        type = session.scalar(
                            select(Type).where(Type.name == pokemon["type1"])
                        )
                        all_types[pokemon["type1"]] = type
                    type.pokemon.add(p)

                    if pokemon.get("type2"):
                        type = all_types.get(pokemon["type2"])
                        if type is None:
                            type = session.scalar(
                                select(Type).where(Type.name == pokemon["type2"])
                            )
                            all_types[pokemon["type2"]] = type
                        type.pokemon.add(p)


if __name__ == "__main__":
    main()
