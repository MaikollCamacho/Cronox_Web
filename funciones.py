from datetime import datetime, timedelta

def crear_recordatorio(titulo: str, tiempo_horas: float):
    """Calcula el tiempo de expiración y asigna el estado inicial."""
    tiempo_actual = datetime.now()
    tiempo_final = tiempo_actual + timedelta(hours=tiempo_horas)
    
    recordatorio = {
        "titulo": titulo,
        "horas_asignadas": tiempo_horas,
        "fecha_creacion": tiempo_actual.strftime("%Y-%m-%d %H:%M:%S"),
        "fecha_limite": tiempo_final.strftime("%Y-%m-%d %H:%M:%S"),
        "estado": "Olimpo"  # Activo
    }
    return recordatorio

def enviar_al_tartaro(lista_recordatorios: list, indice: int):
    """Destierra un recordatorio al Tártaro (completado)."""
    if 0 <= indice < len(lista_recordatorios):
        lista_recordatorios[indice]["estado"] = "Tártaro"
        return True
    return False