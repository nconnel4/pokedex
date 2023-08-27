from sqlalchemy import String
from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column, relationship

from app.core.db import Model
from app.pokemon.models import Pokemon, PokemonType


class Type(Model):
    __tablename__ = "types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

    pokemon: WriteOnlyMapped[list["Pokemon"]] = relationship(
        secondary=PokemonType, back_populates="types"
    )

    def __repr__(self):
        return f"Type({self.id}, '{self.name}')"
