from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Model

PokemonType = Table(
    "pokemon_types",
    Model.metadata,
    Column("pokemon_id", ForeignKey("pokemon.id"), primary_key=True),
    Column("type_id", ForeignKey("types.id"), primary_key=True),
)


class Pokemon(Model):
    __tablename__ = "pokemon"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    height: Mapped[int]
    weight: Mapped[float]

    types: Mapped[list["Type"]] = relationship(  # noqa: #F821
        secondary=PokemonType, back_populates="pokemon"
    )
