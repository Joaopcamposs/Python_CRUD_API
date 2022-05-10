# api.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_all_users, create_user, update_user_by_id, delete_user_by_id, get_user_by_id
from database import get_db
from exceptions import UserException
from schemas import Users, CreateAndUpdateUser

app = APIRouter()


# API endpoint to get the list of users
@app.get("/api/users", response_model=List[Users])
async def list_users(session: Session = Depends(get_db)):
    users_list = await get_all_users(session=session)

    return users_list


# API endpoint to add a user to the database
@app.post("/api/user")
async def add_user(new_user: CreateAndUpdateUser, session: Session = Depends(get_db)):
    try:
        return await create_user(session, new_user)
    except UserException as err:
        raise HTTPException(**err.__dict__)


# API endpoint to get info of a particular user by id
@app.get("/api/user/{user_id}", response_model=Users)
async def get_user(user_id: int, session: Session = Depends(get_db)):
    try:
        return await get_user_by_id(session, user_id)
    except UserException as err:
        raise HTTPException(**err.__dict__)


# API endpoint to update a existing user
@app.put("/api/user/{user_id}", response_model=Users)
async def update_user(user_id: int, new_info: CreateAndUpdateUser,
                           session: Session = Depends(get_db)):
    try:
        return await update_user_by_id(session, user_id, new_info)
    except UserException as err:
        raise HTTPException(**err.__dict__)


# API endpoint to delete a user from the data base
@app.delete("/api/user/{user_id}")
async def delete_user(user_id: int, session: Session = Depends(get_db)):
    try:
        return await delete_user_by_id(session, user_id)
    except UserException as err:
        raise HTTPException(**err.__dict__)
