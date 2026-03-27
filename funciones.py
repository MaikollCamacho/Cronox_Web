# EN: Business logic module / ES: Módulo de lógica de negocio

MULTIPLICADORES = {"alta": 3.0, "media": 2.0, "baja": 1.0}

# INTEGRACIÓN PASO 2: Función de estandarización
def estandarizar_dato(texto_entrada):
    """
    EN: Cleans spaces and standardizes to lowercase for comparisons.
    ES: Limpia espacios y estandariza a minúsculas para comparaciones.
    """
    return texto_entrada.strip().lower()

def calcular_energia(dias, prioridad_raw):
    """EN: Calculates divine energy / ES: Calcula energía divina"""
    # Usamos la estandarización para evitar errores si escriben " AlTa "
    prioridad_limpia = estandarizar_dato(prioridad_raw)
    multiplicador = MULTIPLICADORES.get(prioridad_limpia, 1.0)
    
    if dias <= 0:
        return round(100.0 * multiplicador * 2, 2)
    return round((100.0 / dias) * multiplicador, 2)

# INTEGRACIÓN PASO 3: Reportes Profesionales en Consola
def generar_reporte_consola(lista_destinos):
    """
    EN: Generates aligned professional report in terminal.
    ES: Genera reporte profesional alineado en la terminal.
    """
    print("\n" + "="*60)
    # Uso de f-strings con alineación centrada (^60) y lateral (<20)
    print(f"| {'EN: SYSTEM REPORT / ES: REPORTE DEL SISTEMA':^56} |")
    print("="*60)
    print(f"| {'NAME / NOMBRE':<20} | {'DAYS / DÍAS':<12} | {'ENERGY / ENERGÍA':<17} |")
    print("-" * 60)
    for d in lista_destinos:
        # Aseguramos que los textos estén limpios para la tabla
        nombre = d.get('nombre', '').strip().upper()
        dias = d.get('dias', 0)
        energia = d.get('energia', 0.0)
        print(f"| {nombre:<20} | {dias:<12} | {energia:<17.2f} |")
    print("="*60 + "\n")