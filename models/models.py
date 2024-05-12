# import enum
# import datetime
# from typing import Optional, Annotated


# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from database import Base

# intpk = Annotated[int, mapped_column(primary_key=True)]
# created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
#
# class ConstructionObjectOrm(Base):
#     __tablename__ = "construction_objects"
#
#     id: Mapped[intpk]
#
# class Status(enum.Enum):
#     not_processed = "not processed"
#     in_work = "in work"
#     closed = "closed"
#
# class Category(enum.Enum):
#     not_processed = "not processed"
#     in_work = "in work"
#     closed = "closed"
#
#
# class AppealOrm(Base):
#     __tablename__ = "appeals"
#
#     id: Mapped[intpk]
#     number: Mapped[int]
#     created_at: Mapped[created_at]
#     name: Mapped[str]
#     surname: Mapped[str]
#     patronymic: Mapped[Optional[str]]
#     phone_number: Mapped[str]
#     email: Mapped[Optional[str]]
#     construction_object_id: Mapped[int] = mapped_column(ForeignKey("construction_objects.id"))
#     entrance: Mapped[int]
#     floor: Mapped[int]
#     flat: Mapped[int]
#     status: Mapped[Status]
#     category: Mapped[Category]
#     description: Mapped[str]

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("full_name", String, nullable=False),
    Column("email", String),
    Column("phone_number", String),
    Column("role_id", Integer, ForeignKey("roles.id")),
)

