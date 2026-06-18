from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from src.infrastructure.database.connection import Base

class UsersTable(Base):
    __tablename__ = "Usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    Hashed_password: Mapped[str] = mapped_column(String)