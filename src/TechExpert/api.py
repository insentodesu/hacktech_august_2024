from fastapi import FastAPI, HTTPException, Request
from typing import Optional
import sqlite3, db

app = FastAPI()

async def open_connection():
    connect = sqlite3.connect("base.db")
    cursor = connect.cursor()
    return connect, cursor

async def close_connection(connect):
    connect.commit()
    connect.close()

async def select_users(id: Optional[int] = None):
    # try:
        connect, cursor = await open_connection()
        if id is not None:
            cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
            user_info = cursor.fetchone()
            if user_info:
                user_dict = {
                    "id": user_info[0],
                    "first_name": user_info[1],
                    "last_name": user_info[2],
                    "middle_name": user_info[3],
                    "type": user_info[4],
                    "verifed_identity": user_info[5],
                    "profile_photo": user_info[6],
                    "pass_photo": user_info[7],
                    "pass_series_num": user_info[8],
                    "dep_code_pass": user_info[9],
                    "date_of_issue": user_info[10],
                    "inn": user_info[11],
                    "specialization": user_info[12],
                    "verifed_specialization": user_info[13],
                    "balance": user_info[14],
                    "reserved_balance": user_info[15],
                    "bonus_balance": user_info[16]
                }
            else:
                user_dict = None
        else:
            cursor.execute("SELECT * FROM users")
            all_users = cursor.fetchall()
            user_dict = [{"id": user[0]} for user in all_users]
        
        await close_connection(connect)
        return user_dict
    # except Exception as e:
    #     return {"error": str(e)}

async def select_developers(id: Optional[int] = None):
    try:
        connect, cursor = await open_connection()
        if id is not None:
            cursor.execute("SELECT * FROM developers WHERE id = ?", (id,))
            developer_info = cursor.fetchone()
            if developer_info:
                developer_dict = {
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
                developer_dict = None
        else:
            cursor.execute("SELECT * FROM developers")
            all_developers = cursor.fetchall()
            developer_dict = [{"id": developer[0]} for developer in all_developers]
        
        await close_connection(connect)
        return developer_dict
    except Exception as e:
        return {"error": str(e)}

async def select_objects(id: Optional[int] = None):
    try:
        connect, cursor = await open_connection()
        if id is not None:
            cursor.execute("SELECT * FROM objects WHERE id = ?", (id,))
            object_info = cursor.fetchone()
            if object_info:
                object_dict = {
                    "id": object_info[0],
                    "developer": object_info[1],
                    "name": object_info[2],
                    "status": object_info[3],
                    "workers": object_info[4]
                }
            else:
                object_dict = None
        else:
            cursor.execute("SELECT * FROM objects")
            all_objects = cursor.fetchall()
            object_dict = [{"id": object[0]} for object in all_objects]
        
        await close_connection(connect)
        return object_dict
    except Exception as e:
        return {"error": str(e)}

@app.get("/users/{id}")
async def get_user(id: int):
    result = await select_users(id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result

@app.get("/developers/{id}")
async def get_developer(id: int):
    result = await select_developers(id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="Developer not found")
    return result

@app.get("/objects/{id}")
async def get_object(id: int):
    result = await select_objects(id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return result

@app.post("/users/")
async def create_user(request: Request):
    try:
        user = await request.json()
        users = await db.select_users()
        id = len(users) + 1
        print(id)
        connect, cursor = await open_connection()
        cursor.execute("""
            INSERT INTO users (id, first_name, last_name, middle_name, type, verifed_identity, profile_photo, pass_photo, pass_series_num, dep_code_pass, date_of_issue, inn, specialization, verifed_specialization, balance, reserved_balance, bonus_balance) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            id, user['first_name'], user['last_name'], user['middle_name'], user['type'], user['verifed_identity'], user['profile_photo'],
            user['pass_photo'], user['pass_series_num'], user['dep_code_pass'], user['date_of_issue'], user['inn'], user['specialization'],
            user['verifed_specialization'], user['balance'], user['reserved_balance'], user['bonus_balance']
        ))
        await close_connection(connect)
        return {"detail": "success", "id": id}
    except Exception as e:
        return {"error": str(e)}

@app.post("/developers/")
async def create_developer(request: Request):
    try:
        developer = await request.json()
        developers = await db.select_developers()
        id = len(developers) + 1
        print(id)
        connect, cursor = await open_connection()
        cursor.execute("""
            INSERT INTO developers (id, linked_to, name, fullname, juridical_address, factical_address, inn, kpp, ogrn, photo, banned_workers, balance, founders) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            id, developer['linked_to'], developer['name'], developer['fullname'], developer['juridical_address'], developer['factical_address'],
            developer['inn'], developer['kpp'], developer['ogrn'], developer['photo'], developer['banned_workers'], developer['balance'], developer['founders']
        ))
        await close_connection(connect)
        return {"detail": "success", "id": id}
    except Exception as e:
        return {"error": str(e)}

@app.post("/objects/")
async def create_object(request: Request):
    try:
        object = await request.json()
        objects = await db.select_objects()
        id = len(objects) + 1
        connect, cursor = await open_connection()
        cursor.execute("""
            INSERT INTO objects (id, developer, name, status, workers) 
            VALUES (?, ?, ?, ?, ?)
        """, (
            id, object['developer'], object['name'], object['status'], object['workers']
        ))
        await close_connection(connect)
        return {"detail": "success", "id": id}
    except Exception as e:
        return {"error": str(e)}