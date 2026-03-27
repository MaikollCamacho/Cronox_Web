# EN: Main API routing file / ES: Archivo principal de rutas API
from fastapi import FastAPI
from pydantic import BaseModel
import funciones # EN: Import our logic / ES: Importamos nuestra lógica

app = FastAPI()

# EN: Temporary database / ES: Base de datos temporal
base_datos_destinos = []

class DestinoInput(BaseModel):
    nombre: str
    dias: int
    prioridad: str

@app.post("/forjar")
def forjar_destino(destino: DestinoInput):
    # INTEGRACIÓN PASO 3: Validación de Entradas con .strip()
    # EN: Clean input string / ES: Limpiar cadena de entrada
    nombre_limpio = destino.nombre.strip()
    
    energia = funciones.calcular_energia(destino.dias, destino.prioridad)
    
    nuevo_destino = {
        "nombre": nombre_limpio,
        "dias": destino.dias,
        "energia": energia
    }
    base_datos_destinos.append(nuevo_destino)
    
    # EN: Print professional table in terminal / ES: Imprimir tabla profesional en terminal
    funciones.generar_reporte_consola(base_datos_destinos)
    
    return {"mensaje": f"Destino '{nombre_limpio}' forjado con éxito", "energia": energia}

@app.get("/buscar")
def buscar_destino(termino: str):
    # INTEGRACIÓN PASO 3: Estandarización de Búsquedas (ignora mayúsculas/minúsculas)
    # EN: Normalize search term / ES: Normalizar término de búsqueda
    termino_limpio = funciones.estandarizar_dato(termino)
    
    resultados = []
    for d in base_datos_destinos:
        # EN: Normalize database name / ES: Normalizar nombre en base de datos
        nombre_bd = funciones.estandarizar_dato(d["nombre"])
        if termino_limpio in nombre_bd:
            resultados.append(d)
            
    if not resultados:
        return {"mensaje": "EN: Not found / ES: No encontrado"}
    return {"resultados": resultados}