from fastapi import FastAPI

app = FastAPI()
# python -m uvicorn module_16_1:app

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}
# python -m uvicorn module_16_1:app

@app.get("/user/admin")
async def news() -> dict:
    return {"message": f"Вы вошли как администратор!"}
# python -m uvicorn module_16_1:app

@app.get("/user/{user_id}")
async def news(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}
# python -m uvicorn module_16_1:app

@app.get("/user")
async def id_paginator(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст:  {age}"}
# python -m uvicorn module_16_1:app





