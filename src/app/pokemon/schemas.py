import strawberry

from app.pokemon import models


@strawberry.type
class Pokemon(object):
    id: strawberry.ID
    name: str
    height: int
    weight: float
    type: str

    @classmethod
    def marshal(cls, model: models.Pokemon) -> "Pokemon":
        type_list = [type.name for type in model.types]
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            height=model.height,
            weight=model.weight,
            type="/".join(type_list),
        )
