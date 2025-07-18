import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from core.database import Base


class User(Base):
    __tablename__ = "users"

    id = sa.Column(
        "id",
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text("uuid_generate_v4()"),
    )
    name = sa.Column("name", sa.String(), nullable=False, unique=True)
    created_at = sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.func.now())
    updated_at = sa.Column("updated_at", sa.TIMESTAMP(), server_default=sa.func.now())
