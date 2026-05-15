# EN: String manipulation lab / ES: Laboratorio de manipulación de cadenas

cadena_original = "   pRoDuCtO dE eJeMplO   "

# 1. .strip() para eliminar espacios
texto_strip = cadena_original.strip()
# 2. .lower() y .upper() para estandarizar
texto_lower = cadena_original.lower()
texto_upper = cadena_original.upper()
# 3. .replace() para sustituir
texto_replace = texto_strip.replace(" ", "_")
# 4. .split() para fragmentar
lista_split = texto_strip.split()

# Diseño de Salida (f-strings avanzados con alineación requerida)
print("\n" + "="*55)
print(f"{'MÉTODO':<18} | {'RESULTADO'}")
print("="*55)
print(f"{'Original':<18} | '{cadena_original}'")
print(f"{'.strip()':<18} | '{texto_strip}'")
print(f"{'.lower()':<18} | '{texto_lower}'")
print(f"{'.upper()':<18} | '{texto_upper}'")
print(f"{'.replace()':<18} | '{texto_replace}'")
print(f"{'.split()':<18} | {lista_split}")
print("="*55 + "\n")