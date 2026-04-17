# EN: Business logic module / ES: Módulo de lógica de negocio (BIL)

MULTIPLICADORES = {"alta": 3.0, "media": 2.0, "baja": 1.0}

def estandarizar_dato(texto_entrada):
    """
    EN: Cleans spaces and standardizes to lowercase.
    ES: Limpia espacios y estandariza a minúsculas (G5).
    """
    return texto_entrada.strip().lower()

def calcular_energia(dias, prioridad_raw):
    """EN: Calculates divine energy / ES: Calcula energía divina"""
    prioridad_limpia = estandarizar_dato(prioridad_raw)
    multiplicador = MULTIPLICADORES.get(prioridad_limpia, 1.0)
    
    if dias <= 0:
        return round(100.0 * multiplicador * 2, 2)
    return round((100.0 / dias) * multiplicador, 2)

def generar_reporte_consola(lista_destinos):
    """
    EN: Generates aligned professional report using f-strings.
    ES: Genera reporte profesional alineado usando f-strings (G5).
    """
    print("\n" + "="*68)
    print(f"| {'EN: SYSTEM REPORT / ES: REPORTE DEL SISTEMA':^64} |")
    print("="*68)
    # G5: Modificadores de ancho para alinear la tabla
    print(f"| {'ID':<10} | {'EN/ES: NAME/NOMBRE':<20} | {'DAYS/DÍAS':<10} | {'ENERGY/ENERGÍA':<15} |")
    print("-" * 68)
    
    for d in lista_destinos:
        id_o = d.get('id_oraculo', '')
        nombre = d.get('nombre', '').strip().upper() # G5: Tratamiento de cadenas
        dias = d.get('dias', 0)
        energia = d.get('energia', 0.0)
        print(f"| {id_o:<10} | {nombre:<20} | {dias:<10} | {energia:<15.2f} |")
    print("="*68 + "\n")