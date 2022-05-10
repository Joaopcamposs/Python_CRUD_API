# models.py

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
