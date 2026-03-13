from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RecordatorioIn(BaseModel):
    titulo: str
    tiempo_horas: float

memoria_olimpo = []

@app.get("/api/recordatorios")
def ver_todos():
    return memoria_olimpo

@app.post("/api/recordatorios")
def invocar(rec: RecordatorioIn):
    recordatorio = {"titulo": rec.titulo, "tiempo": rec.tiempo_horas, "estado": "Olimpo"}
    memoria_olimpo.append(recordatorio)
    return recordatorio