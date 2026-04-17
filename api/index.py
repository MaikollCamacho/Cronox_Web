# EN: Main API routing file / ES: Archivo principal de rutas API (BIL)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import funciones
import uuid 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# G7: DICCIONARIOS ANIDADOS 
base_datos_destinos = []

class DestinoInput(BaseModel):
    nombre: str
    fecha_entrega: str  # ¡Cambio clave! Ahora recibe fecha en vez de días
    prioridad: str

@app.post("/forjar")
def forjar_destino(destino: DestinoInput):
    id_generado = f"DEST-{uuid.uuid4().hex[:4].upper()}"
    
    # G5: Tratamiento
    nombre_limpio = destino.nombre.strip()
    dias, energia = funciones.calcular_dias_y_energia(destino.fecha_entrega, destino.prioridad)
    
    # G7: REGISTROS COMPLEJOS
    nuevo_destino = {
        "id_oraculo": id_generado,
        "nombre": nombre_limpio,
        "fecha_entrega": destino.fecha_entrega, # Guardamos la fecha exacta
        "prioridad": destino.prioridad.strip().capitalize(),
        "energia": energia
    }
    
    # G6: MÉTODOS DE LISTA
    base_datos_destinos.append(nuevo_destino)
    funciones.generar_reporte_consola(base_datos_destinos)
    
    return {"status": "success", "mensaje": f"ES: Destino forjado ({id_generado})."}

@app.get("/destinos/ordenados")
def listar_destinos_ordenados():
    if not base_datos_destinos:
        return {"mensaje": "ES: Tapiz vacío. / EN: Empty tapestry."}
    
    # G6: ORDENAMIENTO
    base_datos_destinos.sort(key=lambda x: x["energia"], reverse=True)
    return {"destinos_ordenados": base_datos_destinos}

@app.delete("/destruir/{id_buscar}")
def destruir_destino(id_buscar: str):
    id_limpio = id_buscar.strip().upper()
    for destino in base_datos_destinos:
        if destino["id_oraculo"] == id_limpio:
            # G6: MÉTODOS DE LISTA (.remove)
            base_datos_destinos.remove(destino)
            return {"status": "success", "mensaje": "ES: Destino destruido."}
            
    return {"status": "error", "mensaje": "ES: Clave no encontrada."}