import sqlite3 as sql

async def open_connection():
    connect = sql.connect("base.db", check_same_thread=False)
    cursor = connect.cursor()
    return connect, cursor

async def close_connection(connect):
    connect.commit()
    connect.close()

async def create_db():
    try:
        connect, cursor = await open_connection()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id BIGINT,
            first_name TEXT,
            last_name TEXT,
            middle_name TEXT,
            type TEXT,
            verifed_identity BIGINT,
            profile_photo TEXT,
            pass_photo TEXT,
            pass_series_num TEXT,
            dep_code_pass TEXT,
            date_of_issue TEXT,
            inn BIGINT,
            specialization TEXT,
            verifed_specialization BIGINT,
            balance BIGINT,
            reserved_balance BIGINT,
            bonus_balance BIGINT
        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS developers (
            id BIGINT,
            linked_to BIGINT,
            name TEXT,
            fullname TEXT,
            juridical_address TEXT,
            factical_address TEXT,
            inn BIGINT,
            kpp BIGINT,
            ogrn BIGINT,
            photo TEXT,
            banned_workers TEXT,
            balance BIGINT,
            founders TEXT
        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS objects (
            id BIGINT,
            developer BIGINT,
            name TEXT,
            status TEXT,
            workers TEXT
        )""")
        await close_connection(connect)
        return "success"
    except Exception as e:
        return {"error": str(e)}

async def insert_users(first_name, last_name, middle_name, type, verifed_identity, profile_photo, pass_photo, pass_series_num, dep_code_pass, date_of_issue, inn, specialization, verifed_specialization, balance, reserved_balance, bonus_balance):
    try:
        connect, cursor = await open_connection()
        cursor.execute(f"SELECT * FROM users WHERE id = {id}")
        user_info = cursor.fetchone()
        if not user_info:
            id = len(cursor.fetchall()) + 1
            cursor.execute("""
                INSERT INTO users (
                    id, first_name, last_name, middle_name, type, verifed_identity, profile_photo, pass_photo, pass_series_num, dep_code_pass, date_of_issue, inn, specialization, verifed_specialization, balance, reserved_balance, bonus_balance
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (id, first_name, last_name, middle_name, type, verifed_identity, profile_photo, pass_photo, pass_series_num, dep_code_pass, date_of_issue, inn, specialization, verifed_specialization, balance, reserved_balance, bonus_balance))
        await close_connection(connect)
        return {"detail": "success", "id": id}
    except Exception as e:
        return {"error": str(e)} 

async def insert_developers(linked_to, name, fullname, juridical_address, factical_address, inn, kpp, ogrn, photo, banned_workers, balance, founders):
    try:
        connect, cursor = await open_connection()
        cursor.execute(f"SELECT * FROM developers WHERE id = {id}")
        developer_info = cursor.fetchone()
        if not developer_info:
            id = len(cursor.fetchall()) + 1
            cursor.execute("""
                INSERT INTO developers (
                    id, linked_to, name, fullname, juridical_address, factical_address, inn, kpp, ogrn, photo, banned_workers, balance, founders
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (id, linked_to, name, fullname, juridical_address, factical_address, inn, kpp, ogrn, photo, banned_workers, balance, founders))
        await close_connection(connect)
        return {"success", id}
    except Exception as e:
        return {"error": str(e)}

async def insert_objects(developer, name, status, workers):
    try:
        connect, cursor = await open_connection()
        cursor.execute(f"SELECT * FROM objects WHERE id = {id}")
        object_info = cursor.fetchone()
        if not object_info:
            id = len(cursor.fetchall()) + 1
            cursor.execute("""
                INSERT INTO objects (
                    id, developer, name, status, workers
                ) VALUES (?, ?, ?, ?, ?)
            """, (id, developer, name, status, workers))
        await close_connection(connect)
        return {"success", id}
    except Exception as e:
        return {"error": str(e)}

async def update_db(db, object, value, id):
    connect, cursor = await open_connection()
    if type(value) is str:
        if id != None:
            cursor.execute(f"UPDATE {db} SET {object} = '{value}' WHERE id = {id}")
        if id == None:
            cursor.execute(f"UPDATE {db} SET {object} = '{value}'")
    if type(value) is int:
        if id != None:
            cursor.execute(f"UPDATE {db} SET {object} = {value} WHERE id = {id}")
        if id == None:
            cursor.execute(f"UPDATE {db} SET {object} = {value}")
    await close_connection(connect)

async def select_users(id=None):
    try:
        connect, cursor = await open_connection()
        if id is not None:
            cursor.execute("SELECT * FROM users WHERE id = ?", (id))
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
    except Exception as e:
        return {"error": str(e)}
    
async def select_developers(id=None):
    try:
        connect, cursor = await open_connection()
        if id is not None:
            cursor.execute("SELECT * FROM developers WHERE id = ?", (id))
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
    
async def select_objects(id=None):
    try:
        connect, cursor = await open_connection()
        if id is not None:
            cursor.execute("SELECT * FROM objects WHERE id = ?", (id))
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