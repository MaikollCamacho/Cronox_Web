# EN: Abstract Data Type Definition / ES: Definición de TAD (Unidad 3)
class DestinoTAD:
    """Clase que representa el TAD para la gestión de destinos (G3)."""
    def __init__(self, id_entidad, nombre, dias, energia):
        self.id_entidad = id_entidad
        self.nombre = nombre
        self.dias = dias
        self.energia = energia

    def __repr__(self):
        return f"DestinoTAD({self.id_entidad}, {self.nombre})"

# Ejemplo de uso para tu laboratorio:
if __name__ == "__main__":
    prueba = DestinoTAD("01", "Zenin Gaming", 5, 100.0)
    print(f"Instancia de clase (TAD) creada: {prueba}")