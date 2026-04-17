# EN: Main API routing file / ES: Archivo principal de rutas API (BIL)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import funciones

app = FastAPI()

# EN: CORS configuration for frontend / ES: Configuración CORS para el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# G7: DICCIONARIOS ANIDADOS / EN: Nested Dictionaries
# ES: Lista global para guardar múltiples registros en memoria
base_datos_destinos = []

class DestinoInput(BaseModel):
    id_oraculo: str
    nombre: str
    dias: int
    prioridad: str

@app.post("/forjar")
def forjar_destino(destino: DestinoInput):
    # G5: TRATAMIENTO DE CADENAS / EN: String Treatment
    id_limpio = destino.id_oraculo.strip().upper()
    nombre_limpio = destino.nombre.strip()
    
    # G5: ESTANDARIZACIÓN / EN: Standardization (Evitar duplicidad)
    for d in base_datos_destinos:
        if d["id_oraculo"] == id_limpio:
            return {"status": "error", "mensaje": "ES: La clave ya existe. / EN: Key already exists."}

    energia = funciones.calcular_energia(destino.dias, destino.prioridad)
    
    # G7: REGISTROS COMPLEJOS / EN: Complex Records (Diccionario Llave-Valor)
    nuevo_destino = {
        "id_oraculo": id_limpio,
        "nombre": nombre_limpio,
        "dias": destino.dias,
        "prioridad": destino.prioridad.strip().capitalize(),
        "energia": energia
    }
    
    # G6: MÉTODOS DE LISTA / EN: List Methods (.append)
    base_datos_destinos.append(nuevo_destino)
    
    # G5: FORMATEO DE SALIDA / EN: Output Formatting (Imprime en consola)
    funciones.generar_reporte_consola(base_datos_destinos)
    
    return {"status": "success", "mensaje": f"ES: Destino forjado con éxito. / EN: Destiny successfully forged."}

@app.get("/destinos/ordenados")
def listar_destinos_ordenados():
    if not base_datos_destinos:
        return {"mensaje": "ES: Tapiz vacío. / EN: Empty tapestry."}
    
    # G6: ORDENAMIENTO / EN: Sorting (.sort)
    # ES: Ordenar lista por nivel de energía de mayor a menor
    base_datos_destinos.sort(key=lambda x: x["energia"], reverse=True)
    
    return {"destinos_ordenados": base_datos_destinos}

@app.delete("/destruir/{id_buscar}")
def destruir_destino(id_buscar: str):
    id_limpio = id_buscar.strip().upper()
    
    for destino in base_datos_destinos:
        if destino["id_oraculo"] == id_limpio:
            # G6: MÉTODOS DE LISTA / EN: List Methods (.remove)
            base_datos_destinos.remove(destino)
            return {"status": "success", "mensaje": "ES: Destino destruido. / EN: Destiny destroyed."}
            
    return {"status": "error", "mensaje": "ES: Clave no encontrada. / EN: Key not found."}