# EN: Volatile Memory Simulator / ES: Simulador de Memoria Volátil

print("\n" + "="*50)
print("1. EN: CREATION / ES: CREACIÓN")
# EN: Initialize list with 3 base elements / ES: Inicializar lista con 3 elementos base
destinos = ["Esparta", "Troya", "Atenas"]
print(f"EN: Current state / ES: Estado actual: {destinos}")

print("\n" + "="*50)
print("2. EN: EXPANSION / ES: EXPANSIÓN")
# EN: Ask user for input / ES: Pedir dato al usuario
nuevo_destino = input("👉 ES: Escribe el nombre de un nuevo destino: ")

# EN: .append() adds to the end / ES: .append() agrega al final de la lista
destinos.append(nuevo_destino)
# EN: .insert() adds at specific index / ES: .insert() agrega en la posición 1
destinos.insert(1, "Olimpo")
print(f"EN: Current state / ES: Estado actual: {destinos}")

print("\n" + "="*50)
print("3. EN: DEBUGGING / ES: DEPURACIÓN")
# EN: .remove() deletes exact value / ES: .remove() elimina por valor exacto
destinos.remove("Troya")
# EN: .pop() deletes the last element / ES: .pop() elimina el último elemento
destinos.pop() 
print(f"EN: Current state / ES: Estado actual: {destinos}")

print("\n" + "="*50)
print("4. EN: SORTING / ES: ORDENAMIENTO")
# EN: .sort() organizes alphabetically / ES: .sort() organiza alfabéticamente
destinos.sort()
print(f"EN: Current state / ES: Estado actual: {destinos}")

print("\n" + "="*50)
print("5. EN: SEARCH / ES: BÚSQUEDA")
# EN: Validate with if condition / ES: Validar con condicional if si el elemento existe
if "Olimpo" in destinos:
    print("✅ EN: Element found / ES: El destino 'Olimpo' SÍ existe en la memoria.")
else:
    print("❌ EN: Not found / ES: El destino 'Olimpo' NO existe en la memoria.")
print("="*50 + "\n")