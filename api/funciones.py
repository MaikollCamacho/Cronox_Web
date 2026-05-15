# EN: Business logic module / ES: Módulo de lógica de negocio (BIL)
from datetime import datetime

MULTIPLICADORES = {"alta": 3.0, "media": 2.0, "baja": 1.0}

def estandarizar_dato(texto_entrada):
    """Limpia espacios y estandariza a minúsculas (G5)."""
    return texto_entrada.strip().lower()

def calcular_dias_y_energia(fecha_str, prioridad_raw):
    """Calcula días restantes y la energía divina basada en la fecha exacta"""
    prioridad_limpia = estandarizar_dato(prioridad_raw)
    multiplicador = MULTIPLICADORES.get(prioridad_limpia, 1.0)
    
    try:
        # Convertir el texto de la fecha HTML a un objeto de tiempo en Python
        fecha_limite = datetime.fromisoformat(fecha_str)
        ahora = datetime.now()
        
        # Calcular diferencia
        diferencia = fecha_limite - ahora
        dias_reales = diferencia.days
        
        if dias_reales <= 0:
            energia = round(100.0 * multiplicador * 2, 2)
        else:
            energia = round((100.0 / dias_reales) * multiplicador, 2)
            
        return dias_reales, energia
    except ValueError:
        return 1, 100.0 # Respaldo en caso de error

def generar_reporte_consola(lista_destinos):
    """Genera reporte profesional alineado usando f-strings (G5)."""
    print("\n" + "="*75)
    print(f"| {'EN: SYSTEM REPORT / ES: REPORTE DEL SISTEMA':^71} |")
    print("="*75)
    # G5: Modificadores de ancho
    print(f"| {'ID':<10} | {'NAME/NOMBRE':<20} | {'DATE/FECHA':<16} | {'ENERGY':<10} |")
    print("-" * 75)
    
    for d in lista_destinos:
        id_o = d.get('id_oraculo', '')
        nombre = d.get('nombre', '').strip().upper() 
        fecha = d.get('fecha_entrega', '').replace("T", " ")[:16]
        energia = d.get('energia', 0.0)
        print(f"| {id_o:<10} | {nombre:<20} | {fecha:<16} | {energia:<10.2f} |")
    print("="*75 + "\n")