from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column, relationship

from app.core.db import Model

PokemonType = Table(
    "pokemon_types",
    Model.metadata,
    Column("pokemon_id", ForeignKey("pokemon.id"), primary_key=True),
    Column("type_id", ForeignKey("types.id"), primary_key=True),
)


class Type(Model):
    __tablename__ = "types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

    pokemon: WriteOnlyMapped[list["Pokemon"]] = relationship(
        secondary=PokemonType, back_populates="types"
    )

    def __repr__(self):
        return f"Type({self.id}, '{self.name}')"


class Pokemon(Model):
    __tablename__ = "pokemon"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    height: Mapped[int]
    weight: Mapped[float]

    types: Mapped[list["Type"]] = relationship(
        secondary=PokemonType, back_populates="pokemon"
    )

    def __repr__(self):
        return f"Pokemon({self.id}, '{self.name}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "types": [type.name for type in self.types],
        }
