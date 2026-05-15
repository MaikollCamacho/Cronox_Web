# EN: Abstract Data Type & Persistence / ES: TAD y Persistencia (Unidad 3)
import csv

class Destino:
    def __init__(self, id_o, nombre, fecha, energia):
        self.id_o = id_o
        self.nombre = nombre
        self.fecha = fecha
        self.energia = energia

    def __repr__(self):
        return f"TAD_Destino({self.id_o}, {self.nombre})"

def guardar_datos_csv(lista_objetos, nombre_archivo="datos_proyecto.csv"):
    """Guarda la información usando with open() (Criterio 1.0 - Unidad 3)."""
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            # Cabecera
            escritor.writerow(["ID", "Nombre", "Fecha", "Energia"])
            for obj in lista_objetos:
                escritor.writerow([obj.id_o, obj.nombre, obj.fecha, obj.energia])
        print(f"✅ Datos guardados en {nombre_archivo}")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")

def cargar_datos_csv(nombre_archivo="datos_proyecto.csv"):
    """Carga automática al inicio (Criterio 1.0 - Unidad 3)."""
    lista_cargada = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Re-instanciar el TAD
                nuevo_obj = Destino(fila['ID'], fila['Nombre'], fila['Fecha'], float(fila['Energia']))
                lista_cargada.append(nuevo_obj)
        print(f"✅ {len(lista_cargada)} registros cargados.")
    except FileNotFoundError:
        print("⚠️ No se encontró archivo previo. Iniciando base de datos vacía.")
    return lista_cargada