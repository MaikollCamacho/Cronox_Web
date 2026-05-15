# EN: Persistence Lab / ES: Laboratorio de Persistencia (Unidad 3)
import csv

def ejecutar_persistencia():
    # Datos de prueba basados en tu modelo
    datos = [
        {"id": "01", "nombre": "Zenin Gaming", "energia": 80.5},
        {"id": "02", "nombre": "Cronox App", "energia": 95.0}
    ]
    
    archivo_csv = "persistencia_test.csv"
    
    print("\n" + "="*50)
    print("💾 GUARDANDO DATOS (with open)...")
    try:
        # Implementación de persistencia real (Criterio 1.0)
        with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
            escritor = csv.DictWriter(file, fieldnames=["id", "nombre", "energia"])
            escritor.writeheader()
            escritor.writerows(datos)
        print(f"✅ Archivo '{archivo_csv}' creado exitosamente.")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")

    print("\n" + "="*50)
    print("📂 CARGANDO DATOS (Persistencia Real)...")
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            lector = csv.DictReader(file)
            for fila in lector:
                print(f"Cargado: {fila['nombre']} - Energía: {fila['energia']}")
    except FileNotFoundError:
        print("❌ El archivo no existe.")

if __name__ == "__main__":
    ejecutar_persistencia()