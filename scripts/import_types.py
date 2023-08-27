# flake8: noqa
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, "../src")
sys.path.append(APP_DIR)

from sqlalchemy import delete

from app.core.db import Session
from app.pokemon.models import PokemonType
from app.types.models import Type

TYPES = [
    "normal",
    "fire",
    "water",
    "electric",
    "grass",
    "ice",
    "fight",
    "poison",
    "ground",
    "flying",
    "psychic",
    "bug",
    "rock",
    "ghost",
    "dragon",
]


def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(PokemonType))
            session.execute(delete(Type))

    with Session() as session:
        with session.begin():
            for type in TYPES:
                t = Type(name=type)
                session.add(t)


if __name__ == "__main__":
    main()
