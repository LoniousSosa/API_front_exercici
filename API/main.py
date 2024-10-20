from fastapi import FastAPI,HTTPException
from typing import List
from pydantic import BaseModel
from API_front_exercici.API import alumnos
from API_front_exercici.API import db_alumnos
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#a

class tablaAlumno(BaseModel):
    Nombre:str
    Ciclo:int
    Curso:str
    Grupo:str
    DescAula:str


class alumno(BaseModel):
    idAula:int
    nombre:str
    ciclo:int
    curso:str
    grupo:str
    createdAt:int
    updatedAt:int

class aula(BaseModel):
    descAula:str
    edificio:int
    piso:int
    createdAt:int
    updatedAt:int

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return FileResponse("API_front_exercici/front/html/index.html")

@app.get("/alumnes", response_class=HTMLResponse)
async def read_alumnes():
    return FileResponse("API_front_exercici/front/html/alumnes.html")

@app.get("/alumne/list", response_model= List[tablaAlumno])
def read_alumnos():
    adb = db_alumnos.read()
    alumnos_sch = alumnos.alumnos_schema(adb)
    
    return alumnos_sch

@app.get("/alumne/show/{id}",response_model= List[dict])
def read_alumno_id(id:int):
    if db_alumnos.read_id(id) is not None:
        adb = db_alumnos.read_id(id)
        alumno = alumnos.alumnos_schema(adb)
    
    else:
        raise HTTPException(status_code=404,detail="Item not found")
    
    return alumno

#Falla algo muy pequeño
@app.put("/alumne/update/{id}")
def update_votes(id:int,nombre:str,ciclo:int,curso:str,grupo:str):
    updated_records = db_alumnos.update_alumne(id,nombre,ciclo,curso,grupo)
    
    if updated_records == 0:
       raise HTTPException(status_code=404, detail="Items to update not found")


@app.delete("/alumne/delete/{id}")
def delete_alumne(id:int):
    deleted_records = db_alumnos.delete_alumne(id)
    if deleted_records == 0:
       raise HTTPException(status_code=404, detail="Items to delete not found") 
