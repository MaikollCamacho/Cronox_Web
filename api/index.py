# api/index.py
from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

# Path adjustment for Vercel deployment
# Ajuste de ruta para el despliegue en Vercel
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from funciones import crear_recordatorio

app = FastAPI()

# Data model for incoming requests
# Modelo de datos para las peticiones entrantes
class RecordatorioIn(BaseModel):
    titulo: str
    tiempo_horas: float
    importancia: int
    tipo: str

# Database in memory (will reset on server restart)
# Base de datos en memoria (se reiniciará al reiniciar el servidor)
memoria_olimpo = []

@app.get("/api/recordatorios")
def ver_todos():
    # Sort by priority: highest first
    # Ordenar por prioridad: los más altos primero
    return sorted(memoria_olimpo, key=lambda x: x['prioridad'], reverse=True)

@app.post("/api/recordatorios")
def invocar(rec: RecordatorioIn):
    # Use our math logic from funciones.py
    # Usar nuestra lógica matemática de funciones.py
    nuevo = crear_recordatorio(rec.titulo, rec.tiempo_horas, rec.importancia, rec.tipo)
    memoria_olimpo.append(nuevo)
    return nuevo

@app.delete("/api/recordatorios/{indice}")
def desterrar(indice: int):
    # Sort before deleting to ensure index matches the frontend view
    # Ordenar antes de borrar para asegurar que el índice coincida con la vista
    memoria_olimpo.sort(key=lambda x: x['prioridad'], reverse=True)
    if 0 <= indice < len(memoria_olimpo):
        eliminado = memoria_olimpo.pop(indice)
        return {"mensaje": f"Desterrado al Tártaro: {eliminado['titulo']}"}
    return {"error": "No existe"}