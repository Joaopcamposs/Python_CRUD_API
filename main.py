# main.py

from fastapi import FastAPI
import api
from crud import create_db

# initialize mysql database
create_db()

# initialize the app
app = FastAPI()

# include routes from api
app.include_router(api.app)
