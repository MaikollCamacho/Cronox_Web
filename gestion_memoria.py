# EN: Volatile Memory Simulator / ES: Simulador de Memoria Volátil

print("\n" + "="*40)
print("1. CREACIÓN / CREATION")
# Inicializar lista con 3 elementos base
destinos = ["Atenas", "Esparta", "Troya"]
print(f"Estado actual: {destinos}")

print("\n" + "="*40)
print("2. EXPANSIÓN / EXPANSION")
# .append() para agregar al final
destinos.append("Tebas")
# .insert() para agregar en una posición específica (índice 1)
destinos.insert(1, "Olimpo")
print(f"Estado actual: {destinos}")

print("\n" + "="*40)
print("3. DEPURACIÓN / DEBUGGING")
# .remove() elimina por valor exacto
destinos.remove("Esparta")
# .pop() elimina el último elemento por defecto
destinos.pop() 
print(f"Estado actual: {destinos}")

print("\n" + "="*40)
print("4. ORDENAMIENTO / SORTING")
# .sort() organiza la lista alfabéticamente
destinos.sort()
print(f"Estado actual: {destinos}")

print("\n" + "="*40)
print("5. BÚSQUEDA / SEARCH")
# Validar con un condicional if si un elemento existe
if "Olimpo" in destinos:
    print("✅ EN: Element found / ES: El destino 'Olimpo' SÍ existe en la memoria.")
else:
    print("❌ EN: Not found / ES: El destino NO existe.")
print("="*40 + "\n")