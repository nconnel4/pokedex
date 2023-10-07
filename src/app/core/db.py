from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker

from app.core.config import Settings

settings = Settings()


class Model(MappedAsDataclass, DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


engine = create_engine(settings.database_url.__str__())
Session = sessionmaker(engine)
