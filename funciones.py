# funciones.py
from datetime import datetime, timedelta

def crear_recordatorio(titulo: str, tiempo_horas: float, importancia: int, tipo: str):
    """
    Core logic to calculate priority and deadlines.
    Lógica principal para calcular prioridad y fechas límite.
    """
    
    # MATH OPERATION: Priority calculation (preventing division by zero)
    # OPERACIÓN MATEMÁTICA: Cálculo de prioridad (evitando división por cero)
    prioridad = round((importancia / max(tiempo_horas, 0.1)), 2)
    
    # Time handling using datetime library
    # Manejo de tiempo usando la librería datetime
    tiempo_actual = datetime.now()
    tiempo_final = tiempo_actual + timedelta(hours=tiempo_horas)
    
    return {
        "titulo": titulo,
        "tipo": tipo,
        "prioridad": prioridad,
        "fecha_limite": tiempo_final.strftime("%H:%M:%S"),
        "estado": "Olimpo"
    }