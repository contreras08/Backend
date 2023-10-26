from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#uvicorn users:app --reload

#entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id= 1, name= "Daniel",surname= "Contreras",url= "https://contreras.dev",age= 43),
              User(id= 2, name= "Valeria",surname= "Florez",url= "https://florez.com",age= 23),
              User(id= 3, name= "Luz",surname= "Restrepo",url= "https://restrepo.es",age= 52)]


#Simulando una base de datos
@app.get("/usersjson")
async def usersjson():
    return  [{"name": "Daniel", "surname": "Diaz", "url": "https://contreras.dev"},
             {"name": "Valeria", "surname":"Florez", "url": "https://florez.com"},
             {"name": "Luz", "surname":"Restrepo", "url": "https://restrepo.es"}]
    
@app.get("/users")
async def users():
    return users_list

#Llamado por path (ejemplo /user/1)
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
   
    
#Llamado por query (ejemplo /user/?id=1)
@app.get("/user/")
async def user(id: int):
     return search_user(id)
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
       return list(users)[0]
    except:
          return {"error": "No se ha encontrado el usuario"}
        
    
@app.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    users_list.append(user)
    return user
        
        
@app.put("/user/")
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    
    return user

@app.delete("/user/{id}")
async def user(id: int):
    
    found = False
     
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
           del users_list[index]
           found = True
           
    if not found:
        return {"error": "No se ha eliminado el usuario"}
    
    return user
    
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
       return list(users)[0]
    except:
          return {"error": "No se ha encontrado el usuario"}




