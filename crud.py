# crud.py

from typing import List
from sqlalchemy.orm import Session
from exceptions import UserAlreadyExistError, UserNotFoundError
from models import User
from schemas import CreateAndUpdateUser


# Function to get list of users
async def get_all_users(session: Session) -> List[User]:
    return session.query(User).all()


# Function to  get info of a particular user by id
async def get_user_by_id(session: Session, _id: int) -> User:
    user = session.query(User).filter(User.id == _id).first()

    if user is None:
        raise UserNotFoundError

    return user


# Function to add a new user to the database
async def create_user(session: Session, user: CreateAndUpdateUser) -> User:
    # email must be unique
    user_details = session.query(User).filter(User.email == user.email).first()

    if user_details is not None:
        raise UserAlreadyExistError

    new_user = User(**user.dict())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


# Function to update details of the user
async def update_user_by_id(session: Session, _id: int, info_update: CreateAndUpdateUser) -> User:
    user = await get_user_by_id(session, _id)

    if user is None:
        raise UserNotFoundError

    user.name = info_update.name
    user.email = info_update.email
    user.password = info_update.password

    session.commit()
    session.refresh(user)

    return user


# Function to delete a user from the db
async def delete_user_by_id(session: Session, _id: id):
    user = await get_user_by_id(session, _id)

    if user is None:
        raise UserNotFoundError

    session.delete(user)
    session.commit()

    return


# Function to create project database
def create_db():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+pymysql://user:@host:port/')
    Session = sessionmaker(engine)
    try:
        with Session.begin() as session:
            session.execute('create database crud_api;')
            session.execute('use crud_api;')
            session.execute('create table users(id int AUTO_INCREMENT PRIMARY KEY,name varchar(50) NOT NULL,'
                            'email varchar(50) NOT NULL,password varchar(50) NOT NULL);')
            session.commit()
    except:
        return "Something went wrong"

    return "created database"
