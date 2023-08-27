"""add pokemon and types

Revision ID: 0615858b5256
Revises:
Create Date: 2023-08-27 18:18:51.152066

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0615858b5256"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "pokemon",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=25), nullable=False),
        sa.Column("height", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_pokemon")),
    )
    op.create_table(
        "types",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=25), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_types")),
    )
    op.create_table(
        "pokemon_types",
        sa.Column("pokemon_id", sa.Integer(), nullable=False),
        sa.Column("type_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pokemon_id"],
            ["pokemon.id"],
            name=op.f("fk_pokemon_types_pokemon_id_pokemon"),
        ),
        sa.ForeignKeyConstraint(
            ["type_id"], ["types.id"], name=op.f("fk_pokemon_types_type_id_types")
        ),
        sa.PrimaryKeyConstraint("pokemon_id", "type_id", name=op.f("pk_pokemon_types")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("pokemon_types")
    op.drop_table("types")
    op.drop_table("pokemon")
    # ### end Alembic commands ###