# EN: Main API routing file / ES: Archivo principal de rutas API
from fastapi import FastAPI
from pydantic import BaseModel
import funciones 

app = FastAPI()

# AVANCE 6: Almacenamiento Dinámico (Uso de Listas en lugar de variables simples)
# EN: Global list to store multiple records / ES: Lista global para guardar múltiples registros
base_datos_destinos = []

class DestinoInput(BaseModel):
    nombre: str
    dias: int
    prioridad: str

# AVANCE 6: Operación CRUD Básica (Agregar / Create)
@app.post("/forjar")
def forjar_destino(destino: DestinoInput):
    # Avance 5: Limpieza de datos
    nombre_limpio = destino.nombre.strip()
    energia = funciones.calcular_energia(destino.dias, destino.prioridad)
    
    nuevo_destino = {
        "nombre": nombre_limpio,
        "dias": destino.dias,
        "energia": energia
    }
    
    # AVANCE 6: Uso de .append() para almacenamiento dinámico
    base_datos_destinos.append(nuevo_destino)
    funciones.generar_reporte_consola(base_datos_destinos)
    
    # AVANCE 6: Mensaje de confirmación bilingüe
    return {
        "status": "success",
        "mensaje": f"ES: Registro exitoso. Destino '{nombre_limpio}' forjado. / EN: Success. Destiny forged.", 
        "energia": energia
    }

# AVANCE 6: Operación CRUD Básica (Consultar / Read)
@app.get("/destinos")
def listar_destinos():
    """
    EN: Iterates the list to show all records / ES: Recorre la lista para mostrar todos los registros
    """
    if not base_datos_destinos:
        return {"mensaje": "ES: No hay destinos en el tapiz. / EN: Tapestry is empty."}
    
    # Preparamos una lista formateada recorriendo la base de datos original
    lista_formateada = []
    for i, destino in enumerate(base_datos_destinos, 1):
        lista_formateada.append(f"{i}. {destino['nombre'].upper()} - Energía/Energy: {destino['energia']}")
        
    return {
        "header": "ES: LISTADO ACTUAL DE DESTINOS / EN: CURRENT DESTINIES LIST",
        "total_registros": len(base_datos_destinos),
        "destinos": lista_formateada
    }

@app.get("/buscar")
def buscar_destino(termino: str):
    # Avance 5 y 6: Búsqueda con tratamiento de cadenas
    termino_limpio = funciones.estandarizar_dato(termino)
    
    resultados = []
    # Recorremos la lista con un ciclo for (Requisito Avance 6)
    for d in base_datos_destinos:
        nombre_bd = funciones.estandarizar_dato(d["nombre"])
        if termino_limpio in nombre_bd:
            resultados.append(d)
            
    if not resultados:
        return {"mensaje": "EN: Item not found / ES: Item no encontrado"}
    return {"resultados": resultados}