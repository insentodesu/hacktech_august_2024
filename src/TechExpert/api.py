from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
import db

app = FastAPI()

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    type: Optional[str] = None
    verifed_identity: Optional[int] = None
    profile_photo: Optional[str] = None
    pass_photo: Optional[str] = None
    pass_series_num: Optional[str] = None
    dep_code_pass: Optional[str] = None
    date_of_issue: Optional[str] = None
    inn: Optional[int] = None
    specialization: Optional[str] = None
    verifed_specialization: Optional[int] = None
    balance: Optional[int] = None
    reserved_balance: Optional[int] = None
    bonus_balance: Optional[int] = None

class Developer(BaseModel):
    id: int
    linked_to: Optional[int] = None
    name: str
    fullname: Optional[str] = None
    juridical_address: Optional[str] = None
    factical_address: Optional[str] = None
    inn: Optional[int] = None
    kpp: Optional[int] = None
    ogrn: Optional[int] = None
    photo: Optional[str] = None
    banned_workers: Optional[str] = None
    balance: Optional[int] = None
    founders: Optional[str] = None

class Object(BaseModel):
    id: int
    developer: int
    name: str
    status: Optional[str] = None
    workers: Optional[str] = None

@app.get("/users/{id}", response_model=User)
async def get_user(id: int):
    try:
        user_info = await db.select_users(id)
        if user_info:
            return user_info
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/users/")
async def create_user(user: User):
    try:
        existing_user = await db.select_db(id)
        if not existing_user:
            user_info = await db.insert_users(user.first_name, user.last_name, user.middle_name, user.type, user.verifed_identity, user.profile_photo, user.pass_photo, user.pass_series_num, user.dep_code_pass, user.date_of_issue, user.inn, user.specialization, user.verifed_specialization, user.balance, user.reserved_balance, user.bonus_balance)
            return {"detail": "success", "id": user_info["id"]}
        else:
            raise HTTPException(status_code=400, detail="User already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/developers/{id}", response_model=Developer)
async def get_developer(id: int):
    try:
        developer_info = await db.select_db("developers")
        if developer_info:
            return {
                "id": developer_info[0],
                "linked_to": developer_info[1],
                "name": developer_info[2],
                "fullname": developer_info[3],
                "juridical_address": developer_info[4],
                "factical_address": developer_info[5],
                "inn": developer_info[6],
                "kpp": developer_info[7],
                "ogrn": developer_info[8],
                "photo": developer_info[9],
                "banned_workers": developer_info[10],
                "balance": developer_info[11],
                "founders": developer_info[12]
            }
        else:
            raise HTTPException(status_code=404, detail="Developer not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/developers/")
async def create_developer(developer: Developer):    
    try:
        existing_user = await db.select_db(id)
        if not existing_user:
            user_info = await db.insert_developers(developer.linked_to, developer.name, developer.fullname, developer.juridical_address, developer.factical_address, developer.inn, developer.kpp, developer.ogrn, developer.photo, developer.banned_workers, developer.balance, developer.founders)
            return {"detail": "success", "id": user_info["id"]}
        else:
            raise HTTPException(status_code=400, detail="User already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))