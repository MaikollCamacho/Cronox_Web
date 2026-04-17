# EN: Entity Modeling Lab / ES: Laboratorio de Modelado de Entidad
print("\n" + "="*50)
print("1. EN: COMPLEX RECORD / ES: REGISTRO COMPLEJO (G7)")
# Creamos un registro usando un Diccionario (Llave-Valor)
destino_prueba = {
    "clave_id": "DEST-01",
    "nombre": "Conquista de Troya",
    "dias": 10,
    "energia": 30.0
}
print(f"Original: {destino_prueba}")

print("\n" + "="*50)
print("2. EN: UPDATE RECORD / ES: ACTUALIZACIÓN (G7)")
# Buscamos por clave y modificamos sus atributos internos
destino_prueba["dias"] = 5
destino_prueba["energia"] = 60.0
print(f"Actualizado: {destino_prueba}")

print("\n" + "="*50)
print("3. EN: NESTED DICTIONARIES / ES: DICCIONARIOS ANIDADOS (G7)")
# Estructuración de una lista de diccionarios (Base de datos robusta)
base_datos = [
    destino_prueba,
    {"clave_id": "DEST-02", "nombre": "Defensa de Esparta", "dias": 20, "energia": 15.0}
]
print(f"BD Simulada: {base_datos}")
print("="*50 + "\n")
print("="*50 + "\n")
