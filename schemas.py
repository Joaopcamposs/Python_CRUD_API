# schemas.py

from pydantic import BaseModel


# To support creation and update APIs
class CreateAndUpdateUser(BaseModel):
    name: str
    email: str
    password: str


# To support list and get APIs
class Users(CreateAndUpdateUser):
    id: int

    class Config:
        orm_mode = True
